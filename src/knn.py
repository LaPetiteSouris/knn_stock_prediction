import fetch_data as fetcher
from sklearn.neighbors import KNeighborsRegressor


class predictor:
    def __init__(self):
        self.feature = [[]]
        self.result = []
        self.target_label = []

    def predict(self):
        feature, result, target_label = fetcher.load_yahoo_finance_data()
        self.feature = feature
        self.target_label = target_label
        self.result = result
        knnregressor = KNeighborsRegressor(n_neighbors=5, weights='uniform',
                                           algorithm='brute')
        val = 0
        if feature and result is not None:

            knnregressor.fit(self.feature, self.result)
            val = knnregressor.predict(target_label)
        return val[0]
