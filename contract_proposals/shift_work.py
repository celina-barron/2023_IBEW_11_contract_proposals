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


def shift_work():
    # set up the browser driver
    driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Shift Work 3.12"
    most_closely_addresses = "Contractors adjusting of the starting time to dodge the payment of the higher wage rate."
    language_of_the_proposal = """From: There shall be no pyramiding of overtime rates and double the straight rate shall be the maximum compensation for any hour worked. There shall be no requirement for a first shift (day shift) when either the second shift (swing shift) or third shift
(graveyard shift) is worked. The shift rate of pay is determined by the start time of the shift (see chart below).
First Shift (Day Shift): Start time between 5:00AM and 9:30AM (Straight TimeRate)
Second Shift (Swing): Start time between 9:31AM and 8:00PM (Straight Time Rate +17.3%)
Third Shift (Graveyard): Start time between 8:01PM and 4:59AM (Straight Time Rate +31.4%)

\n To: Overtime multipliers shall be applied to the Shift Pay Rate worked. There shall be no requirement for a first shift (day shift) when either the second shift (swing shift) or third shift (graveyard shift) is worked.
When a customer requires or jobsite conditions require the working of a shift that is outside of First Shifts hours, and 4 or more of those hours are worked in the higher paid shift of the two, then the entire non-standard shift shall be paid at the higher of the two wage rates. When determining the hours for this non-first shift rate, the hours listed above shall prevail. Adjustment of the starting time to avoid the payment of the higher wage rate shall not be allowed.
First Shift (Day Shift): between 5:00AM and 9:30AM (Straight TimeRate)
Second Shift (Swing): between 9:30AM and 8:00PM (Straight Time Rate +17.3%)
Third Shift (Graveyard): between 8:00PM and 4:59AM (Straight Time Rate +31.4%)"""
    reasoning = """If 4 or more hours are worked at a higher shift our members should be paid the higher paid shift pay. This proposal mirrors language NECA has agreed to with IBEW LU 100. Contractors should not be allowed to skip out on paying members what they deserve."""

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


shift_work()
