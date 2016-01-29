__author__ = 'tung'

from fetch_data import data
from arma_model import ARMA
import datetime as date
import matplotlib.pyplot as plt
import statsmodels.api as sm


# first, loading historical index point from Yahoo Finance
data_loader = data()
current_date = date.datetime.now().date()
data = data_loader.load_yahoo_finance_data(current_date)
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)

array_data_without_index = data_loader.convert_data_to_array(data)
data.plot(ax=ax1, title='EURONEXT 100')


# Start Modelling Process
arma_modeling_helper = ARMA(array_data_without_index)
arma_model = arma_modeling_helper.start_modeling()
resid = arma_model.resid
ax2=fig.add_subplot(212)
sm.qqplot(resid, line='q',ax=ax2, fit='True')


# Prediction
predicted_stock = arma_modeling_helper.prediction(arma_model)
print predicted_stock
plt.figure()
ax=plt.plot(predicted_stock)
plt.xlabel('Days')
plt.title('Predicted Closing Price of EURONEXT 100 in next 5 business day')
plt.grid()
plt.show()
