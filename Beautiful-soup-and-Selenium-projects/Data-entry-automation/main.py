from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

URL = "https://appbrewery.github.io/Zillow-Clone/"
workURL = 'Your Google Form link here'

response = requests.get(URL, headers=header)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

addresses = soup.find_all(name='address')
address_names = [x.text.replace(" | ", " ").strip() for x in addresses]

price = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
prices = [x.text.strip().split('+')[0].split('/')[0] for x in price]

links = soup.find_all('a', class_='StyledPropertyCardDataArea-anchor')
link_names = [x['href'] for x in links]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(workURL)
for i in range(len(address_names)):
    time.sleep(3)
    first_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first_answer.send_keys(address_names[i])
    second_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_answer.send_keys(prices[i])
    third_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_answer.send_keys(link_names[i])
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    another_answer = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_answer.click()

driver.quit()