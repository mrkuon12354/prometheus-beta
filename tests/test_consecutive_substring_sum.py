import pytest
from src.consecutive_substring_sum import max_consecutive_substring_sum

def test_empty_string():
    assert max_consecutive_substring_sum('') == 0

def test_single_character():
    assert max_consecutive_substring_sum('a') == 1
    assert max_consecutive_substring_sum('z') == 26

def test_consecutive_lowercase():
    assert max_consecutive_substring_sum('abc') == 6  # a=1, b=2, c=3 → sum is 6
    assert max_consecutive_substring_sum('xyz') == 24  # x=24, y=25, z=26 → sum is 75

def test_non_consecutive_characters():
    assert max_consecutive_substring_sum('adc') == 4  # a=1, d=4 → max sum is 4

def test_repeated_partial_sequence():
    assert max_consecutive_substring_sum('abcabcabc') == 3

def test_mixed_sequence():
    assert max_consecutive_substring_sum('abcdefbcdefg') == 21

def test_large_range_lowercase():
    assert max_consecutive_substring_sum('abcdefghijklmnopqrstuvwxyz') == 351

@pytest.mark.parametrize("input_str, expected", [
    ('', 0),
    ('a', 1),
    ('abc', 6),
    ('xyz', 24),
    ('abcabcabc', 3),
    ('aabbccdd', 8),
    ('abcdefbcdefg', 21)
])
def test_multiple_scenarios(input_str, expected):
    assert max_consecutive_substring_sum(input_str) == expected