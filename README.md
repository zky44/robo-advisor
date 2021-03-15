# robo-advisor application

Thanks for checking out this awesome robo-advisor! Read the steps below to learn how to set up your local environment so that you can use it to get stock trading data and recommendations.

## Prerequisites

+ Anaconda 3.7+
+ Python 3.7+
+ Pip

## Installation

Fork this [remote repository](https://github.com/zky44/robo-advisor) under your own control, then clone your remote copy onto your local computer.

Next, navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd robo-advisor
```

If you haven't done so yet, use anaconda to create and activate a new virtual environment. A suggestion would be to call it "stocks-env":

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```

From inside the virtual environment, install package dependicies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws you an error, make sure you are running it from the repository's root directory where the requirements.txt file exists. Refer back to the initial `cd` step above

## Getting Your Custom API Key

Visit [Alpha Vantage](https://www.alphavantage.co/) to retreive your custom API Key. Click "GET YOUR FREE API KEY TODAY" and fill in your information. Once you get your key, you'll want to store the API Key value in an [environment variable](https://github.com/zky44/intro-to-python/blob/master/notes/environment-variables.md) called `ALPHAVANTAGE_API_KEY`

```sh

ALPHAVANTAGE_API_KEY = "abc123"
```

>IMPORTANT: the ".env" file is usally the place for passing configuration options and secret credentials, so as a best practrice we don't upload this file to version control. Make sure that you add the code in this [.gitignore](/.gitignore) file, most importantly line 2, to your ".gitignore" file.

## Using the Robo-Advisor

From inside the virtual environment, run the code using the command below:

```sh
python app/robo_advisor.py
```

Type in a stock symbol that you would like to analyze and you will be presented with an output showing you the latest closing price as well as the most recent high and low prices of the past 100 days.

You will also be presented with a "BUY", "HOLD", or "SELL" recommendation and rationale. The current rules are written below, but can be modified anytime in the robo_advisor.py file.

+ "BUY" - The stock's latest closing price is less than 20% above its recent low. It may have just sold-off and would be a good time to get back in!
+ "HOLD" - The stock's latest closing price is more than 20% above its recent low but less than 70% above its recent low. It is best to stay neutral!
+ "SELL" - The stock's latest closing price is more than 70% above its recent low. It may have spiked in the past 100 days and could be overvalued!

Finally, the system will write all historical stock prices of the past 100 days to the "prices.csv" file located in the repository's "data" directory, which you can access using the file path shown.

Making a change at the end.