import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal from a sorted list."""
    assert remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_already_unique():
    """Test a list with no duplicates."""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    """Test a list with a single element."""
    assert remove_duplicates([42]) == [42]

def test_remove_duplicates_all_duplicates():
    """Test a list with all duplicate elements."""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_negative_numbers():
    """Test a list with negative numbers."""
    assert remove_duplicates([-3, -3, -2, -1, -1, 0, 0, 1, 1]) == [-3, -2, -1, 0, 1]

def test_remove_duplicates_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_unsorted_list():
    """Test that a ValueError is raised for an unsorted list."""
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        remove_duplicates([3, 1, 4, 2, 5])