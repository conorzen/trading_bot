import numpy as np
from scipy import stats
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# the purpose of this is to test my understanding of analysis of the tesco share price using python

ticker = 'TSCO.L'
df = yf.download(ticker, start="2024-01-01", end="2025-01-01")

print(df.head())

data = df.T

print(data.head())

# for i in range(len(df)):
#     month = df.loc[df["Date"] == i]["Close"]
#     print("the close price of " + str(i) + " is " + str("close"))

# # closing price data
closing_price_mean = np.average(df['Close'])
closing_price_mode = stats.mode(df['Close'])
closing_price_median = np.median(df['Close'])
closing_price_variance = np.var(df['Close'])
closing_price_standard_deviation = np.std(df['Close'])
max = np.max(df['Close'])

volume_mean = np.average(df['Volume'])
volume_median = np.median(df['Volume'])
volume_standard_deviation = np.std(df['Volume'])

print("this is the closing price average " +str(round(closing_price_mean,2)))
print("this is the closing price median " +str(round(closing_price_median,2)))
print("this is the closing price mode " +str(closing_price_mode))
print("the variance of the ' +str(ticker) + ' share price is " +str(closing_price_variance))
print("the max of the " +str(ticker) + " share price is " +str(round(max,2)))
print("the standard deviation of the " +str(ticker) + " share price is " +str(round(closing_price_standard_deviation,2)))

plt.hist(df['Volume'], bins=20, edgecolor='black')
plt.axvline(volume_mean, color='r', linestyle='dashed', linewidth=2, label='mean')
plt.axvline(volume_median, color='y', linestyle='dashed', linewidth=2, label='median',)
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.legend()
plt.title('Histogram of ' +str(ticker) + ' Volume 2024')
plt.show()





