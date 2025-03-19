def count_zero_sum_pairs(arr):
    """
    Count the number of pairs of elements in the input array that sum up to 0.
    
    Args:
        arr (list): A list of integers to search for zero-sum pairs.
    
    Returns:
        int: The number of pairs that sum to zero.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    
    Examples:
        >>> count_zero_sum_pairs([1, -1, 2, -2, 3])
        2  # pairs are (1,-1) and (2,-2)
        >>> count_zero_sum_pairs([])
        0
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Convert to integers for consistent type checking
    try:
        arr = [int(x) for x in arr]
    except (ValueError, TypeError):
        raise TypeError("All elements must be convertible to integers")
    
    # If array is too short to form pairs, return 0
    if len(arr) < 2:
        return 0
    
    # Use a hash map approach for O(n) time complexity
    pair_count = 0
    num_counts = {}
    
    for num in arr:
        # Check if the complement exists in our previous numbers
        if -num in num_counts:
            pair_count += num_counts[-num]
        
        # Increment the count of the current number
        num_counts[num] = num_counts.get(num, 0) + 1
    
    return pair_count