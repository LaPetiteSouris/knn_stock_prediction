import fetch_data as fetcher
from sklearn.neighbors import KNeighborsRegressor


class predictor:
    def __init__(self):
        self.feature = [[]]
        self.result = []

    def predict(self, target):
        feature, result = fetcher.load_yahoo_finance_data()
        self.feature = feature
        self.result = result
        knnregressor = KNeighborsRegressor(n_neighbors=5, weights='uniform',
                                           algorithm='brute')
        val = 0
        if feature and result is not None:

            knnregressor.fit(self.feature, self.result)
            val = knnregressor.predict(target)
        return val

p = predictor()
data0 = [16.830, 16.83, 16.56, 1685700]
data1 = [16.38, 16.99, 16.84, 2242100]
data2 = [16.95, 17.36, 16.84, 2573400]
data3 = [17.315, 17.51, 17.09, 2574800]
p_26 = p.predict(data0)
p_27 = p.predict(data1)
p_28 = p.predict(data2)
print 'predicted value 26/1 is %s' % p_26[0]
print 'predicted value 27/1 is %s' % p_27[0]
print 'predicted value 28/1 is %s' % p_28[0]
