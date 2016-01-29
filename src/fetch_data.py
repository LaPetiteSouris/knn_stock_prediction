import datetime as date
import pandas.io.data as web


def load_yahoo_finance_data():
    feature = []
    #current_date = date.datetime.now().date()
    start = date.datetime(2000, 1, 1)
    current_date = date.datetime(2016, 1, 25)
    result = web.DataReader('ABBN.VX', 'yahoo', start, current_date)
    # Adj closing point of the index
    cls_point = result.loc[:, ['Close']]
    open_point = result.loc[:, ['Open']]
    high_point = result.loc[:, ['High']]
    low_point = result.loc[:, ['Low']]
    vol = result.loc[:, ['Volume']]
    for i in range(len(cls_point.index)):
        feature.append([open_point.iloc[i].values[0],
                        high_point.iloc[i].values[0],
                        low_point.iloc[i].values[0],
                        vol.iloc[i].values[0]]
                       )
    return feature, cls_point


def load_raw_yahoo_finance_data():
    feature = []
    #current_date = date.datetime.now().date()
    start = date.datetime(2016, 1, 26)
    current_date = date.datetime(2016, 1, 27)
    result = web.DataReader('ABBN.VX', 'yahoo', start, current_date)
    # Adj closing point of the index
    cls_point = result.loc[:, ['Close']]
    open_point = result.loc[:, ['Open']]
    high_point = result.loc[:, ['High']]
    low_point = result.loc[:, ['Low']]
    vol = result.loc[:, ['Volume']]
    return cls_point, open_point, high_point, low_point, vol
