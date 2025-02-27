import re

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CharacterFrequency(BaseEstimator, TransformerMixin):
    def __init__(self, char):
        self.char = char

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.DataFrame(X.apply(lambda x: len(re.findall(re.escape(self.char), x))))
