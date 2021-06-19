import requests
import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
import shrimpy
import plotly
import plotly.graph_objects as go
from plotly.offline import plot, iplot, download_plotlyjs
from matplotlib import pyplot as plt

#iplot([{'x':[1,2,3,4,5,6,7,8], 'y':[4,2,8,5,3,5,8,9]}])
shrimpy_pub = 'b49812d3c2ef8f1f3a6fe9e6add25d8272ec291c983242e74c2eec90403d2193'
shrimpy_pri = '97baf2e78b9398d1d450660c3130cfbdea8f6f628c924d46b0aa92913dc8dd3e78333ec611c5821508a6d33269484dbd41ad7b1f472f19922875a4e4bbefbe8a'

client = shrimpy.ShrimpyApiClient(shrimpy_pub, shrimpy_pri)

candles = client.get_candles('binance', 'BTC', 'USDT', '1d')
candles1 = client.get_candles('binance', 'XRP', 'USDT', '1d')
candles2 = client.get_candles('binance', 'XLM', 'USDT', '1d')

dates = []
open_data = []
high_data = []
low_data = []
close_data = []

dates1 = []
dates2 = []
close_data1 = []
close_data2 = []

for candle in candles:
	dates.append(candle['time'])
	open_data.append(candle['open'])
	high_data.append(candle['high'])
	low_data.append(candle['low'])
	close_data.append(candle['close'])

for candle in candles1:
	dates1.append(candle['time'])
	close_data1.append(candle['close'])

for candle in candles2:
	dates2.append(candle['time'])
	close_data2.append(candle['close'])

#fig = go.Figure()
#fig.add_trace(go.Scatter(x=dates1, y=close_data1))
#fig.add_trace(go.Scatter(x=dates2, y=close_data2))

#fig.show()

tt = [1,2,3,4,5,6,7,8,9,10]
ttt = [9,5,8,3,9,4,8,8,3,9]


plt.plot(tt, ttt)
plt.show()





btcaud = 'https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=xbt&secondaryCurrencyCode=aud'
btcusd = 'https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd'
ethaud = 'https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=eth&secondaryCurrencyCode=aud'
xrpaud = 'https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=xrp&secondaryCurrencyCode=aud'
xlmaud = 'https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=xlm&secondaryCurrencyCode=aud'
ltcaud = 'https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=ltc&secondaryCurrencyCode=aud'


def get_btcaud():
	price_btcaud = requests.get(btcaud)
	return float(price_btcaud.json()['LastPrice'])

def get_btcusd():
	price_btcusd = requests.get(btcusd)
	return float(price_btcusd.json()['LastPrice'])

def get_ethaud():
	price_ethaud = requests.get(ethaud)
	return float(price_ethaud.json()['LastPrice'])

def get_xrpaud():
	price_xrpaud = requests.get(xrpaud)
	return float(price_xrpaud.json()['LastPrice'])

def get_xlmaud():
	price_xlmaud = requests.get(xlmaud)
	return float(price_xlmaud.json()['LastPrice'])

def get_ltcaud():
	price_ltcaud = requests.get(ltcaud)
	return float(price_ltcaud.json()['LastPrice'])

font = 'dragonlands, 30'

root = tk.Tk()

class ApplyCrypto:
	def __init__(self, master, img, ticker, y):
		self.openimg = p.Image.open('media/{}'.format(img)).resize((150,150))
		self.img = ptk.PhotoImage(self.openimg)
		self.crypto_label = tk.Label(master, image = self.img)
		self.crypto_label.image = self.img
		self.crypto_label.grid(row = y, column = 0)

	def apply_all():
		ApplyCrypto.apply_btcaud()
		ApplyCrypto.apply_ethaud()
		ApplyCrypto.apply_ltcaud()
		ApplyCrypto.apply_xrpaud()
		ApplyCrypto.apply_xlmaud()

	def apply_btcaud():
		global btcaud_label
		btcaud_label = ApplyCrypto(root, 'btc.jpg', btcaud, 1)
	def apply_ethaud():
		global ethaud_label
		ethaud_label = ApplyCrypto(root, 'eth.jpg', ethaud, 2)
	def apply_ltcaud():
		global ltcaud_label
		ltcaud_label = ApplyCrypto(root, 'ltc.jpg', ltcaud, 3)
	def apply_xrpaud():
		global xrpaud_label
		xrpaud_label = ApplyCrypto(root, 'xrp.jpg', xrpaud, 4)
	def apply_xlmaud():
		global xlmaud_label
		xlmaud_label = ApplyCrypto(root, 'xlm.jpg', xlmaud, 5)

	def update():
		btcaud_label.crypto_label.configure(text = get_btcaud(), font = font, compound = tk.CENTER, fg = 'red')
		ethaud_label.crypto_label.configure(text = get_ethaud(), font = font, compound = tk.CENTER, fg = 'red')
		xrpaud_label.crypto_label.configure(text = get_xrpaud(), font = font, compound = tk.CENTER, fg = 'red')
		xlmaud_label.crypto_label.configure(text = get_xlmaud(), font = font, compound = tk.CENTER, fg = 'red')
		ltcaud_label.crypto_label.configure(text = get_ltcaud(), font = font, compound = tk.CENTER, fg = 'red')
	
ApplyCrypto.apply_all()
ApplyCrypto.update()

#root.bind('<KP_Enter>', ApplyCrypto.apply_all())											#numpad enter to submit answer


root.mainloop()