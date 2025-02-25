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
    
    # Group words, keeping numeric words separate
    result_words = []
    current_word = ""
    
    for word in words:
        # If current word is numeric or previous word was numeric
        if word.isnumeric() or (current_word and current_word.isnumeric()):
            # If we have a non-numeric previous word, add it
            if current_word and not current_word.isnumeric():
                result_words.append(current_word)
                current_word = word
            else:
                current_word += word
        else:
            # If we have a numeric previous word, add it
            if current_word and current_word.isnumeric():
                result_words.append(current_word)
                current_word = word
            else:
                current_word += word
    
    # Add final word
    if current_word:
        result_words.append(current_word)
    
    return '-'.join(result_words)