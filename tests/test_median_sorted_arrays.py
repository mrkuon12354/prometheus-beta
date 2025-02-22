import pytest
from src.median_sorted_arrays import find_median_sorted_arrays

def test_even_length_arrays():
    """Test median for two even-length arrays"""
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_different_length_arrays():
    """Test median for two arrays of different lengths"""
    nums1 = [1, 2]
    nums2 = [3, 4, 5, 6]
    assert find_median_sorted_arrays(nums1, nums2) == 3.5

def test_odd_length_arrays():
    """Test median for two odd-length arrays"""
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    assert find_median_sorted_arrays(nums1, nums2) == 3.5

def test_one_empty_array():
    """Test median when one array is empty"""
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_unequal_length_arrays():
    """Test median for very unequal length arrays"""
    nums1 = [1]
    nums2 = [2, 3, 4, 5, 6]
    assert find_median_sorted_arrays(nums1, nums2) == 3.5

def test_single_element_arrays():
    """Test median for single-element arrays"""
    nums1 = [1]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 1.5

def test_both_arrays_empty_raises_error():
    """Test that an error is raised when both arrays are empty"""
    with pytest.raises(ValueError, match="Both input arrays cannot be empty"):
        find_median_sorted_arrays([], [])

def test_unsorted_input_raises_error():
    """Test that an error is raised for unsorted inputs"""
    with pytest.raises(ValueError, match="Input arrays are not sorted"):
        find_median_sorted_arrays([3, 1], [2, 4])