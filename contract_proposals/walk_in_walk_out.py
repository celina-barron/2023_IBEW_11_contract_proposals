from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title 

#keep the chrome browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def walk_in_walk_out():
    # set up the browser driver
    driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "ARTICLE III Hours - Wages - Working Conditions 3.02 (b)"
    most_closely_addresses = "Walk in, walk out, + parking time."
    language_of_the_proposal = """From: (b) Where multiple reporting locations are utilized, the men shall report to their assigned reporting location on their own time and shall be allowed adequate pickup time and will leave the reporting location at quitting time.
    \nTo: (b) Where the travel time between initial entrance or final exit of worker parking and worker reporting or quitting location exceeds 5 minutes workers shall be allowed adequate pickup and travel time to enter and exit the job parking at the shift starting and quitting time."""
    reasoning = "Our workers are excessively made to walk in, walk out, or wait in long lines in their car to park or exit parking on their own time. Being that contractors control reporting locations and parking venues, contractors should cover the travel time it takes to enter and exit."

    # find the input fields by xpath and fill them
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_6"]').\
    send_keys("Inside Wireman")
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field_7_1"]').\
    click()
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_8"]').\
    send_keys(articles_and_sections)
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_9"]').\
    send_keys(most_closely_addresses)
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_10"]').\
    send_keys(language_of_the_proposal)
    driver.find_element(by=By.XPATH, value='//*[@id="kb_field__42ccad-55_11"]').\
    send_keys(reasoning)


walk_in_walk_out()
