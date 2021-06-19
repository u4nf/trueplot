from matplotlib import pyplot as plt
from pandas import read_csv
import pandas as pd

gold_raw = read_csv('goldc.csv', usecols = ['DATE', 'PRICE'])
silver_raw = read_csv('silverc.csv', usecols = ['DATE', 'PRICE'])
platinum_raw = read_csv('platinumc.csv', usecols = ['DATE', 'PRICE'])

gold_raw = gold_raw.fillna(method = 'ffill')
silver_raw = silver_raw.fillna(method = 'ffill')
platinum_raw = platinum_raw.fillna(method = 'ffill')

#silver_raw = silver_raw.fillna(axis = 0, how = 'any')
#platinum_raw = platinum_raw.fillna(axis = 0, how = 'any')


gold_raw['DATE'] = pd.to_datetime(gold_raw.DATE, format = '%d/%m/%y')
silver_raw['DATE'] = pd.to_datetime(silver_raw.DATE, format = '%d/%m/%y')
platinum_raw['DATE'] = pd.to_datetime(platinum_raw.DATE, format = '%d/%m/%y')


#date = gld_raw['DATE'].to_list()
#g = gld_raw['PRICE'].to_list()
#s = silver_raw['PRICE'].to_list()
#p = platinum_raw['PRICE'].to_list()



#g_dict = dict(zip(date, g))
#s_dict = dict(zip(date, s))
#p_dict = dict(zip(date, p))

plt.plot(gold_raw['DATE'], gold_raw['PRICE'], label = 'Gold', color = 'k')
plt.plot(platinum_raw['DATE'], platinum_raw['PRICE'], label = 'Platinum', color = 'g')
#plt.plot(date, s, label = 'Silver', color = 'g')
#plt.plot(date, p, label = 'Platinum', color = 'k')
plt.legend()
plt.show()