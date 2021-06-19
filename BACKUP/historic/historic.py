from matplotlib import pyplot as plt
from pandas import read_csv
import pandas as pd


gold_raw = read_csv('gold.csv', usecols = ['DATE', 'PRICE_AUD', 'PRICE_USD'])
sp500 = read_csv('sp-500_1975.csv', usecols = ['Date', 'SP500'])
oil = read_csv('oil.csv', usecols = ['Date', 'Brent', 'WTI'])
silver = read_csv('silver.csv', usecols = ['DATE', 'PRICE_USD', 'PRICE_AUD'])
platinum = read_csv('platinum.csv', usecols = ['DATE', 'PRICE_AUD', 'PRICE_USD'])
unemployed = read_csv('usa_unemployment.csv', usecols = ['Date', 'unemployed'])
earthquake = read_csv('earthquake7p5plus.csv', usecols = ['Date', 'Magnitude', 'Ones'])
lunar = read_csv('total_lunar.csv', usecols = ['Date', 'Ones'])

gold_raw = gold_raw.fillna(method = 'ffill')
sp500 = sp500.fillna(method = 'ffill')
oil = oil.fillna(method = 'ffill')
silver = silver.fillna(method = 'ffill')
platinum = platinum.fillna(method = 'ffill')
#silver_raw = silver_raw.fillna(axis = 0, how = 'any')
#platinum_raw = platinum_raw.fillna(axis = 0, how = 'any')


unemployed['Date'] = pd.to_datetime\
									(unemployed.Date, format = '%Y')
gold_raw['DATE'] = pd.to_datetime(gold_raw.DATE, format = '%d/%m/%y')
sp500['Date'] = pd.to_datetime(sp500.Date, format = '%Y-%m-%d')
oil['Date'] = pd.to_datetime(oil.Date, format = '%Y-%m-%d')
silver['DATE'] = pd.to_datetime(silver.DATE, format = '%d/%m/%y')
platinum['DATE'] = pd.to_datetime(platinum.DATE, format = '%d/%m/%y')
earthquake['Date'] = pd.to_datetime(earthquake.Date, format = '%m/%d/%Y')
lunar['Date'] = pd.to_datetime(lunar.Date, format = '%Y %B %d')





fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.scatter(earthquake['Date'], earthquake['Ones'], label = 'Earthquakes > 5.5', color = 'g')
# ax2.plot(oil['Date'], oil['Brent'], label = 'Brent Crude Oil', color = 'k')
# ax1.plot(oil['Date'], oil['WTI'], label = 'WTI', color = 'r')
# ax1.plot(unemployed['Date'], unemployed['unemployed'], label = 'USA unemployment %')
ax2.plot(silver['DATE'], silver['PRICE_USD'], label = 'Silver USD', color = 'b')
# ax1.plot(platinum['DATE'], platinum['PRICE_USD'], label = 'Platinum USD', color = 'y')
# ax2.plot(gold_raw['DATE'], gold_raw['PRICE_AUD'], label = 'Gold AUD')
# ax2.plot(gold_raw['DATE'], gold_raw['PRICE_USD'], label = 'Gold USD')
#ax2.plot(sp500['Date'], sp500['SP500'], label = 'SP500')
#ax2.scatter(lunar['Date'], lunar['Ones'], label = 'Total Lunar Eclispse', color = 'r')

#plt.legend()
ax1.legend(loc = 0)
ax2.legend(loc = 2)
fig.tight_layout()
plt.show()