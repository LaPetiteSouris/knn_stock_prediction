import fetch_data as fetcher
from sklearn.neighbors import KNeighborsRegressor


class predictor:
    def __init__(self):
        self.feature = [[]]
        self.result = []

    def predict(self):
        feature, result = fetcher.load_yahoo_finance_data()
        self.feature = feature
        self.result = result
        knnregressor = KNeighborsRegressor(n_neighbors=5, weights='distance',
                                           algorithm='kd_tree')
        val = 0
        if feature and result is not None:

            knnregressor.fit(self.feature, self.result)
            data = [16.95, 17.36, 16.84, 2573400]
            data2 = [16.38, 16.99, 16.84, 2242100]
            val = knnregressor.predict(data)
        return val
