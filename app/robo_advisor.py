# this is the "app/robo_advisor.py" file

import csv
import json
import os
from dotenv import load_dotenv

import requests
from datetime import datetime

load_dotenv()

now = datetime.now()
print(now.strftime('%Y/%m/%d %I:%M:%S'))

#date = datetime.date.today()
#time = datetime.datetime.now()
#date_time = date, time.strftime("%I:%M:%S %p")

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# INFO INPUTS

symbol = input("Please input a stock symbol in all upper-case letters: ")
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(request_url)


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

# assuming first day is on top of list
dates = list(tsd.keys())

date = dates[0]

latest_close = tsd[date]["4. close"]
latest_day = tsd[date]

high_prices = []
low_prices = []


for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

#max of all prices
recent_high = max(high_prices)
recent_low = min(low_prices)



# csv-mgmt/write_teams.py

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
#os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
csv_headers = fieldnames=["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open", "high", "low", "close", "volume"])
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
    })
 


print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {dates}") #need to fix this
print("-------------------------")
print(f"LATEST DAY: {dates[0]}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"RECOMMENDATION REASON: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
