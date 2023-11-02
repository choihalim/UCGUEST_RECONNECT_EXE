import logging
import subprocess
import time
import traceback
import warnings
from selenium import webdriver

# Set up logging
warnings.filterwarnings(action='ignore')
logging.basicConfig(filename='wifi_login.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

###########################################################

# Define network name, URLs, and login information
network_name = "UC_Guest"
target_url = "https://www.ultiumcell.com/"
website_link = "http://10.95.4.50/guest/guest_reg.php?cmd=login&mac=58:86:94:f4:02:e7&ip=10.95.60.164&essid=UC%5FGuest&apname=UC_OA_ABA_1F_AP_59.91&apgroup=UC_OA&url=http%3A%2F%2Fwww%2Emsftconnecttest%2Ecom%2Fredirect&_browser=1"
username = "guest"
email = "guest@gmail.com"
phone = "2483184938"

# Define actions
sks = "send_keys"
click = "click"

# Define element IDs for form fields
element_for_username = "ID_formf9f21400_guest_register_visitor_name"
element_for_email = "ID_formf9f21400_guest_register_email"
element_for_phone = "ID_formf9f21400_guest_register_visitor_phone_intl"
element_for_checkbox = "ID_formf9f21400_guest_register_creator_accept_terms"
element_for_submit_1 = "ID_formf9f21400_guest_register_submit"
element_for_submit_2 = "ID_forme2917b01_guest_register_receipt_submit"

###########################################################

required_packages = [
    'pandas',
    'selenium',
    'chromedriver_autoinstaller',
]

# install required packages
def pip_install(module):
    try:

        print(module + ' module install')
        subprocess.run(['pip', 'install', module], capture_output=True,
                       text=True, creationflags=subprocess.CREATE_NO_WINDOW)

        print(module + ' module install complete')
        return True
    except:
        print(traceback.format_exc())
        return False

for package in required_packages:
    try:
        __import__(package)  # Check if the package is already installed
        print(f'{package} is already installed.')
    except ImportError:
        if pip_install(package):
            __import__(package)  # Try to import the package after installation
            print(f'{package} is now installed and imported.')

try:
    import pandas as pd
except:
    if pip_install('pandas'):
        import pandas as pd
try:
    import subprocess
except:
    if pip_install('subprocess'):
        import subprocess
try:
    import time
except:
    if pip_install('time'):
        import time
try:
    import traceback
except:
    if pip_install('traceback'):
        import traceback
# try:
#     import 
        
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
except:
    if pip_install('selenium'):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    if pip_install('webdriver-manager'):
        from webdriver_manager.chrome import ChromeDriverManager
    pip_install('chromedriver_autoinstaller')

###########################################################


# disconnects from UC_Guest
def disconnect_from_current_wifi():
    try:
        # Use the netsh command to disconnect from the currently connected network
        subprocess.run(['netsh', 'wlan', 'disconnect'], check=True)
        print("Disconnected from the current Wi-Fi network")
        return True
    except subprocess.CalledProcessError as e:
        logging.error("An error occurred during the disconnection process: %s", e)
        print("Failed to disconnect from the current Wi-Fi network")
        return False

# connects to UC_Guest
def connect_to_uc_guest():
    try:
        # Use the netsh command to connect to the "UC_Guest" network
        subprocess.run(['netsh', 'wlan', 'connect',
                       'name=UC_Guest'], check=True)
        print("Connected to 'UC_Guest' Wi-Fi network")
        return True
    except subprocess.CalledProcessError as e:
        logging.error("Failed to connect to 'UC_Guest' Wi-Fi network. Please check that the connection is available: %s", e)
        print("Failed to connect to 'UC_Guest' Wi-Fi network. Please check that the connection is available.")
        return False

# fills out the guest form
def fill_form(browser, element_name, id, action):
    try:
        element = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.NAME, id))
        )
        if action == sks:
            element.send_keys(element_name)
        elif action == click:
            element.click()
    except TimeoutException as e:
        logging.error(f"Timeout waiting for element: {element_name}, id: {id}")
        logging.error(e)
        return False
    return True

# closes Chrome browser
def close_browser(browser):
    try:
        browser.quit()
        print("Browser closed successfully.")
    except Exception as e:
        logging.error("An error occurred while closing the browser.")
        logging.error(e)

# closes Chrome browser when target URL is reached
def close_browser_when_complete(browser, target_url):
    try:
        WebDriverWait(browser, 10).until(
            lambda x: x.current_url == target_url
        )
        browser.quit()
        print(f"Browser closed after reaching the target URL: {target_url}")
    except TimeoutException as e:
        logging.error(
            "Login failed, UC site never reached. Browser will close now.")
        logging.error(e)
        browser.quit()

# conducts login + browser close
def login_website():
    try:
        browser = webdriver.Chrome()  # uncomment this line,for chrome users
        browser.get((website_link))
        fill_form(browser, username, element_for_username, sks)
        fill_form(browser, email, element_for_email, sks)
        fill_form(browser, phone, element_for_phone, sks)
        fill_form(browser, None, element_for_checkbox, click)
        fill_form(browser, None, element_for_submit_1, click)
        fill_form(browser, None, element_for_submit_2, click)
        close_browser_when_complete(browser, target_url)
        return True
    except Exception as e:
        logging.error("An error occurred during the login process...")
        logging.error(e)
        close_browser(browser)
        return False

def main():
    try:
        if disconnect_from_current_wifi():
            print("Attempting to connect to UC_Guest...")
            logging.info("Success: Disconnected from the current Wi-Fi network")
            time.sleep(5)
            if connect_to_uc_guest():
                logging.info("Success: Connected to UC_Guest")
                time.sleep(5)
                if login_website():
                    logging.info("Success: Reconnected to UC_Guest, guest wifi access form complete")
                    return
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
