import pytest
from src.alternating_path_case import convert_to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert convert_to_alternating_path_case("Hello World") == "hello-world"

def test_mixed_case():
    """Test conversion with mixed case"""
    assert convert_to_alternating_path_case("SnakeCase Test") == "snake-case-test"

def test_with_special_characters():
    """Test conversion with special characters"""
    assert convert_to_alternating_path_case("Hello, World!") == "hello-world"

def test_with_numbers():
    """Test conversion with numbers"""
    assert convert_to_alternating_path_case("Test 123 ABC") == "test-123-abc"

def test_already_lowercase():
    """Test conversion of already lowercase string"""
    assert convert_to_alternating_path_case("hello world") == "hello-world"

def test_empty_string():
    """Test conversion of empty string"""
    assert convert_to_alternating_path_case("") == ""

def test_only_special_characters():
    """Test conversion of string with only special characters"""
    assert convert_to_alternating_path_case("!@#$%^") == ""

def test_type_error():
    """Test type error is raised for non-string input"""
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(123)

def test_multiple_spaces():
    """Test conversion with multiple spaces"""
    assert convert_to_alternating_path_case("hello   world  test") == "hello-world-test"