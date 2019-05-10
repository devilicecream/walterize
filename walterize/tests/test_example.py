"""
Example test.

"""
import pytest
from walterize import walterize

WORDS_LIST = [
    ("top", "toppese"),
    ("ops", "oppese"),
    ("devops", "devoppese"),
    ("ciao", "ciaoppese"),
    ("diocane", "diocanese"),
    ("cani", "canippese"),
    ("canapa", "canapappese"),
    ("gas", "gaseppese"),
]


@pytest.mark.parametrize("input_word,expected", WORDS_LIST)
def test_words(input_word, expected):
    assert walterize(input_word) == expected
