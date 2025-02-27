import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CountPOS(BaseEstimator, TransformerMixin):
    def __init__(self, pos_tag):
        self.pos_tag = pos_tag

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        pos_counts = []
        for doc in X:
            count = sum(1 for token in doc if token.pos_ == self.pos_tag)
            pos_counts.append(count)
        return pd.DataFrame({self.pos_tag: pos_counts})
