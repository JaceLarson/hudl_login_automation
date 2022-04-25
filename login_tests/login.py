from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import config as cfg

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait

driver.get("https://www.hudl.com/login")
wait = WebDriverWait(driver, 10)


wait.until(ec.element_to_be_clickable((By.ID, "email")))
#arrange
email_text_box = driver.find_element(By.ID, "email")
password_text_box = driver.find_element(By.ID, "password")

#act
email_text_box.send_keys(cfg.credentials["email"])
password_text_box.send_keys(cfg.credentials["password"])

log_in_button = driver.find_element(By.ID, "logIn")
log_in_button.click()

wait = WebDriverWait(driver, 10)
wait.until(ec.presence_of_element_located((By.CLASS_NAME, "hui-globaluseritem__email")))
email_displayed_on_home_page = driver.find_element(By.CLASS_NAME, "hui-globaluseritem__email").get_attribute("outerText")

#assert (user is logged in and correct email is showing)
assert email_displayed_on_home_page == cfg.credentials["email"]

driver.quit()

