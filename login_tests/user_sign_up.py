from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import config as cfg

SIGN_UP_URL = "https://www.hudl.com/register/signup"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait

driver.get("https://www.hudl.com/login")
wait = WebDriverWait(driver, 10)

wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "sign-up-trial")))
#arrange
sign_up_button = driver.find_element(By.CLASS_NAME, "sign-up-trial")

#act
sign_up_button.click()

#assert (resend email page is showing and correct email is showing)
driver.implicitly_wait(5)
assert driver.current_url == SIGN_UP_URL

driver.quit()

