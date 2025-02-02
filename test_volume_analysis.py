
# Tesco Share Price Analysis Script
# This script downloads and analyzes Tesco PLC (TSCO.L) share price data using yfinance.
# It calculates various statistical measures and creates a volume histogram with key metrics.

# Required packages:
# - numpy
# - scipy
# - pandas
# - yfinance
# - matplotlib


import numpy as np
from scipy import stats
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats.mstats import gmean

ticker = 'TSCO.L'
data = yf.download(ticker, start="2024-01-01", end="2025-01-01")
print(data.info()) # Shows data types, non-null counts, etc.
print(data.describe()) # Provides summary statistics(this shows the mean, std, etc.) but for the purpose of this we will be calculting ourselves

## print the first five rows of the data
print("\nFirst 5 rows of data:")
print(data.head())


## closing price data
closing_price_mean = np.average(data['Close'])
closing_price_mode = stats.mode(data['Close'])
closing_price_median = np.median(data['Close'])
closing_price_variance = np.var(data['Close'].values, ddof=1)
closing_prices = data['Close'].dropna() # removes any missing values
closing_price_standard_deviation = closing_prices.std()
max = np.max(data['Close'])

volume_mean = np.average(data['Volume'])
volume_median = np.median(data['Volume'])
volume_standard_deviation = data['Volume'].std()
volume_25th = np.percentile(data['Volume'], 25)
volume_75th = np.percentile(data['Volume'], 75)
volume_90th = np.percentile(data['Volume'], 90)

##the geometric mean of the volume has to be calculated of instances where trading data isnt 0

volumes = data['Volume'][data['Volume'] > 0]
volume_geometric_mean = gmean(volumes).item()

## print the results of the analysis

print("\nStatistical Analysis of "+ str(ticker) + ":")
print(f"Closing Price Statistics:")
print(f"Average: £{closing_price_mean:.2f}")
print(f"Median: £{closing_price_median:.2f}")
print(f"Mode: £{closing_price_mode.mode[0]:.2f}")
print(f"Variance: £{closing_price_variance:.2f}")
print(f"Standard Deviation: £{closing_price_standard_deviation}")
print(f"Maximum: £{max:.2f}")

print(f"\nVolume Statistics")
print(f"Arithmetic Mean: {volume_mean:,.0f}")
print(f"Geometric Mean: {volume_geometric_mean:,.0f}")
print(f"Median: {volume_median:,.0f}")
print(f"Standard Deviation: {volume_standard_deviation}")
print(f"25th Percentile: {volume_25th:,.0f}")
print(f"75th Percentile: {volume_75th:,.0f}")
print(f"90th Percentile: {volume_90th:,.0f}")

## output is a histogram on the volume of the tesco share price with the mean and median plotted this year

plt.hist(data['Volume'], bins=20, edgecolor='black')
plt.axvline(volume_mean, color='r', linestyle='dashed', linewidth=2, label='mean')
plt.axvline(volume_median, color='y', linestyle='dashed', linewidth=2, label='median',)
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.legend()
plt.title('volume distribution of ' +str(ticker) + ' 2024')
plt.show()





