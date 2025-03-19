import pytest
from src.zero_sum_pairs import count_zero_sum_pairs

def test_basic_zero_sum_pairs():
    """Test basic functionality with zero-sum pairs"""
    assert count_zero_sum_pairs([1, -1, 2, -2, 3]) == 2

def test_empty_list():
    """Test empty list returns zero pairs"""
    assert count_zero_sum_pairs([]) == 0

def test_single_element_list():
    """Test list with single element returns zero pairs"""
    assert count_zero_sum_pairs([5]) == 0

def test_multiple_same_pair():
    """Test list with multiple instances of same zero-sum pair"""
    assert count_zero_sum_pairs([1, -1, 1, -1]) == 4

def test_zero_elements():
    """Test list with zero elements"""
    assert count_zero_sum_pairs([0, 0, 0]) == 3

def test_mixed_types_convertible():
    """Test list with mixed but convertible types"""
    assert count_zero_sum_pairs([1, -1.0, '2', -2]) == 2

def test_invalid_input_non_list():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError):
        count_zero_sum_pairs("not a list")

def test_invalid_input_non_numeric():
    """Test list with non-numeric elements raises TypeError"""
    with pytest.raises(TypeError):
        count_zero_sum_pairs([1, 2, 'a', -3])

def test_large_list():
    """Test a larger list with multiple zero-sum pairs"""
    test_list = [1, -1, 2, -2, 3, -3, 4, -4, 0, 0, 0]
    assert count_zero_sum_pairs(test_list) == 10