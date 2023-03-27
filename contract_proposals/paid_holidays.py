from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title 

#keep the chrome browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def paid_holidays():
    # set up the browser driver
    driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    # time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Adding a Paid Holidays section after section 3.03 (g) Sick Pay"
    most_closely_addresses = "Making four holidays paid holidays."
    language_of_the_proposal = """(h) Holiday Pay: Workers shall receive a full day's wages for the unworked Thanksgiving Day, Day After Thanksgiving, Christmas Day, and New Year's Day holidays."""
    reasoning = """The winter holiday season should not create financial stress on our workers."""

    # find the input fields by xpath and fill them
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_6"]').\
    send_keys("Inside Wireman")
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field_7_0"]').\
    click()
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_8"]').\
    send_keys(articles_and_sections)
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_9"]').\
    send_keys(most_closely_addresses)
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_10"]').\
    send_keys(language_of_the_proposal)
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_11"]').\
    send_keys(reasoning)


paid_holidays()
