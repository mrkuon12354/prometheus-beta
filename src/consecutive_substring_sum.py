def max_consecutive_substring_sum(s: str) -> int:
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Maximum sum of consecutive characters
    
    Examples:
        - 'aabbccdd' returns 8 (all consecutive characters)
        - 'abcabcabc' returns 3 (repeated subsequences)
        - '' returns 0 (empty string)
    """
    if not s:
        return 0
    
    # Track the maximum sum of consecutive characters
    max_sum = 0
    current_sum = 0
    
    for i in range(len(s)):
        # If first character or current character is consecutive to previous
        if i == 0 or ord(s[i]) == ord(s[i-1]) + 1:
            current_sum += ord(s[i]) - ord('a') + 1
            max_sum = max(max_sum, current_sum)
        else:
            # Reset current sum if not consecutive
            current_sum = ord(s[i]) - ord('a') + 1
            max_sum = max(max_sum, current_sum)
    
    return max_sum