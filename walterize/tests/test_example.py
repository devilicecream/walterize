"""
Example test.

"""
import pytest
from walterize import walterize
from walterize.algorithm import walterize_phrase, WalterizeException

WORDS_LIST = [
    ("top", "toppese"),
    ("ops", "oppese"),
    ("devops", "devoppese"),
    ("ciao", "ciaoppese"),
    ("diocane", "diocanese"),
    ("cani", "canippese"),
    ("canapa", "canapappese"),
    ("gas", "gasese"),
]

CLI_ARGS_LIST = [
    ([], WalterizeException),
    (["ciao"], "ciaoppese"),
    (["ciao", "a", "tutti"], "ciaoppese a tuttippese"),
]


@pytest.mark.parametrize("input_word,expected", WORDS_LIST)
def test_words(input_word, expected):
    assert walterize(input_word) == expected


@pytest.mark.parametrize("words,expected", CLI_ARGS_LIST)
def test_phrase(words, expected):
    if callable(expected) and issubclass(expected, Exception):
        with pytest.raises(expected):
            walterize_phrase(words)
    else:
        assert walterize_phrase(words) == expected
