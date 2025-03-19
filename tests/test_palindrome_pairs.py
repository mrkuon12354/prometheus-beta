import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pairs scenario."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert set(result) == {(0, 1), (1, 0)}

def test_multiple_palindrome_pairs():
    """Test case with multiple palindrome pairs."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    assert set(result) == {(0, 1), (1, 0), (3, 4), (4, 3)}

def test_empty_list():
    """Test with an empty list of words."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word():
    """Test with a single word in the list."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_no_palindrome_pairs():
    """Test case with no palindrome pairs."""
    words = ["dog", "cat", "bird"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_palindrome_with_empty_string():
    """Test case including empty string."""
    words = ["", "abc", "cba"]
    result = find_palindrome_pairs(words)
    assert set(result) == {(1, 2), (2, 1)}

def test_different_length_words():
    """Test palindrome pairs with words of different lengths."""
    words = ["a", "abc", "aba"]
    result = find_palindrome_pairs(words)
    assert set(result) == {(1, 2), (2, 1)}

def test_repeated_words():
    """Test case with repeated words."""
    words = ["a", "a", "b"]
    result = find_palindrome_pairs(words)
    assert set(result) == {(0, 1), (1, 0)}