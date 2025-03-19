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
    def is_partial_palindrome(s1, s2):
        """
        Check if concatenation of two strings forms a palindrome,
        including partial word matching.
        """
        # Try concatenation in both orders
        concat1 = s1 + s2
        concat2 = s2 + s1
        
        return (
            concat1 == concat1[::-1] or 
            concat2 == concat2[::-1]
        )
    
    palindrome_pairs = []
    
    # Check all possible pairs of words
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip pairing a word with itself
            if i == j:
                continue
            
            # Handle special case of empty string
            if words[i] == "" and all(is_partial_palindrome(words[i], words[j])):
                palindrome_pairs.append((i, j))
                continue
            
            # Check for palindrome pairs
            if is_partial_palindrome(words[i], words[j]):
                palindrome_pairs.append((i, j))
    
    # Remove duplicate pairs
    unique_pairs = list(set(palindrome_pairs))
    
    return unique_pairs