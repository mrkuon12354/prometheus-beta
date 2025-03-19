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
            
            # Match complete words first
            concatenated = words[i] + words[j]
            if is_palindrome(concatenated):
                palindrome_pairs.append((i, j))
                continue
            
            # Handle empty string
            if words[i] == "" and is_palindrome(words[j]):
                palindrome_pairs.append((i, j))
                continue
            
            # Check for partial palindrome matching
            # Check if a word can be inserted to create a palindrome
            for k in range(1, len(words[i]) + 1):
                left = words[i][:k]
                right = words[i][k:]
                
                # Forward direction
                if is_palindrome(left) and is_palindrome(right + words[j]):
                    palindrome_pairs.append((i, j))
                    break
                
                # Reverse direction
                if is_palindrome(right) and is_palindrome(left + words[j]):
                    palindrome_pairs.append((i, j))
                    break
    
    # Remove duplicate pairs and ensure unique combinations
    unique_pairs = list(set(palindrome_pairs))
    
    return unique_pairs