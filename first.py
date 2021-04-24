from selenium import webdriver

from datetime import datetime

from random import randint

driver = webdriver.Chrome (executable_path="C:\\BrowserDrivers\\chromedriver.exe")

driver.get("https://www.y8.com/")

now = datetime.now().strftime("%Y-%m-%d_%H%M%S")

number = str(randint(1,10000))
directory = r'C:\Python_Selenium\pythonProject\MY_FIRST_AUTO\screenshots'


driver.get_screenshot_as_file(str(directory) + "\\" + now + "Y8.png")

driver.quit()
