from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 

#keep the chrome browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def increased_boot_stipend():
    # set up the browser driver
    driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Section 3.25 (d)"
    most_closely_addresses = "Increasing the boot stipend"
    language_of_the_proposal = """From: (d) When specialized safety shoes (e.g., steel toe/composite toe boots) are required by the customer as a condition of work at the job site, the employee shall be reimbursed with a stipend in the amount of $125.00 toward the cost of the footwear. For the purposes of this section, “specialized safety shoes” shall be defined as that footwear that has been determined by Cal OSHA to be a contractor purchasing responsibility.
    \nTo: (d) When specialized safety shoes (e.g., steel toe/composite toe boots) are required by the customer as a condition of work at the job site, the employee shall be reimbursed with a stipend in the amount of $200.00 toward the cost of the footwear. For the purposes of this section, “specialized safety shoes” shall be defined as that footwear that has been determined by Cal OSHA to be a contractor purchasing responsibility."""
    reasoning = "Boot prices continue to go up."

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


increased_boot_stipend()
