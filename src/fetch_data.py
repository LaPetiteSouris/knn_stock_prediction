import datetime as date
import pandas.io.data as web


def load_yahoo_finance_data():
    ''' This function load Finance data about ABB stock
    from Yahoo Finance API, then return trainng features, target label
    and training result.
    :return: training feature, traing result, target label for prediction
    '''
    feature = []
    cls_point_arr = []
    target_label = []
    start = date.datetime(2000, 1, 1)
    last_date = date.datetime(2016, 1, 28)
    result = web.DataReader('ABBN.VX', 'yahoo', start, last_date)
    # Adj closing point of the index
    cls_point = result.loc[:, ['Close']]
    open_point = result.loc[:, ['Open']]
    high_point = result.loc[:, ['High']]
    low_point = result.loc[:, ['Low']]
    vol = result.loc[:, ['Volume']]
    # Traing features are Open value, High value, Low value and
    # Sold volume of the stock of the previous day.
    # This is used to predict close value of the upcoming day.
    for i in range((len(cls_point.index) - 1)):
        feature.append([open_point.iloc[i].values[0],
                        high_point.iloc[i].values[0],
                        low_point.iloc[i].values[0],
                        vol.iloc[i].values[0]]
                       )
    for i in range(len(cls_point.index)):
        cls_point_arr.append(cls_point.iloc[i].values[0])
    close_point_shifted_right = [cls_point_arr[i]
                                 for i in range(1, len(cls_point_arr))]
    j = len(cls_point.index)-1
    target_label.append([open_point.iloc[j].values[0],
                         high_point.iloc[j].values[0],
                         low_point.iloc[j].values[0],
                         vol.iloc[j].values[0]]
                        )
    return feature, close_point_shifted_right, target_label


def load_raw_yahoo_finance_data():
    feature = []
    #current_date = date.datetime.now().date()
    start = date.datetime(2016, 1, 25)
    current_date = date.datetime(2016, 1, 28)
    result = web.DataReader('ABBN.VX', 'yahoo', start, current_date)
    # Adj closing point of the index
    cls_point = result.loc[:, ['Close']]
    open_point = result.loc[:, ['Open']]
    high_point = result.loc[:, ['High']]
    low_point = result.loc[:, ['Low']]
    vol = result.loc[:, ['Volume']]
    return cls_point, open_point, high_point, low_point, vol
