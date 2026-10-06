# AI Tools Lab

A small Python project for practicing GitHub workflows, sorting algorithms, and utility functions with AI assistance. Each function was reviewed and run with sample input before being merged.

## Requirements

- Python 3.10 or newer
- Git, if you want to clone the repository

No third-party Python packages are required.

## Installation

```bash
git clone https://github.com/CodePandaaAI/ai-tools-lab.git
cd ai-tools-lab
```

## Usage

Run the files from the project folder:

```bash
python hello.py
python sorting.py
python utils.py
```

`sorting.py` sorts `[5, 1, 4, 2, 8]` into `[1, 2, 4, 5, 8]`.

`utils.py` demonstrates:

- `is_palindrome("Racecar")` → `True`
- `count_words("Hello AI Tools Lab")` → `4`
- `celsius_to_fahrenheit(0)` → `32.0`

You can also use the functions in Python code:

```python
from sorting import bubble_sort
from utils import is_palindrome, count_words, celsius_to_fahrenheit

print(bubble_sort([3, 1, 2]))
print(is_palindrome("Racecar"))
print(count_words("Hello AI Tools Lab"))
print(celsius_to_fahrenheit(0))
```

The current files print their sample results when imported, so the example above will show those results too.

## Contributors

- Romit Sharma

## License

MIT License. See [LICENSE](LICENSE) for the complete terms.