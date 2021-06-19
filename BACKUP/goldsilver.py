from matplotlib import pyplot as plt
from pandas import read_csv
import pandas as pd

gld_raw = read_csv('goldc.csv', usecols = ['DATE', 'PRICE'])
silver_raw = read_csv('silverc.csv', usecols = ['PRICE'])
platinum_raw = read_csv('platinumc.csv', usecols = ['PRICE'])

gld_raw['DATE'] = pd.to_datetime(gld_raw['DATE'])


gold = {}
#date = gld_raw['DATE'].to_list()
#g = gld_raw['PRICE'].to_list()
s = silver_raw['PRICE'].to_list()
p = platinum_raw['PRICE'].to_list()



g_dict = dict(zip(date, g))
s_dict = dict(zip(date, s))
p_dict = dict(zip(date, p))


plt.plot(date, g, label = 'Gold', color = 'y')
plt.plot(date, s, label = 'Silver', color = 'g')
plt.plot(date, p, label = 'Platinum', color = 'k')
plt.legend()
plt.show()