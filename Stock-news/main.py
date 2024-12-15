import requests
from twilio.rest import Client

account_sid = "account_sid"
auth_token = "auth_token"
Phone_number = "phone_number"


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def send_sms(arrow, percent, article):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"TSLA: {arrow}{percent:.2f}%\nHeadline: {article['title']}\nBrief: {article['description']}",
        from_=Phone_number,
        to="Receiver",
    )


def get_news(arrow, percent):
    news_parameters = {
        "qInTitle": "TSLA",
        "apiKey": "API KEY",
        "language": "en",
        "sortBy": "publishedAt"
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]
    for article in news_data:
        send_sms(arrow, percent, article)

def get_stocks():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": "API KEY",
    }

    stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in stock_data.items()]
    yesterday_price = float(data_list[0]["4. close"])
    day_before_price = float(data_list[1]["4. close"])

    if yesterday_price > day_before_price:
        arrow = "🔺"
    else:
        arrow = "🔻"
    diff = abs(yesterday_price - day_before_price)
    percentage_diff = (diff / yesterday_price) * 100

    if percentage_diff > 0.1:
        get_news(arrow, percentage_diff)

get_stocks()


