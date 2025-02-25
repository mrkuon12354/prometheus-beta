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
    
    # Group numeric and non-numeric words
    result_words = []
    
    # Temporary storage to handle numeric/non-numeric groups
    current_numeric_group = ""
    current_letter_group = ""
    
    for word in words:
        if word.isnumeric():
            # If we have accumulated letters, add them first
            if current_letter_group:
                result_words.append(current_letter_group)
                current_letter_group = ""
            
            # If we have a different numeric group, add it first
            if current_numeric_group and current_numeric_group != word:
                result_words.append(current_numeric_group)
            
            # Update or initialize numeric group
            current_numeric_group = word
        else:
            # If we have a numeric group, add it
            if current_numeric_group:
                result_words.append(current_numeric_group)
                current_numeric_group = ""
            
            # Accumulate letters 
            current_letter_group += word
    
    # Add any remaining groups
    if current_numeric_group:
        result_words.append(current_numeric_group)
    if current_letter_group:
        result_words.append(current_letter_group)
    
    return '-'.join(result_words)