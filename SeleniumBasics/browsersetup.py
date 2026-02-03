from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# create a web driver
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

driver.get("https://www.google.com/")

