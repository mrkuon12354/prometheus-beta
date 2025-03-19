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
    
    # Define cases where pairs create palindromes
    cases = [
        # Direct concatenation
        lambda words, i, j: is_palindrome(words[i] + words[j]),
        
        # Handling empty string
        lambda words, i, j: words[j] == "" and is_palindrome(words[i]),
        
        # Partial palindrome with shorter word
        lambda words, i, j: (
            len(words[i]) <= len(words[j]) and 
            (is_palindrome(words[j][:len(words[i])] + words[i]) or
             is_palindrome(words[i] + words[j][len(words[i]):]))
    ]
    
    # Check all possible pairs of words
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip pairing a word with itself
            if i == j:
                continue
            
            # Check all palindrome cases
            if any(case(words, i, j) for case in cases):
                palindrome_pairs.append((i, j))
    
    # Remove duplicate pairs and ensure unique combinations
    unique_pairs = list(set(palindrome_pairs))
    
    return unique_pairs