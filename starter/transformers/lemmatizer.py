import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class Lemmatizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.Series(" ".join([token.lemma_ for token in doc]) for doc in X)
