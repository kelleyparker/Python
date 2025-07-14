import requests
import keyring
import urllib3
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

start_time = time.time()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://____.com"
api_url = f"{base_url}/api/v2/job_templates/"
inventory_api_url = f"{base_url}/api/v2/inventories/242/groups/"
project_id = __
inventory_id = __
credential_id = ___

api_key = keyring.get_password("___","___")

if not api_key:
    raise ValueError("Failed to retrieve the Red Hat AAP API Key from Windows Credential Manager.")
else:
    print("Red Hat AAP API Key is successfully loaded!")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

smtp_server = '____'
smtp_port = 25
email_addresses = '_____'

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_addresses.split(',')[0].strip()
    msg['To'] = email_addresses
    msg['Bcc'] = email_addresses
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(msg['From'], email_addresses.split(','), msg.as_string())
        print(f"Email sent successfully to {email_addresses}")
    except Exception as e:
        print(f"Failed to send email to {email_addresses}: {e}")

groups = []
url = inventory_api_url

while url:
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    groups.extend(data['results'])
    url = data.get('next')
    if url:
        url = base_url + url

def job_template_exists(template_name):
    response = requests.get(api_url, headers=headers, verify=False)
    if response.status_code == 200:
        templates = response.json().get('results', [])
        for template in templates:
            if template['name'] == template_name:
                return True
    return False

def delete_matching_templates():
    url = api_url
    while url:
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            templates = data.get('results', [])
            for template in templates:
                name = template['name'].lower()
                if "beta" in name and ("svr_chk" in name or "patch_rhel" in name):
                    template_id = template['id']
                    delete_url = f"{api_url}{template_id}/"
                    delete_response = requests.delete(delete_url, headers=headers, verify=False)
                    if delete_response.status_code == 204:
                        print(f"Deleted template: {template['name']}")
                    else:
                        print(f"Failed to delete template: {template['name']}, Status Code: {delete_response.status_code}")
            url = data.get('next')
            if url:
                url = base_url + url
        else:
            print(f"Failed to retrieve templates, Status Code: {response.status_code}")
            break

try:
    send_email("AAP Script Started", "The AAP job template creation script has started.")

    delete_matching_templates()

    for group in groups:
        group_name = group['name']
        if "foreman_hostcollection_lxp" in group_name:
            formatted_name = group_name.replace('foreman_hostcollection_', '').replace('_', '-').upper()
            extra_vars = json.dumps({"run_hosts": group_name})

            svr_chk_name = f"Svr_Chk - {formatted_name} - beta"
            patch_rhel_name = f"Patch_RHEL - {formatted_name} - beta"

            if not job_template_exists(svr_chk_name):
                payload_svr_chk = {
                    "name": svr_chk_name,
                    "description": "",
                    "project": project_id,
                    "inventory": inventory_id,
                    "job_type": "run",
                    "playbook": "svr_chk.yml",
                    "forks": 20,
                    "verbosity": 0,
                    "extra_vars": extra_vars
                }

                response_svr_chk = requests.post(api_url, headers=headers, json=payload_svr_chk, verify=False)
                print(response_svr_chk.status_code)
                try:
                    print(response_svr_chk.json())
                    job_template_id_svr_chk = response_svr_chk.json().get('id')
                except ValueError:
                    print("Failed to parse response as JSON:", response_svr_chk.text)
                    continue

                if job_template_id_svr_chk:
                    credentials_url_svr_chk = f"{base_url}/api/v2/job_templates/{job_template_id_svr_chk}/credentials/"
                    payload_associate = {'associate': True, 'id': credential_id}
                    response_associate_svr_chk = requests.post(credentials_url_svr_chk, headers=headers, json=payload_associate, verify=False)
                    print(response_associate_svr_chk.status_code)
                    try:
                        print(response_associate_svr_chk.json())
                    except ValueError:
                        print("Failed to parse response as JSON:", response_associate_svr_chk.text)

            if not job_template_exists(patch_rhel_name):
                payload_patch_rhel = {
                    "name": patch_rhel_name,
                    "description": "This is an example job template",
                    "project": project_id,
                    "inventory": inventory_id,
                    "job_type": "run",
                    "playbook": "patch_rhel.yml",
                    "forks": 20,
                    "verbosity": 0,
                    "extra_vars": extra_vars
                }

                response_patch_rhel = requests.post(api_url, headers=headers, json=payload_patch_rhel, verify=False)
                print(response_patch_rhel.status_code)
                try:
                    print(response_patch_rhel.json())
                    job_template_id_patch_rhel = response_patch_rhel.json().get('id')
                except ValueError:
                    print("Failed to parse response as JSON:", response_patch_rhel.text)
                    continue

                if job_template_id_patch_rhel:
                    credentials_url_patch_rhel = f"{base_url}/api/v2/job_templates/{job_template_id_patch_rhel}/credentials/"
                    payload_associate = {'associate': True, 'id': credential_id}
                    response_associate_patch_rhel = requests.post(credentials_url_patch_rhel, headers=headers, json=payload_associate, verify=False)
                    print(response_associate_patch_rhel.status_code)
                    try:
                        print(response_associate_patch_rhel.json())
                    except ValueError:
                        print("Failed to parse response as JSON:", response_associate_patch_rhel.text)

    end_time = time.time()
    elapsed_time = end_time - start_time
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    elapsed_time_str = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

    send_email("AAP Script Completed", f"The AAP job template creation script has completed successfully.\nElapsed time: {elapsed_time_str}")

except Exception as e:
    print(f"An error occurred: {e}")
    send_email("AAP Script Failed", f"An error occurred during the AAP job template creation script: {e}")
