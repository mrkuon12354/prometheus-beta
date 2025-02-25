import pytest
from src.alternating_path_case import convert_to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion"""
    result = convert_to_alternating_path_case("Hello World")
    assert result == "hello-world", f"Expected 'hello-world', got '{result}'"

def test_mixed_case():
    """Test conversion with mixed case"""
    result = convert_to_alternating_path_case("SnakeCase Test")
    assert result == "snake-case-test", f"Expected 'snake-case-test', got '{result}'"

def test_with_special_characters():
    """Test conversion with special characters"""
    result = convert_to_alternating_path_case("Hello, World!")
    assert result == "hello-world", f"Expected 'hello-world', got '{result}'"

def test_with_numbers():
    """Test conversion with numbers"""
    result = convert_to_alternating_path_case("Test 123 ABC")
    assert result == "test-123-abc", f"Expected 'test-123-abc', got '{result}'"

def test_already_lowercase():
    """Test conversion of already lowercase string"""
    result = convert_to_alternating_path_case("hello world")
    assert result == "hello-world", f"Expected 'hello-world', got '{result}'"

def test_empty_string():
    """Test conversion of empty string"""
    result = convert_to_alternating_path_case("")
    assert result == "", f"Expected '', got '{result}'"

def test_only_special_characters():
    """Test conversion of string with only special characters"""
    result = convert_to_alternating_path_case("!@#$%^")
    assert result == "", f"Expected '', got '{result}'"

def test_type_error():
    """Test type error is raised for non-string input"""
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(123)

def test_multiple_spaces():
    """Test conversion with multiple spaces"""
    result = convert_to_alternating_path_case("hello   world  test")
    assert result == "hello-world-test", f"Expected 'hello-world-test', got '{result}'"