from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set Chrome options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Create driver with options
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chr_options
)

# Open the target website
driver.get("https://demo.automationtesting.in/Index.html")

'''Locators:
By.ID
By.NAME
By.CLASS_NAME
By.TAG_NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT
By.CSS_SELECTOR
By.XPATH
'''

# Find email text box and send keys
email_text = driver.find_element(By.ID, 'email')
email_text.send_keys("test@gmail.com")

# Find and click the 'entering' button
driver.find_element(By.ID, 'enterimg').click()