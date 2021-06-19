from matplotlib import pyplot as plt

title_x = 'Day of the week'
title_y = 'Revenue'

colors = ['k','r','b','g','m','y','w']  #can use hex eg - #9b8c5f  (rrggbb)
#print(plt.style.available)					#shows available styles (not executable)
#plt.style.use('fivethirtyeight')			#change style of whole graph


title = '{} vs {}'.format(title_x, title_y)

coles_revenue = [100,300,200,500,800,0,0]
days = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun']

woolies_revenue = [800,600,200,750,900,100,0]
plt.plot(days, coles_revenue, label = 'Coles', color = colors[3], marker ='.', linewidth = 4)

plt.plot(days, woolies_revenue, label = 'Woolies', color = colors[1], marker ='.', linestyle = '--')

plt.title(title)
plt.xlabel(title_x)
plt.ylabel(title_y)
#plt.legend(['Coles', 'Woolies'])			#label = xxx is better
plt.legend()								#enable legend
plt.grid(True)								#enable grid
#plt.tight_layout()  						#adjust padding
#plt.savefig('filename.png')				#save as png
plt.show()