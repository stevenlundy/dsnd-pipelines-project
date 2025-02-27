import pandas as pd
from word_count import WordCount


def test_count_words():
    # Define a list of text data
    data = [
        "I love Python",
        "Python is the best",
        "Python is the best programming language",
    ]
    # Initialize the transformer
    transformer = WordCount()
    # Transform the data
    data = pd.Series(data)
    result = transformer.fit_transform(data)
    # Define the expected output
    expected = [3, 4, 6]
    # Check the result
    assert list(result[0]) == expected
