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


def doubletime():
    # set up the browser driver
    driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    # time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Overtime: 3.03(a)"
    most_closely_addresses = "All overtime as double time."
    language_of_the_proposal = """From: (a) Overtime on all types of construction shall be paid at time and one-half the regular straight time rate of pay for hours worked. The overtime rate shall be double the straight time rate of pay on Sunday, the following Holidays, and after twelve (12) hours on any day.
\nTo: (a) Overtime on all types of construction shall be paid at double time the shift rate of pay for hours worked on Saturday, Sunday, the following Holidays, after eight (8) hours on any day, or after forty (40) hours in any Monday to Sunday week."""
    reasoning = "Our workers are excessively laid off and out of work, while a small handful of our workers are made to work mismanaged jobs that require overtime."

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


doubletime()
