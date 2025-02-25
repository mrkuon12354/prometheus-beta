import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    Args:
        cost_matrix (list or np.ndarray): A square cost matrix where each element 
                                          represents the cost of assigning a worker 
                                          to a job.
    
    Returns:
        list: An optimal assignment of workers to jobs with minimal total cost.
    
    Raises:
        ValueError: If the input is not a valid square matrix.
    """
    # Convert input to numpy array for easier manipulation
    matrix = np.array(cost_matrix, dtype=float)
    
    # Validate input
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a square matrix")
    
    n = matrix.shape[0]
    
    # Step 1: Subtract row minimums
    for i in range(n):
        matrix[i] -= matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        matrix[:, j] -= matrix[:, j].min()
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # Find zeros
        zeros = np.argwhere(matrix == 0)
        row_lines = set()
        col_lines = set()
        
        # Greedy approach to cover zeros
        for zero in zeros:
            row, col = zero
            if row not in row_lines and col not in col_lines:
                row_lines.add(row)
                col_lines.add(col)
        
        return list(row_lines), list(col_lines)
    
    # Step 4: Find optimal assignment
    def find_assignment(matrix):
        assignment = []
        used_rows = set()
        used_cols = set()
        
        # Sort zeros to prioritize unique zero lines
        zeros = sorted([(r, c) for r, c in np.argwhere(matrix == 0)], 
                       key=lambda x: (sum(matrix[x[0]] == 0), sum(matrix[:, x[1]] == 0)))
        
        for row, col in zeros:
            if row not in used_rows and col not in used_cols:
                assignment.append((row, col))
                used_rows.add(row)
                used_cols.add(col)
        
        return assignment
    
    # Repeat until optimal solution is found
    while True:
        # Find the assignment
        assignment = find_assignment(matrix)
        
        # If assignment covers all rows/cols, return result
        if len(assignment) == n:
            return assignment
        
        # Find the smallest uncovered value
        covered_rows, covered_cols = cover_zeros(matrix)
        uncovered = matrix.copy()
        
        # Mark covered rows and columns
        uncovered[covered_rows, :] = np.inf
        uncovered[:, covered_cols] = np.inf
        
        # Find minimum of uncovered values
        min_uncovered = np.min(uncovered)
        
        # Adjust matrix
        matrix[covered_rows, :] -= min_uncovered
        matrix[:, covered_cols] += min_uncovered