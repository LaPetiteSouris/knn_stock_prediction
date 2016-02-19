import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# make up some data
dates = ['8-2-2016', '9-2-2016', '10-2-2016', '11-2-2016', '12-2-2016',
         '15-2-2016', '16-2-2016', '17-2-2016', '18-2-2016', '19-2-2016']
x = [datetime.datetime.strptime(d, '%d-%m-%Y').date() for d in dates]
y = [20.448, 20.8205, 19.514, 21.099, 19.686, 19.8525,
     20.5625, 19.3475, 19.3475, 19.0585]
y_real = [16.89, 16.49, 16.69, 16.17,
          16.51, 17.09, 17.19, 17.75, 17.79, 17.73]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x, y, '-o', label=' predited close value of ABBN.VX ')
plt.plot(x, y_real, '-o', color='red',
         label=' historic close value of ABBN.VX ')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
