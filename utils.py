def is_palindrome(s: str) -> bool:
    """Check whether text reads the same backward, ignoring case and punctuation."""
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text: str) -> int:
    """Count words separated by whitespace."""
    return len(text.split())


def celsius_to_fahrenheit(c: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


print(is_palindrome("Racecar"))          # True
print(count_words("Hello AI Tools Lab")) # 4
print(celsius_to_fahrenheit(0))          # 32.0