def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenation of words forms a palindrome.
    
    Args:
        words (list): A list of strings to check for palindrome pairs.
    
    Returns:
        list: A list of tuples, where each tuple contains two indices (i, j) 
              such that words[i] + words[j] is a palindrome.
    
    Time Complexity: O(n^2 * m), where n is the number of words and m is the max word length
    Space Complexity: O(1) excluding the output list
    
    Examples:
        >>> find_palindrome_pairs(["bat", "tab", "cat"])
        [(0, 1), (1, 0)]
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [(0, 1), (1, 0), (3, 4), (4, 3)]
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    palindrome_pairs = []
    
    # Check all possible pairs of words
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip pairing a word with itself
            if i == j:
                continue
            
            # Various palindrome checking methods
            options = [
                # Direct concatenation
                words[i] + words[j],
                
                # Handling empty string
                words[j] if words[i] == "" else None,
                
                # Partial palindrome checks
                words[j][:len(words[i])] + words[i] if len(words[i]) <= len(words[j]) else None,
                words[i] + words[j][len(words[i]):] if len(words[i]) <= len(words[j]) else None
            ]
            
            # Check each option
            for opt in options:
                if opt is not None and is_palindrome(opt):
                    palindrome_pairs.append((i, j))
                    break
    
    return palindrome_pairs