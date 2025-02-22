def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays with O(log(min(m,n))) time complexity.
    
    Args:
        nums1 (list): First sorted input array
        nums2 (list): Second sorted input array
    
    Returns:
        float: Median of the combined sorted arrays
    
    Raises:
        ValueError: If both input arrays are empty
    """
    # Ensure nums1 is the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # Handle empty array cases
    if not nums1 and not nums2:
        raise ValueError("Both input arrays cannot be empty")
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition_x = (left + right) // 2
        partition_y = (m + n + 1) // 2 - partition_x
        
        # Find max and min values for partitions
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
        # Check if partition is valid
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # If total length is odd
            if (m + n) % 2 == 1:
                return max(max_left_x, max_left_y)
            
            # If total length is even
            return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
        
        # Adjust partitions
        elif max_left_x > min_right_y:
            right = partition_x - 1
        else:
            left = partition_x + 1
    
    raise ValueError("Input arrays are not sorted")