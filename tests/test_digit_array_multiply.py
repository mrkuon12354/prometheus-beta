import pytest
from src.digit_array_multiply import multiply_digit_arrays

def test_basic_multiplication():
    assert multiply_digit_arrays([1, 2, 3], [4, 5, 6]) == [5, 6, 0, 8, 8]

def test_zero_array():
    assert multiply_digit_arrays([0, 0, 1], [0, 0, 1]) == [0, 0, 0, 1]

def test_single_digit_array():
    assert multiply_digit_arrays([5], [7]) == [3, 5]

def test_unequal_length_arrays():
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_array([1, 2], [1, 2, 3])

def test_invalid_digit():
    with pytest.raises(ValueError, match="All digits must be between 0 and 9"):
        multiply_digit_arrays([1, 10, 3], [4, 5, 6])

def test_edge_case_large_numbers():
    assert multiply_digit_arrays([9, 9, 9], [9, 9, 9]) == [9, 9, 8, 0, 0, 1]