import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from multi_array_manipulator import multiArrayManipulator

def test_multiply_operation():
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    expected = [[2, 4], [6, 8]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_add_operation():
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': 3}
    expected = [[4, 5], [6, 7]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_transpose_operation():
    arr = [[1, 2], [3, 4]]
    manipulations = {'transpose': True}
    expected = [[1, 3], [2, 4]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_multiple_operations():
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2, 'add': 1, 'transpose': True}
    expected = [[3, 7], [5, 9]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_empty_array_raises_error():
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        multiArrayManipulator([], {})

def test_non_integer_array_raises_error():
    with pytest.raises(TypeError, match="Array must contain only integers"):
        multiArrayManipulator([[1, 'a'], [3, 4]], {})

def test_invalid_manipulation_type():
    with pytest.raises(TypeError, match="Manipulations must be a dictionary"):
        multiArrayManipulator([[1, 2], [3, 4]], None)

def test_unsupported_operation():
    with pytest.raises(ValueError, match="Unsupported operation"):
        multiArrayManipulator([[1, 2], [3, 4]], {'invalid_op': 5})

def test_invalid_multiply_value():
    with pytest.raises(TypeError, match="Multiply value must be a number"):
        multiArrayManipulator([[1, 2], [3, 4]], {'multiply': 'abc'})

def test_invalid_add_value():
    with pytest.raises(TypeError, match="Add value must be a number"):
        multiArrayManipulator([[1, 2], [3, 4]], {'add': 'abc'})

def test_invalid_transpose_value():
    with pytest.raises(ValueError, match="Transpose does not require a value"):
        multiArrayManipulator([[1, 2], [3, 4]], {'transpose': 5})