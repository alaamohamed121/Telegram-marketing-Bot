from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
message = input("enter the message:")
photo_path = input(r"enter photopath:")
filename= input("enter file name:")
phone = input("enter phone number:")

# Create ChromeOptions object with headless mode enabled
chrome_options = Options()
# chrome_options.add_argument('--headless')

# Launch Chrome in headless mode
driver = webdriver.Chrome(options=chrome_options)
# Navigate to the Telegram link
driver.get('https://web.telegram.org/k/')

# Wait for the page to load
time.sleep(5)


phone_founder = driver.find_element(By.XPATH , "//div[@class='c-ripple']")
phone_founder.click()

time.sleep(2)
phone_number = driver.find_elements(By.XPATH , "//div[@class='input-field-input']")
phone_number[1].send_keys(phone)
time.sleep(3)

next_button = driver.find_elements(By.XPATH , "//div[@class='c-ripple']")
next_button[1].click()
code = input("enter the code:")

code_type = driver.find_element(By.XPATH , "//input[@class='input-field-input']")
code_type.send_keys(code)
time.sleep(2)
with open(filename, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            try:
                url = "https://web.telegram.org/k/#@" +line.strip()
                time.sleep(3)
                # Open a new tab using JavaScript
                driver.execute_script("window.open('');")
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                driver.close()

                # Switch to the new tab
                driver.switch_to.window(driver.window_handles[0])

                # Paste the contents of the current row from the file
                driver.get(url.strip())
                time.sleep(2)
                
                # find the attachment button and click it
                attachment_button = driver.find_element(By.XPATH,"//div[@class='btn-icon btn-menu-toggle attach-file tgico-attach']")
                attachment_button.click()
                time.sleep(5)
      

                upload_button = driver.find_element(By.XPATH ,"//input[@type='file']")
                upload_button.send_keys(photo_path)
                time.sleep(5)

                # wait for the photo to upload
                message_button = driver.find_elements(By.XPATH , "//div[@class='input-message-input i18n scrollable scrollable-y no-scrollbar']")
                message_button[1].send_keys(message)

                # wait for the photo to upload
                time.sleep(5)
                send_button = driver.find_element(By.XPATH , "//button[@class='btn-primary btn-color-primary rp']")
                send_button.click()
                time.sleep(2)

                # delete the current line from the file
                del lines[i]
                with open(filename, "w") as f:
                    f.writelines(lines)
                time.sleep(5)
            except:
                next
