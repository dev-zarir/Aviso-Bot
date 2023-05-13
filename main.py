from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium_recaptcha.components import find_until_clicklable, find_until_located
from time import sleep

email = "mariamkhanam1979@gmail.com"
password = "mariam@1"

d=print
def print(*a, **kw):
    kw["flush"] = True
    return d(*a, **kw)

print("Openning Browser")
options=webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://aviso.bz/login")
find_until_located(driver, By.CSS_SELECTOR, 'input[name="username"]').send_keys(email)
find_until_located(driver, By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)
find_until_clicklable(driver, By.ID, "button-login").click()
print("Logging in...")

sleep(600)