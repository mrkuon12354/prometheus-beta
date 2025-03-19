import pytest
from src.string_utils import remove_char_length

def test_remove_char_length_basic():
    """Test basic functionality of removing a character and getting length."""
    assert remove_char_length("hello", "l") == 3

def test_remove_char_length_no_match():
    """Test removing a character that doesn't exist in the string."""
    assert remove_char_length("hello", "x") == 5

def test_remove_char_length_empty_string():
    """Test with an empty input string."""
    assert remove_char_length("", "a") == 0

def test_remove_char_length_all_chars_removed():
    """Test when all characters are removed."""
    assert remove_char_length("aaaa", "a") == 0

def test_remove_char_length_invalid_string_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input string must be a string"):
        remove_char_length(123, "a")

def test_remove_char_length_invalid_char_type():
    """Test raising TypeError for non-string character."""
    with pytest.raises(TypeError, match="Character to remove must be a string"):
        remove_char_length("hello", 1)

def test_remove_char_length_invalid_char_length():
    """Test raising ValueError for multi-character input."""
    with pytest.raises(ValueError, match="Character to remove must be a single character"):
        remove_char_length("hello", "ab")