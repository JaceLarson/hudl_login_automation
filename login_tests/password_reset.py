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

wait.until(ec.element_to_be_clickable((By.ID, "forgot-password-link")))
need_help_button = driver.find_element(By.ID, "forgot-password-link")
need_help_button.click()

#assert (resend email page is showing and correct email is showing)
wait.until(ec.element_to_be_clickable((By.ID, "forgot-email")))

assert driver.find_element(By.ID, "forgot-email").is_displayed
assert driver.find_element(By.ID, "resetBtn").is_displayed
assert driver.find_element(By.ID, "forgot-email").get_attribute("value") == cfg.credentials["email"]

driver.quit()

