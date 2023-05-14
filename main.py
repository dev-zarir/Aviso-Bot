from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium_recaptcha.components import find_until_clicklable, find_until_located
from time import sleep

email = "mariamkhanam1979@gmail.com"
password = "mariam@1"
cookie = "_ym_uid=1683481656190358898; _ym_d=1683481656; _vid_t=fVmAOhgv8IpjJI6Ztk8Pf5Sjr4XJxtgj8OOM4h1o4oKeRHddKZiWohtU+wrkrQSxyWXhJZlDmWbIfw==; mnu_title4=1; PHPSESSID=dsm4s279tgrk6cnerufl30orju; menu_ref=4b4743cf320d1fb0de8deb97d10ecab5; _ym_isad=2; cenrifugo_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDEwMjc3IiwiZXhwIjoxNjg0MDYzMTc2fQ.t4x1ULkhPFNzpZp-EXuljiVDRuutlWTA2MT3x_3vlro; cenrifugo_token_exp=1684063176; googtrans=null; googtrans=null"

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
