# this is the "app/robo_advisor.py" file

import csv
import json
import os
from dotenv import load_dotenv


import requests
from datetime import datetime
import validators


load_dotenv()

now = datetime.now()
#print(now.strftime('%Y/%m/%d %I:%M:%S%p'))
request_time = now.strftime('%Y/%m/%d %I:%M:%S%p')

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# INFO INPUTS

user_choice = input("Please input a stock symbol: ")
user_choice = user_choice.upper()

#print(user_choice.isdigit())

#preliminary data validation
#Step 1 - test that user input is not too long
if len(user_choice) < 7:
    pass
else:
    print("Oops, we are expecting a properly formatted stock symbol such as 'MSFT'. Please try again.")
    exit()

#Step 2 - test that user input does not contain any numbers
contains_digit = False
for character in user_choice:
    if character.isdigit():
        contains_digit = True

if contains_digit == False:
    pass
else:
    print("Oops, we are expecting a properly formatted stock symbol such as 'MSFT'. Please try again.")
    exit()


symbol = user_choice
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)



#data validation part 2 - validate that stock symbol exists
#found an online forum helping explain how to look for a specific value in a dictionary (https://www.educative.io/edpresso/how-to-check-if-a-key-exists-in-a-python-dictionary)
key_to_lookup = 'Error Message'
if key_to_lookup in parsed_response:
  print ("Sorry, we couldn't find any trading data for that symbol. Please try again.")
  exit()
else:
  pass


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
 


if float(latest_close) <= 1.2 * recent_low:
    recommendation = "BUY"
elif float(latest_close) <= 1.7 * recent_low:
    recommendation = "HOLD"
else:
    recommendation = "SELL"

if recommendation == "BUY":
    recommendation_reason = "The stock's latest closing price is less than 20% above its recent low. Therefore, it could be selling at an attractive price."

if recommendation == "HOLD":
    recommendation_reason = "The stock's latest closing price is more than 20% above its recent low but less than 70% above its recent low. Therefore, we recommend holding on for now."

if recommendation == "SELL":
    recommendation_reason = "The stock's latest closing price is more than 70% above its recent low. Therefore, it could be too expensive."


print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print(f"REQUEST AT: {request_time}")
print("-------------------------")
print(f"LATEST DAY: {dates[0]}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {recommendation}")
print(f"RECOMMENDATION REASON: {recommendation_reason}")
print("-------------------------")
print(f"RECOMMENDATION REASON: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
