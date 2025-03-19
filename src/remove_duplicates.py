def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list of integers without using built-in set() or dict().

    Args:
        sorted_list (list): A sorted list of integers.

    Returns:
        list: A new list with duplicate values removed, maintaining the original order.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is not sorted.
    """
    # Check input type
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not sorted_list:
        return []
    
    # Check if list is sorted
    if sorted_list != sorted(sorted_list):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Remove duplicates while preserving order
    unique_list = []
    for num in sorted_list:
        # Only add if the number is not already in the unique list
        if not unique_list or num > unique_list[-1]:
            unique_list.append(num)
    
    return unique_list