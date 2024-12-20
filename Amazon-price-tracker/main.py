import requests
import bs4
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')
RECIPIENT = os.getenv('RECIPIENT')
SMTP_ADDRESS = os.getenv('SMTP_ADDRESS')

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

url = 'https://appbrewery.github.io/instant_pot/'
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(live_url)
web_site = response.content

soup = bs4.BeautifulSoup(web_site, 'html.parser')

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split('$')[1]
price_in_float = float(price_without_currency)

name = soup.find(id="productTitle").get_text().strip()
letter_content = f"Subject: Low Price Alert - {name}\n\nHey there! I just wanted to let you know that the price of your favorite instant pot has dropped to ${price_in_float}. Here's the link: {live_url}"



if price_in_float < 100:
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT,
            msg=letter_content.encode("utf-8"))
