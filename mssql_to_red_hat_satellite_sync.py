# This script is built to run as is (provided you fill in necessary server information, email addresses, Satellite user/OrgID/URL, etc) on a Windows Server
# with Windows Credential manager.  Be sure you run the following pip commands:

# pip install smtplib
# pip install pyodbc
# pip install requests
# pip install urllib3
# pip install keyring
# pip install time (maybe not necessary

# Any version of Python3 should work.  Keyring syntax would be  keyring.get_password("Name of Service", "Username")

# Check any section with underscores.  I didn't take time to fully modularize EVERY variable, but most of them.  

# check Email details section also for smtp server and email address.  


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyodbc
import requests
import urllib3
import keyring
import time 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Record the start time
start_time = time.time()

# Email details
smtp_server = ''
smtp_port = 25
email_address = ''

server = ''
database = ''
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'

SATELLITE_USER = ""
SATELLITE_URL = ""
ORGANIZATION_ID = ""

SATELLITE_TOKEN = keyring.get_password("","")

if not SATELLITE_TOKEN:
    raise ValueError("Failed to retrieve the SATELLITE_TOKEN from Windows Credential Manager.")
else:
    print("Satellite token is successfully loaded!")

AAP_PASSWORD = keyring.get_password("","")
if not AAP_PASSWORD:
    raise ValueError("Failed to retrieve the aap_password from Windows Credential Manager.")
else:
    print("AAP token is successfully loaded!")

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Bcc'] = email_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(email_address, [email_address], msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def get_host_id(server_name):
    full_server_name = f"{server_name.lower()}._____.com"  #making name lower case as most server names in Satellite are lower case
    
    response = requests.get(
        f"https://_____.com/api/hosts?search=name=\"{full_server_name}\"",
        auth=(SATELLITE_USER, SATELLITE_TOKEN),
        headers={'Content-Type': 'application/json'},
        verify=False
    )
    
    if response.status_code == 200:
        hosts = response.json()
        if hosts and 'results' in hosts and hosts['results']:
            return hosts['results'][0]['id']
        else:
            print(f"No host found with name {full_server_name}.")
            return None
    else:
        print(f"Failed to retrieve host ID for {full_server_name}. Error: {response.text}")
        return None

def create_host_collection(server_group_name):
    response = requests.post(
        f"{SATELLITE_URL}/host_collections",
        json={'name': server_group_name, 'organization_id': ORGANIZATION_ID},
        auth=(SATELLITE_USER, SATELLITE_TOKEN),
        headers={'Content-Type': 'application/json'},
        verify=False
    )
    if response.status_code == 201:
        print(f"Successfully created host collection {server_group_name}.")
        return response.json()['id']
    else:
        print(f"Failed to create host collection {server_group_name}. Error: {response.text}")
        return None

def add_host_to_collection(host_collection_id, host_id):
    response = requests.put(
        f"https://___.com/katello/api/host_collections/{host_collection_id}/add_hosts",
        json={'host_ids': [host_id]},
        auth=(SATELLITE_USER, SATELLITE_TOKEN),
        headers={'Content-Type': 'application/json'},
        verify=False
    )
    if response.status_code in [200, 201]:
        print(f"Successfully added host ID {host_id} to host collection ID {host_collection_id}.")
    else:
        print(f"Failed to add host ID {host_id} to host collection ID {host_collection_id}. Error: {response.text}")
        
def remove_all_hosts_from_collections():
    response = requests.get(
        f"{SATELLITE_URL}/host_collections",
        auth=(SATELLITE_USER, SATELLITE_TOKEN),
        headers={'Content-Type': 'application/json'},
        verify=False
    )
    
    if response.status_code == 200:
        host_collections = response.json()
        if host_collections and 'results' in host_collections and host_collections['results']:
            for host_collection in host_collections['results']:
                host_collection_id = host_collection['id']
                host_collection_name = host_collection['name']

                hosts_response = requests.get(
                    f"{SATELLITE_URL}/host_collections/{host_collection_id}",
                    auth=(SATELLITE_USER, SATELLITE_TOKEN),
                    headers={'Content-Type': 'application/json'},
                    verify=False
                )
                
                if hosts_response.status_code == 200:
                    hosts = hosts_response.json()
                    host_ids = hosts.get('host_ids', [])

                    if host_ids:
                        payload = {
                            "host_ids": host_ids
                        }
                        
                        clear_response = requests.put(
                            f"{SATELLITE_URL}/host_collections/{host_collection_id}/remove_hosts",
                            json=payload,
                            auth=(SATELLITE_USER, SATELLITE_TOKEN),
                            headers={'Content-Type': 'application/json'},
                            verify=False
                        )
                        if clear_response.status_code in [200, 204]:
                            print(f"Successfully removed all hosts from host collection '{host_collection_name}' (ID {host_collection_id}).")
                        else:
                            print(f"Failed to remove hosts from host collection '{host_collection_name}' (ID {host_collection_id}). Error: {clear_response.text}")
                    else:
                        print(f"No hosts found in host collection '{host_collection_name}' (ID {host_collection_id}).")
    else:
        print(f"Failed to retrieve host collections for clearing hosts. Error: {response.text}")

def delete_host_collections(existing_server_group_names):
    response = requests.get(
        f"{SATELLITE_URL}/host_collections",
        auth=(SATELLITE_USER, SATELLITE_TOKEN),
        headers={'Content-Type': 'application/json'},
        verify=False
    )
    
    if response.status_code == 200:
        host_collections = response.json()
        if host_collections and 'results' in host_collections and host_collections['results']:
            for host_collection in host_collections['results']:
                host_collection_name = host_collection['name']
                host_collection_id = host_collection['id']
                
                if host_collection_name not in existing_server_group_names:
                    delete_response = requests.delete(
                        f"{SATELLITE_URL}/host_collections/{host_collection_id}",
                        auth=(SATELLITE_USER, SATELLITE_TOKEN),
                        headers={'Content-Type': 'application/json'},
                        verify=False
                    )
                    if delete_response.status_code in [200, 204]:
                        print(f"Successfully deleted host collection '{host_collection_name}' (ID {host_collection_id}).")
                    else:
                        print(f"Failed to delete host collection '{host_collection_name}' (ID {host_collection_id}). Error: {delete_response.text}")
    else:
        print(f"Failed to retrieve host collections for deletion. Error: {response.text}")

def main():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
        SELECT  ####
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        existing_server_group_names = [row[0] for row in results]

        # Delete host collections that are not in the existing server group names from APART
        delete_host_collections(existing_server_group_names)

        # Remove all hosts from all host collections before importing latest hosts and patch group names into host collections in satellite.
        remove_all_hosts_from_collections()

        for row in results:
            server_group_name = row[0]
            server_name = row[1]
            print(server_group_name + " " + server_name)

            # Get host ID from Satellite with the modified server name
            host_id = get_host_id(server_name)
            if host_id is None:
                print(f"Skipping server {server_name} as it was not found in Satellite.")
                continue

            # Find or create the host collection
            response = requests.get(
                f"{SATELLITE_URL}/host_collections?search=name=\"{server_group_name}\"&organization_id={ORGANIZATION_ID}",
                auth=(SATELLITE_USER, SATELLITE_TOKEN),
                headers={'Content-Type': 'application/json'},
                verify=False
            )

            if response.status_code == 200:
                host_collections = response.json()
                if host_collections and 'results' in host_collections and host_collections['results']:
                    host_collection_id = host_collections['results'][0]['id']
                else:
                    print(f"No host collection found with name {server_group_name}. Creating new host collection.")
                    host_collection_id = create_host_collection(server_group_name)

                if host_collection_id:
                    add_host_to_collection(host_collection_id, host_id)
            else:
                print(f"Failed to retrieve host collections. Error: {response.text}")
                send_email("Host Collection Retrieval Failed", f"Failed to retrieve host collections. Error: {response.text}")
                return

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Calculate hours, minutes, and seconds
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the elapsed time string
        elapsed_time_str = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
        
        send_email("Sync Successful", f"The synchronization process completed successfully.\nElapsed time: {elapsed_time_str}")

    except Exception as e:
        print(f"An error occurred: {e}")
        send_email("Sync Failed", f"An error occurred during synchronization: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred in the main process of script: {e}")
        send_email("Sync Failed", f"An error occurred in the main process: {e}")
