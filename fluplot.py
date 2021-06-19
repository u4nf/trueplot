from matplotlib import pyplot as plt
from pandas import read_csv
import pandas as pd
import tkinter as tk

root = tk.Tk()
root.title('Fluplot')
root.geometry('400x400')

#                    DICT NAME          [0]              [1]            [2]         [3]          [4]        [5]
#             'text for drop menus: text for title, variable name, filename.csv, column data, date format, color '
ds = {'Gold AUD': ['Gold AUD', 'GOLD_AUD', 'dsets/GOLD.csv', 'PRICE_AUD', '%d/%m/%y', 'm', 'plot']}		

#SET DROP LIST FROM DICT(ds) KEYS
dslist = list(ds.keys())

def go():
	y1data = y1button.get()
	y2data = y2button.get()

	fig, ax1 = plt.subplots()														#SET AS DUAL Y AXIS, SHARING COMMON X AXIS
	ax2 = ax1.twinx()

	for axis, ydata in zip([ax1, ax2], [y1data, y2data]):
		print(axis, ydata)
		ds[ydata][1] = read_csv(ds[ydata][2], usecols = ['DATE', ds[ydata][3]])
		ds[ydata][1] = ds[ydata][1].fillna(method = 'ffill')
		ds[ydata][1]['DATE'] = pd.to_datetime(ds[ydata][1].DATE, format = ds[ydata][4])
		axis.set_ylabel(ds[ydata][0])
		axis.plot(ds[ydata][1]['DATE'], ds[ydata][1][ds[ydata][3]], label = ds[ydata][0], color = ds[ydata][5])

	ax1.legend(loc = 1)																#SET LEGENDS TO TOP L & R CORNER
	ax2.legend(loc = 2)
	plt.title(ds[y1data][0] + ' / ' + ds[y2data][0])								#SET TITLE USING DICTIONARY
	fig.tight_layout()
	ax1.grid()

	mng = plt.get_current_fig_manager()												#SET FIGURE TO FULLSCREEN
	mng.full_screen_toggle()
	plt.show()

go()




root.mainloop()
