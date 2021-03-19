from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
url = "https://wpartner.wemakeprice.com/login"
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(3)
driver = driver.get(url)