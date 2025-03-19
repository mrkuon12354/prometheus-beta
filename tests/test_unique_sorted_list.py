import pytest
from src.unique_sorted_list import get_unique_sorted_integers

def test_unique_sorted_list_basic():
    """Test basic functionality with a list of integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6, 9]
    assert get_unique_sorted_integers(input_list) == expected

def test_unique_sorted_list_already_sorted():
    """Test with an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert get_unique_sorted_integers(input_list) == [1, 2, 3, 4, 5]

def test_unique_sorted_list_empty():
    """Test with an empty list"""
    assert get_unique_sorted_integers([]) == []

def test_unique_sorted_list_negative_numbers():
    """Test with negative numbers and zero"""
    input_list = [-3, -1, 0, -1, 3, 0, 1]
    expected = [-3, -1, 0, 1, 3]
    assert get_unique_sorted_integers(input_list) == expected

def test_unique_sorted_list_invalid_input_not_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers("not a list")

def test_unique_sorted_list_invalid_input_non_integers():
    """Test raising TypeError for list with non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])