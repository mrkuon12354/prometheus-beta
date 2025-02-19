def multiply_digit_arrays(A, B):
    """
    Multiply two arrays of equal length representing numbers as digit arrays.
    
    Args:
        A (list): First array of digits
        B (list): Second array of digits of same length as A
    
    Returns:
        list: Result of multiplying A and B, represented as an array of digits
    
    Raises:
        ValueError: If input arrays are not of equal length or contain invalid digits
    """
    # Validate input
    if len(A) != len(B):
        raise ValueError("Input arrays must be of equal length")
    
    # Check for valid digits (0-9)
    if not all(0 <= digit <= 9 for digit in A + B):
        raise ValueError("All digits must be between 0 and 9")
    
    # Convert digit arrays to integers
    num1 = int(''.join(map(str, A)))
    num2 = int(''.join(map(str, B)))
    
    # Multiply
    result = num1 * num2
    
    # Convert result to string and digit list
    result_str = str(result)
    
    # Pad the result with leading zeros to match the input array length
    padded_result = result_str.zfill(len(A) * 2)
    result_digits = [int(digit) for digit in padded_result]
    
    return result_digits