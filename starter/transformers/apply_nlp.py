from sklearn.base import BaseEstimator, TransformerMixin


class ApplyNLP(BaseEstimator, TransformerMixin):
    def __init__(self, nlp):
        self.nlp = nlp
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return list(self.nlp.pipe(X))
