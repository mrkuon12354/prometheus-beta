import re

def convert_to_alternating_path_case(input_string: str) -> str:
    """
    Convert a given string to alternating path case.
    
    Alternating path case follows these rules:
    - Remove any non-alphanumeric characters
    - Convert to lowercase
    - Separate words with a hyphen
    - Handle camel case and snake case
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating path case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> convert_to_alternating_path_case("Hello World!")
        'hello-world'
        >>> convert_to_alternating_path_case("Snake_Case Test")
        'snake-case-test'
        >>> convert_to_alternating_path_case("123 ABC xyz")
        '123-abc-xyz'
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert camel case and snake case to space-separated words
    # First replace underscores with spaces
    spaced_string = re.sub(r'_', ' ', input_string)
    
    # Split camel case: insert a space before capital letters (except at start)
    spaced_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', spaced_string)
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', spaced_string).lower()
    
    # Split into words, filter out empty strings
    words = [word for word in cleaned_string.split() if word]
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Process words, grouping by type (numeric/non-numeric)
    result_words = []
    current_segment = []
    current_is_numeric = None
    
    for word in words:
        # Determine if current word is numeric
        is_numeric = word.isnumeric()
        
        # If first word or same type as current segment
        if current_is_numeric is None or is_numeric == current_is_numeric:
            current_segment.append(word)
            current_is_numeric = is_numeric
        else:
            # Different type detected, add previous segment and start new
            result_words.append(''.join(current_segment))
            current_segment = [word]
            current_is_numeric = is_numeric
    
    # Add final segment
    result_words.append(''.join(current_segment))
    
    return '-'.join(result_words)