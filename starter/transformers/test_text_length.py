import pandas as pd
from text_length import TextLength


def test_text_length():
    # Define a list of text data
    data = [
        "I love Python",
        "Python is the best",
        "Python is the best programming language",
    ]
    # Initialize the transformer
    transformer = TextLength()
    # Transform the data
    data = pd.Series(data)
    result = transformer.fit_transform(data)
    # Define the expected output
    expected = [13, 18, 39]
    # Check the result
    assert list(result[0]) == expected
