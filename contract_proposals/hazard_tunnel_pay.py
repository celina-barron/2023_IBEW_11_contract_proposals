from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 

#keep the chrome browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def hazard_tunnel_pay():
    # set up the browser driver
    driver = webdriver.Chrome(options=options, executable_path="path/to/executable")

    # navigate to the form page
    driver.get("https://www.ibew11.org/contract-proposals/")

    # time.sleep(2)

    # variables for text to be inserted
    articles_and_sections = "Wedge Scale 3.05"
    most_closely_addresses = "Tunnel + Hazard Pay"
    language_of_the_proposal = """From: Tunnel Work... Apprentices equal to wage percentage in program as above plus 10%.\n
    To: Tunnel/Hazard Work... Apprentices equal to wage % in program as above plus 10%. All shifts where FRC/NOMEX clothing 
    is a requirement to be worn for work in chemical plants, process plants, refineries (including pipeline work upstream or 
    downstream), or any other facility to protect personnel from hazards such as chemical, environmental, radiological, 
    mechanical irritants, etc., shall be paid at the hazard/tunnel pay rate. All shifts where electrical construction 
    installation, maintenance or repair work in tunnels or where a self-contained oxygen breathing apparatus or similar 
    self-rescue device is a requirement to be worn for work, shall be paid at the tunnel/hazard pay rate."""
    reasoning = "Workers in these dangerous conditions should be appropriately compensated."

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


hazard_tunnel_pay()
