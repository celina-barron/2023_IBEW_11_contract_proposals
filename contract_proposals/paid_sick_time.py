from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 

#keep the chrome browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def paid_sick_time():
    # set up the browser driver
    driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Overtime Section 3.03 (g) Sick Pay"
    most_closely_addresses = "Stop waiving our right to sick pay"
    language_of_the_proposal = """From: (g) Sick Pay: The parties to this Agreement hereby agree to WAIVE the requirements of any statute, ordinance, rule, law or regulation mandating paid sick leave for employees within its jurisdiction including, but not limited to, Article 1.5 (commencing with Section 245) of the California labor code and California labor code Section 2810.5. Any employer who is signatory to this agreement shall not be required to comply with said statute, ordinance, rule, law or regulation, and any employee covered by this agreement shall not have any right or cause of action against any signatory employer or Local 11 for violation of said statute, ordinance, rule, law or regulation.
    \nTo: (g) Sick Pay: The parties to this Agreement hereby agree to ABIDE BY the requirements of any statute, ordinance, rule, law or regulation mandating paid sick leave for employees within its jurisdiction including, but not limited to, Article 1.5 (commencing with Section 245) of the California labor code and California labor code Section 2810.5. Any employer who is signatory to this agreement shall not be required to comply with said statute, ordinance, rule, law or regulation, and any employee covered by this agreement shall not have any right or cause of action against any signatory employer or Local 11 for violation of said statute, ordinance, rule, law or regulation."""
    reasoning = """Members who cannot go to work due to illness should be paid sick time in accordance with any required statute, ordinance, rule, law or regulation mandating paid sick leave. These are benefits we are supposed to be getting. Why should we continue to give them away?"""

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


paid_sick_time()
