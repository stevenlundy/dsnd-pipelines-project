import pandas as pd
from character_freq import CharacterFrequency


def test_character_freq():
    # Define a list of text data
    data = [
        "I love Python",
        "Python is the best",
        "Python is the best programming language",
    ]
    # Initialize the transformer
    transformer = CharacterFrequency("e")
    # Transform the data
    data = pd.Series(data)
    result = transformer.fit_transform(data)
    # Define the expected output
    expected = [1, 2, 3]
    assert list(result[0]) == expected
