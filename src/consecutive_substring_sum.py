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
    
    def is_consecutive(substr: str) -> bool:
        """Check if characters in substring are consecutive."""
        if len(substr) <= 1:
            return True
        return all(ord(substr[i+1]) == ord(substr[i]) + 1 for i in range(len(substr)-1))
    
    def calculate_sum(substr: str) -> int:
        """Calculate sum of character positions for a consecutive substring."""
        return sum(ord(char) - ord('a') + 1 for char in substr)
    
    max_sum = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if is_consecutive(substr):
                max_sum = max(max_sum, calculate_sum(substr[:3]))
    
    return max_sum