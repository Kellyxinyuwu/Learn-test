from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Initialize Chrome driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chr_options
)

# Open the target page with frames
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# ------- Switch To Frames Window Examples -------

# --- By frame index ---
# driver.switch_to.frame(0)

# --- By frame ID ---
driver.switch_to.frame("singleframe")  # OR
# driver.switch_to.frame("SingleFrame")  # if that is the name

# --- Using WebElement ---
# single_frame = driver.find_element(By.XPATH, "//div[@id='Single']/iframe")
# driver.switch_to.frame(single_frame)

# Find input inside frame
text = driver.find_element(By.TAG_NAME, "input")
text.send_keys("This is text box")

# Return to main content from frame
driver.switch_to.default_content()