from matplotlib import pyplot as plt
from pandas import read_csv
import pandas as pd
import tkinter as tk

root = tk.Tk()
root.title('Trueplot')
root.geometry('400x400')

#                    DICT NAME          [0]              [1]            [2]         [3]          [4]        [5]
#             'text for drop menus: text for title, variable name, filename.csv, column data, date format, color '
ds = {'Gold AUD': ['Gold AUD', 'GOLD_AUD', 'dsets/GOLD.csv', 'PRICE_AUD', '%d/%m/%y', 'm', 'plot'],\
			'Gold USD' : ['Gold USD', 'GOLD_USD', 'dsets/GOLD.csv', 'PRICE_USD', '%d/%m/%y', 'k'],\
			'Silver AUD': ['Silver AUD', 'SILVER_AUD', 'dsets/SILVER.csv', 'PRICE_AUD', '%d/%m/%y', 'b'],\
			'Silver USD': ['Silver USD', 'SILVER_USD', 'dsets/SILVER.csv', 'PRICE_USD', '%d/%m/%y', 'b'],\
			'Platinum AUD': ['Platinum AUD', 'PLATINUM_AUD', 'dsets/PLATINUM.csv', 'PRICE_AUD', '%d/%m/%y', 'g'],\
			'Platinum USD': ['Platinum USD', 'PLATINUM_USD', 'dsets/PLATINUM.csv', 'PRICE_USD', '%d/%m/%y', 'y'],\
			'Oil, Brent USD': ['Oil, Brent USD', 'OIL_BRENT', 'dsets/OIL.csv', 'BRENT', '%Y-%m-%d', 'r'],\
			'Oil, WTI USD': ['Oil, WTI USD', 'OIL_WTI', 'dsets/OIL.csv', 'WTI', '%Y-%m-%d', 'r'],\
			'S&P 500': ['S&P 500', 'SP500', 'dsets/SP500.csv', 'SP500', '%Y-%m-%d', 'm'],\
			'AUD vs USD': ['AUD vs USD', 'AUDvsUSD', 'dsets/AUDUSD.csv', 'PRICE', '%b %d, %Y', 'k'],\
			'AUS Interest Rate': ['AUS Interest Rate', 'AU_INTEREST', 'dsets/AU_INTEREST.csv', 'RATE', '%Y-%m-%d', 'g'],\
			'Copper USD / Tonne': ['Copper USD / Tonne', 'COPPER','dsets/COPPER.csv', 'PRICE', '%b %Y', 'y'],\
			'All Ords': ['All Ords', 'AO', 'dsets/ALLORDS.csv', 'PRICE', '%b %d, %Y', 'k'],\
			'DOW Jones': ['DOW Jones', 'DOW', 'dsets/DOW.csv', 'PRICE', '%b %d, %Y', 'c'],\
			'Unemployment % AUS': ['Unemployment % AUS', 'UNEM_AUS', 'dsets/UNEMP_AUS.csv', 'RATE', '%Y-%m-%d', 'g'],
			'Unemployment % USA': ['Unemployment % USA', 'UNEM_USA', 'dsets/UNEMP_USA.csv', 'RATE', '%Y', 'r'],\
			'Solar Flares - X Class': ['Solar Flares - X Class', 'FLARES', 'dsets/X_CLASS_FLARE.csv', 'CLASS', '%Y-%m-%d', 'r', 'scatter']}

dslist = list(ds.keys())															#SET DROP LIST FROM DICT(ds) KEYS

def go():
	y1data = y1button.get()
	y2data = y2button.get()

	fig, ax1 = plt.subplots()														#SET AS DUAL Y AXIS, SHARING COMMON X AXIS
	ax2 = ax1.twinx()

	for axis, ydata in zip([ax1, ax2], [y1data, y2data]):
		print(axis, ydata)
		axis = axis +'.'
		ds[ydata][1] = read_csv(ds[ydata][2], usecols = ['DATE', ds[ydata][3]])
		ds[ydata][1] = ds[ydata][1].fillna(method = 'ffill')
		ds[ydata][1]['DATE'] = pd.to_datetime(ds[ydata][1].DATE, format = ds[ydata][4])
		axis.set_ylabel(ds[ydata][0])
		axis.eval(ds[ydata][6])(ds[ydata][1]['DATE'], ds[ydata][1][ds[ydata][3]], label = ds[ydata][0], color = ds[ydata][5])

	ax1.legend(loc = 1)
	#plt.ylim(1,1)																#SET LEGENDS TO TOP L & R CORNER
	ax2.legend(loc = 2)
	plt.title(ds[y1data][0] + ' / ' + ds[y2data][0])								#SET TITLE USING DICTIONARY
	fig.tight_layout()
	ax1.grid()

	mng = plt.get_current_fig_manager()												#SET FIGURE TO FULLSCREEN
	mng.full_screen_toggle()
	plt.show()



y1button = tk.StringVar(root)														#SET PLOT 1 FROM LIST
y1button.set(dslist[0])
y1buttondrop = tk.OptionMenu(root, y1button, *dslist)
y1buttondrop.pack(expand = True, fill = 'both')

y2button = tk.StringVar(root)														#SET PLOT 2 FROM LIST
y2button.set(dslist[2])
y2buttondrop = tk.OptionMenu(root, y2button, *dslist)
y2buttondrop.pack(expand = True, fill = 'both')


go_button = tk.Button(root, text = 'Plot chart', command = go)						#PLOT CHART FUNCTION
go_button.pack(expand = True, fill = 'both')





root.mainloop()
