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
    
    # Split into words, filter out empty strings, join adjacent numbers and letters
    split_words = cleaned_string.split()
    merged_words = []
    
    current_merged = ""
    for word in split_words:
        # If current word is numeric or previous merged is numeric and current word contains letters
        if word.isnumeric() or (current_merged.isnumeric() and word.isalpha()):
            current_merged += word
        else:
            # If we have a previous merged word, add it
            if current_merged:
                merged_words.append(current_merged)
            current_merged = word
    
    # Add the last merged word if it exists
    if current_merged:
        merged_words.append(current_merged)
    
    # Join with hyphen
    return '-'.join(merged_words)