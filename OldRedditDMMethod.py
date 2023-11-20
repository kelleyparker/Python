from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

# Set up the web driver (you may need to install the Selenium library)
driver = webdriver.Chrome()

# Open the Reddit login page
driver.get("https://old.reddit.com/login/?dest=https%3A%2F%2Fold.reddit.com%2Fmessage%2Fcompose%2F")

# Wait for the username input field to be present
try:
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_login"))
    )
    print("Username input found.")
except Exception as e:
    print("Error finding username input:", str(e))

# Add a 1-second delay before entering the username
time.sleep(1)
# Enter the username
username_input.send_keys("pokequick")

# Find the password input field
password_input = driver.find_element(By.ID, "passwd_login")

# Add a 1-second delay before entering the password
time.sleep(1)
# Enter the password
password_input.send_keys("F@$tB@ll98")

# Find the login button using XPath and click it
try:
    # Updated to use XPath for submit button with type, tabindex, and text content
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="submit" and @tabindex="3" and contains(text(), "log in")]'))
    )
    print("Login button found.")
except Exception as e:
    print("Error finding login button:", str(e))

login_button.click()

# Wait for the login to complete
try:
    WebDriverWait(driver, 10).until(
        EC.url_contains("https://old.reddit.com/message/compose/")
    )
    print("Login successful.")
except Exception as e:
    print("Error waiting for login:", str(e))

# Add a 1-second delay before opening the compose message page
time.sleep(1)

# Now, open the compose message page
driver.get("https://old.reddit.com/message/compose/")

# Read usernames from the file
with open("usernames.txt", "r") as file:
    usernames = file.read().splitlines()

# Loop through each username in the list
for username in usernames:
    # Find the "to" input element by its HTML element name
    to_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "to"))
    )

    # Replace "" with the actual username you want to send the message to
    to_input.clear()
    # Add a 1-second delay before entering the "to" field
    time.sleep(1)
    to_input.send_keys(username)

    # Find the "subject" input element by its HTML element name using By.NAME
    subject_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "subject"))
    )

    # Fill the "subject" input element with the specified subject
    subject_input.clear()
    # Add a 1-second delay before entering the subject
    time.sleep(1)
    subject_input.send_keys("SUBJECT TEXT")

    # Find the "text" textarea element by its HTML element name
    text_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/form[2]/div[7]/div/div/div[2]/div/div[1]/textarea'))
    )

    # Add a 1-second delay before entering text in the textarea
    time.sleep(1)

    # Use JavaScript to set the value of the textarea to an empty string
    driver.execute_script("arguments[0].value = '';", text_area)

    # Add a 1-second delay before entering text in the textarea
    time.sleep(1)

    # Enter text in the "text" textarea element using Selenium's send_keys method
    text_area.send_keys("Test Message")

    # Add a 1-second delay before clicking the "send" button
    time.sleep(1)

    # Find the "send" button by its HTML element ID
    send_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "send"))
    )

    # Click the "send" button
    send_button.click()

# Add a 1-second delay before closing the browser window
time.sleep(1)

# Close the browser window
driver.close()

# Print success message with username and current date/time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Success! Messages sent to usernames in usernames.txt at {current_time}")
