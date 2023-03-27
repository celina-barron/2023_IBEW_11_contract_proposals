from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title 

#keep the chrome browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def manditory_app_rotation():
    # set up the browser driver
    # driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
    driver = webdriver.Chrome(options=options, )

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    # time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Adding a Manditory Apprentice Rotation section to the end of ARTICLE V: STANDARD INSIDE APPRENTICESHIP & TRAINING LANGUAGE"
    most_closely_addresses = "Adding a Manditory Apprentice Rotation"
    language_of_the_proposal = """Add: 5.17 The apprentice be rotated at least three times in their apprenticeship in order to receive a diversity of work experience. Consideration of the prior experience of the apprentice when making a rotation will be made. The apprentice shall be required to accept all rotations."""
    reasoning = """Some of our apprentices are coming out of the apprenticeship without well rounded education or experience. Rotating apprentices will allow them to have a broader range of experiences. Many Locals rotate their apprentices. This language closely mirrors that of IBEW 569."""

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


manditory_app_rotation()
