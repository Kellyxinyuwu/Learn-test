from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Initialize Chrome driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Go to the demo form site
driver.get("https://demo.automationtesting.in/Register.html")

try:
    # ✅ Wait for "Full Name" label
    label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Full Name')]"))
    )
    print("✅ Label found:", label.text)

    # ✅ Wait for First Name field and input text
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
    )
    first_name.send_keys("Kelly")

    # ✅ Wait for Last Name field and input text
    last_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Last Name']"))
    )
    last_name.send_keys("Wu")

    print("✅ Form fields filled successfully.")

except Exception as e:
    print("❌ Something went wrong:", e)

finally:
    # Keep browser open due to detach option OR safely quit here:
    # driver.quit()
    pass