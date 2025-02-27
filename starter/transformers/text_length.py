import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class TextLength(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.DataFrame(X.str.len())
