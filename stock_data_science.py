import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

last_year = datetime.datetime.now().year - 1
start_date = datetime.datetime.now().replace(year = last_year)
end_date = datetime.datetime.now()

data_frame = web.DataReader(name = 'AMZN', data_source='yahoo', start = start_date, end = end_date)

print(data_frame)

df.to_csv("~/Documents/{}.csv".format(symbol))

close = df[['close']]

close = close.rename(columns={'close': symbol})
ax = close.plot(title = 'Amazon')
ax.set_xlabel('date')
ax.set_ylabel('close price')
ax.grid()
plt.show()

