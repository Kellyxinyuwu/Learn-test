from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chr_options
)

# Navigate to the demo registration form
driver.get("https://demo.automationtesting.in/Register.html")

# Click on the gender radio button (e.g., Male)
# XPath targets: <input value="Male">
driver.find_element(By.XPATH, "//input[@value='Male']").click()

# Radio Button
driver.find_element(By.XPATH, "//input[@value='Male']").click()

# Check Box and get Attribute
li = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for ele in li:
    val = ele.get_attribute('value')
    print(val)
    if val == 'Cricket':
        ele.click()