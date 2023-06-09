from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

#keep the chrome browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# set up the browser driver
chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
driver = webdriver.Chrome(options=options, )
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title


def twenty_over_three():
    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    # time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Wedge Scale 3.05"
    most_closely_addresses = "Wages"
    language_of_the_proposal = "Journeyman Wadge ingrease of $20 over 3 years"
    reasoning = """The cost of living is rapidly increasing. More and more of our members are reliant on working overtime and are forced to move out or to the edges of the county causing our members to make hours long commutes to work because our members cannot afford to live in Los Angeles. These long hours and long commutes take a serious toll on our members often with devastating impacts on our members lives, including but not limited to extreme fatigue and mental health stress. The instances of fatigue and mental health related incidents, accidents, and death are escalating to an intolerable frequency. Working as skilled and trained Union Electricians, we should all easily be able to afford the middle class American dream, but right now contractors exploit our labor and reap the benefits we deserve."""

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


twenty_over_three()
