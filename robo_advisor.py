# this is the "app/robo_advisor.py" file

import requests
import json
import datetime

date = datetime.date.today()
time = datetime.datetime.now()
date_time = date, time.strftime("%I:%M:%S %p")

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# INFO INPUTS

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
response = requests.get(request_url)


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

# assuming first day is on top of list
dates = list(tsd.keys())

date = dates[0]

latest_close = tsd[date]["4. close"]

high_prices = []
low_prices = []


for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float((high_price))
    low_prices.append(float((low_price))

#max of all prices
recent_high = max(high_prices)
recent_low = min(low_prices)

#breakpoint()



print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {date_time}") #need to fix this
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")