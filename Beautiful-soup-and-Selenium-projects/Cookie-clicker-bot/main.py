from selenium import webdriver
from selenium.webdriver.common.by import By
import time

timeout = time.time() + 60*5
five_seconds = time.time() + 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
addons = driver.find_elements(By.CSS_SELECTOR, value="#store b")
addons_list = [x.text for x in addons if x.text.strip() != ""]
reversed_addons = addons_list[::-1]
last_addons = [element.replace(",", "") for element in reversed_addons]

while True:
    cookie.click()

    if time.time() >= timeout:
        driver.quit()
        break
    if time.time() > five_seconds:
        money = driver.find_element(By.ID, value="money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)
        for addon in last_addons:
            if int(money) >= int(addon.split(' - ')[1]):
                addon_name = addon.split(' - ')[0]
                click_addon = driver.find_element(By.ID, value=f"buy{addon_name}")
                click_addon.click()
                break
        five_seconds = int(time.time()) + 5

cookies_per_second = driver.find_element(By.ID, value='cps')
print(cookies_per_second.text
      )