import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    """Test a simple 3x3 assignment problem."""
    cost_matrix = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 5, 9]
    ]
    result = hungarian_algorithm(cost_matrix)
    
    # Validate result is a list of (row, col) tuples
    assert len(result) == 3
    assert len(set(r for r, _ in result)) == 3  # Unique rows
    assert len(set(c for _, c in result)) == 3  # Unique cols

def test_optimal_assignment():
    """Test that the algorithm finds the minimal cost assignment."""
    cost_matrix = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 5, 9]
    ]
    result = hungarian_algorithm(cost_matrix)
    
    # Compute total cost of the assignment
    total_cost = sum(cost_matrix[row][col] for row, col in result)
    assert total_cost == 6  # Optimal solution

def test_larger_matrix():
    """Test a larger matrix to ensure scalability."""
    cost_matrix = [
        [82, 83, 69, 92],
        [77, 37, 49, 92],
        [11, 69, 5, 86],
        [8, 9, 98, 23]
    ]
    result = hungarian_algorithm(cost_matrix)
    
    assert len(result) == 4
    assert len(set(r for r, _ in result)) == 4
    assert len(set(c for _, c in result)) == 4

def test_invalid_input():
    """Test error handling for invalid inputs."""
    # Non-square matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([
            [1, 2, 3],
            [4, 5, 6]
        ])
    
    # Non-matrix input
    with pytest.raises(ValueError):
        hungarian_algorithm([1, 2, 3])

def test_zero_cost_matrix():
    """Test a matrix with all zeros."""
    cost_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result = hungarian_algorithm(cost_matrix)
    
    assert len(result) == 3
    assert len(set(r for r, _ in result)) == 3
    assert len(set(c for _, c in result)) == 3

def test_different_zero_configurations():
    """Test matrices with different zero configurations."""
    # Scenario with complex zero arrangements
    cost_matrix = [
        [10, 0, 8],
        [0, 5, 0],
        [7, 0, 6]
    ]
    result = hungarian_algorithm(cost_matrix)
    
    assert len(result) == 3
    assert len(set(r for r, _ in result)) == 3
    assert len(set(c for _, c in result)) == 3

def test_numpy_input():
    """Test that the function works with numpy array input."""
    cost_matrix = np.array([
        [1, 2, 3],
        [2, 4, 6],
        [3, 5, 9]
    ])
    result = hungarian_algorithm(cost_matrix)
    
    assert len(result) == 3
    assert len(set(r for r, _ in result)) == 3
    assert len(set(c for _, c in result)) == 3