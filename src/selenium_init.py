import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def selenium_connect(weblink):
    print("Please wait... (Selenium connection)")
    opts = Options()
    opts.add_argument(" --headless")
    opts.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    os.chdir("../")
    chrome_driver = os.getcwd() + "\\drivers\\chromedriver.exe"
    driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)
    driver.get(weblink)

    return driver
