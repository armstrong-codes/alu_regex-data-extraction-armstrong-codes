import re
from main import regex_patterns

def test_pattern(pattern_key, sample, expected):
    pattern = regex_patterns[pattern_key]
    result = re.findall(pattern, sample)
    print(f"\nTesting {pattern_key.upper()}...")
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
    assert expected == result, f"{pattern_key} failed!"

if __name__ == "__main__":
    test_pattern("emails", "Contact: user@example.com", ["user@example.com"])
    test_pattern("urls", "Visit https://example.com.", ["https://example.com"])
    test_pattern("phone_numbers", "Call 123-456-7890", ["123-456-7890"])
    test_pattern("credit_cards", "Card: 1234 5678 9012 3456", ["1234 5678 9012 3456"])
    test_pattern("times", "Time is 2:30 PM", ["2:30 PM"])
    test_pattern("html_tags", "<div>Text</div>", ["<div>", "</div>"])
    test_pattern("hashtags", "Tag #Python3", ["#Python3"])
    test_pattern("currency", "Price: $19.99", ["$19.99"])

    print("\n All tests passed!")
