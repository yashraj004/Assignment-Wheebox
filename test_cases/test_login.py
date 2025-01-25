from  selenium import webdriver


def setup():


    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    return driver
