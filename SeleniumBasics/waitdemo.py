from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# === Setup Chrome Options ===
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# === Initialize WebDriver ===
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chr_options
)

# === Open the Target URL ===
driver.get("https://demo.automationtesting.in/")
driver.maximize_window()

# === 1. Static Wait (wait fixed time) ===
# time.sleep(2)  # Not recommended in production

# === 2. Implicit Wait (applies to all find_element) ===
driver.implicitly_wait(3)

# === Fill Email Field and Click Button ===
driver.find_element(By.ID, "email").send_keys("Test@gmail.com")
driver.find_element(By.ID, "enterimg").click()

# === 3. Explicit Wait (wait for specific condition) ===
wait = WebDriverWait(driver, 5)

# Wait until "First Name" input is visible, then fill it
first_name_input = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//input[@placeholder='First Name']")
))
first_name_input.send_keys("Niharika")

# === Optional: Perform more actions or close browser later
# driver.quit()