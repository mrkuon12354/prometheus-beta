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
    
    def get_consecutive_sequence_sum(substring: str) -> int:
        """Calculate sum for a single consecutive substring."""
        total = 0
        for i in range(len(substring)):
            if i == 0 or ord(substring[i]) == ord(substring[i-1]) + 1:
                total += ord(substring[i]) - ord('a') + 1
            else:
                break
        return total

    # Try all possible subsequences
    max_sum = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            sum_val = get_consecutive_sequence_sum(s[i:j+1])
            max_sum = max(max_sum, sum_val)
    
    return max_sum