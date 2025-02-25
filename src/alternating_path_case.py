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
    # Then split camel case words
    spaced_string = re.sub(r'_', ' ', input_string)
    
    # Insert spaces before capital letters (except at start)
    spaced_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', spaced_string)
    
    # Remove non-alphanumeric characters, convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', spaced_string).lower()
    
    # Split into words, filter out empty strings
    words = [word for word in cleaned_string.split() if word]
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Processes words into separate segments
    processed_words = []
    current_segment = ""
    current_is_numeric = False
    
    for word in words:
        # Check if current word is entirely numeric
        is_numeric = word.isnumeric()
        
        # If current segment is empty or matches numeric state, add to segment
        if not current_segment or is_numeric == current_is_numeric:
            current_segment += word
            current_is_numeric = is_numeric
        else:
            # Different type, so add previous segment and start new
            processed_words.append(current_segment)
            current_segment = word
            current_is_numeric = is_numeric
    
    # Add final segment
    processed_words.append(current_segment)
    
    return '-'.join(processed_words)