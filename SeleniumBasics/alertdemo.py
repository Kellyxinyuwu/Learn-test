from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Open the Alerts demo page
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# --- Alert with OK ---
driver.find_element(By.ID, 'OKTab').click()

# Wait and switch to alert
alert = wait.until(EC.alert_is_present())
print("OK Alert Text:", alert.text)
alert.accept()

# --- Alert with OK & Cancel ---
driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()
driver.find_element(By.ID, 'CancelTab').click()

alert = wait.until(EC.alert_is_present())
print("Confirm Alert Text:", alert.text)
alert.dismiss()  # or alert.accept()

# --- Alert with Textbox ---
driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()
driver.find_element(By.ID, 'Textbox').click()

alert = wait.until(EC.alert_is_present())
print("Prompt Alert Text:", alert.text)
alert.send_keys("Kelly Wu")   # Send text to the prompt
alert.accept()

time.sleep(2)
driver.quit()