from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chr_options
)

# Open demo page
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

# Store Parent Window Handle
parent = driver.current_window_handle
print("Parent Window Handle:", parent)

# Click button to open new window
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

# Get list of all open windows
windows = driver.window_handles

# Switch to the new (child) window
for win in windows:
    if win != parent:
        driver.switch_to.window(win)
        break

# Do some action in the child window
driver.find_element(By.XPATH, "//span[contains(text(),'Downloads')]").click()

# Close child window
driver.close()

# Switch back to the parent
driver.switch_to.window(parent)

# Optional: Repeat the action again or close
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

# Final actions or cleanup
time.sleep(3)
driver.quit()