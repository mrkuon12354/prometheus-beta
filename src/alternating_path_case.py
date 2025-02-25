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
    
    # Group sequences of letters, keeping numbers distinct
    result_words = []
    current_letters = ""
    
    for word in words:
        # Check if the word is entirely numeric
        if word.isnumeric():
            # If we have accumulated letters, add them first
            if current_letters:
                result_words.append(current_letters)
                current_letters = ""
            
            # Add the numeric word
            result_words.append(word)
        else:
            # Accumulate letters
            current_letters += word
    
    # Add any remaining letters
    if current_letters:
        result_words.append(current_letters)
    
    return '-'.join(result_words)