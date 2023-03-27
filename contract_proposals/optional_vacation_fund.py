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


def optional_vacation_fund():
    # set up the browser driver
    driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Section 7.40. Vacation Fund in Credit Union"
    most_closely_addresses = "Make the Vacation Fund optional"
    language_of_the_proposal = """From: Section 7.40. The Employer shall deduct and forward payment to each employee, by paying to an account maintained in his/her name at the Los Angeles Electrical Workers Credit Union (LAEWCU), a state-chartered credit union. The amount to be deducted from the gross pay of each employee shall be the amount specified on the approved rate bulletin sheet, currently at 8.5%. This amount is not in excess of, but is a part of the wage scale, and shall be paid to the LAEWCU by remitting said amount along with other contributions to the existing "Lock Box" account.
    \nTo: Section 7.40. If approved by the employee the Employer shall deduct and forward payment to each employee, by paying to an account maintained in their name at the Los Angeles Electrical Workers Credit Union (LAEWCU), a state-chartered credit union. The amount to be deducted from the gross pay of each employee shall be the amount specified on the approved rate bulletin sheet, currently at 8.5%. This amount is not in excess of, but is a part of the wage scale, and shall be paid to the LAEWCU by remitting said amount along with other contributions to the existing "Lock Box" account."""
    reasoning = "Some workers may want a vacation fund, but all workers should not be forced to participate."

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


optional_vacation_fund()