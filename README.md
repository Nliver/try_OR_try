# try_OR_try

A simple Python utility for chaining fallback operations. Try one operation, and if it fails, try another!

## Overview

`try_or_try` provides a clean and simple way to attempt multiple operations in sequence, returning the result of the first successful operation. This is useful for implementing fallback mechanisms, retry logic with different strategies, or graceful degradation.

## Installation

Simply copy `try_or_try.py` to your project, or install from the repository:

```bash
pip install git+https://github.com/Nliver/try_OR_try.git
```

## Usage

### Basic Example

```python
from try_or_try import try_or_try

def fetch_from_primary_api():
    # Might fail if API is down
    raise ConnectionError("Primary API is down")

def fetch_from_backup_api():
    # Fallback option
    return {"data": "from backup"}

# Try primary first, fall back to backup if it fails
result = try_or_try(fetch_from_primary_api, fetch_from_backup_api)
print(result)  # {"data": "from backup"}
```

### Multiple Fallbacks

```python
from try_or_try import try_or_try

def try_cdn():
    raise TimeoutError("CDN timeout")

def try_origin():
    raise ConnectionError("Origin unreachable")

def try_cache():
    return "cached_data"

# Try multiple options in order
data = try_or_try(try_cdn, try_origin, try_cache)
print(data)  # "cached_data"
```

### Configuration Loading Example

```python
from try_or_try import try_or_try
import json

def load_env_config():
    # Try to load from environment variables
    import os
    if 'CONFIG' not in os.environ:
        raise ValueError("No CONFIG in environment")
    return json.loads(os.environ['CONFIG'])

def load_file_config():
    # Try to load from config file
    with open('config.json', 'r') as f:
        return json.load(f)

def load_default_config():
    # Fall back to defaults
    return {"host": "localhost", "port": 8080}

# Try loading config from multiple sources
config = try_or_try(
    load_env_config,
    load_file_config,
    load_default_config
)
```

## API Reference

### `try_or_try(*funcs)`

Try multiple functions in sequence until one succeeds.

**Parameters:**
- `*funcs`: Variable number of callables to try in sequence. Each should be a zero-argument callable.

**Returns:**
- The return value of the first function that succeeds (doesn't raise an exception).

**Raises:**
- The exception from the last function if all functions fail.
- `ValueError` if no functions are provided.

**Behavior:**
- Functions are called in the order provided
- If a function succeeds (doesn't raise an exception), its return value is returned immediately
- If a function raises an exception, the next function is tried
- If all functions fail, the exception from the last function is raised
- "Falsy" return values (None, False, 0, "", etc.) are considered successful returns

## Running Tests

```bash
python -m unittest test_try_or_try.py -v
```

## License

MIT License - Feel free to use this in your projects!