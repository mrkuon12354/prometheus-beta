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
    # This regex will insert a space before any uppercase letter (except at the start)
    # and replace underscores with spaces
    spaced_string = re.sub(r'_', ' ', input_string)
    spaced_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', spaced_string)
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', spaced_string).lower()
    
    # Split into words
    words = cleaned_string.split()
    
    # If there are no words, return empty string
    if not words:
        return ""
    
    # Process words: keep adjacent letters together, handle numbers
    processed_words = []
    current_word = ""
    current_is_numeric = False
    
    for word in words:
        # Check if current word is numeric
        is_numeric = word.isnumeric()
        
        # If it's a number or matches the current state, extend the current word
        if is_numeric == current_is_numeric or not current_word:
            current_word += word
            current_is_numeric = is_numeric
        else:
            # Add the previous word and start a new one
            processed_words.append(current_word)
            current_word = word
            current_is_numeric = is_numeric
    
    # Add the last word
    processed_words.append(current_word)
    
    # Join with hyphen
    return '-'.join(processed_words)