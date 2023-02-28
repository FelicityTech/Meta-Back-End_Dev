# test_string_methods.py

# Import the string methods to be tested
from string_methods import word_count, char_count, first_char, last_char

# Test the word_count function
def test_word_count():
    assert word_count("The quick brown fox jumps over the lazy dog.") == 9
    assert word_count("Hello, world!") == 2
    assert word_count("") == 0

# Test the char_count function
def test_char_count():
    assert char_count("The quick brown fox jumps over the lazy dog.") == 43
    assert char_count("Hello, world!") == 13
    assert char_count("") == 0

# Test the first_char function
def test_first_char():
    assert first_char("The quick brown fox jumps over the lazy dog.") == "T"
    assert first_char("Hello, world!") == "H"
    assert first_char("") == ""

# Test the last_char function
def test_last_char():
    assert last_char("The quick brown fox jumps over the lazy dog.") == "."
    assert last_char("Hello, world!") == "!"
    assert last_char("") == ""
