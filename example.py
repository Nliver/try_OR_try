#!/usr/bin/env python3
"""
Example usage of the try_or_try function.

This script demonstrates various use cases for the try_or_try utility.
"""

from try_or_try import try_or_try


def example_basic():
    """Basic example with primary and fallback."""
    print("=" * 60)
    print("Example 1: Basic fallback")
    print("=" * 60)
    
    def primary():
        print("  Trying primary operation...")
        raise ValueError("Primary failed!")
    
    def fallback():
        print("  Trying fallback operation...")
        return "Success from fallback!"
    
    result = try_or_try(primary, fallback)
    print(f"  Result: {result}")
    print()


def example_multiple_fallbacks():
    """Example with multiple fallback options."""
    print("=" * 60)
    print("Example 2: Multiple fallbacks")
    print("=" * 60)
    
    def first():
        print("  Trying first option...")
        raise ConnectionError("First option failed")
    
    def second():
        print("  Trying second option...")
        raise TimeoutError("Second option failed")
    
    def third():
        print("  Trying third option...")
        return "Third option succeeded!"
    
    result = try_or_try(first, second, third)
    print(f"  Result: {result}")
    print()


def example_immediate_success():
    """Example where the first option succeeds."""
    print("=" * 60)
    print("Example 3: Immediate success")
    print("=" * 60)
    
    def quick_win():
        print("  Trying primary operation...")
        return 42
    
    def not_needed():
        print("  This won't be called...")
        return 0
    
    result = try_or_try(quick_win, not_needed)
    print(f"  Result: {result}")
    print()


def example_all_fail():
    """Example where all options fail."""
    print("=" * 60)
    print("Example 4: All options fail")
    print("=" * 60)
    
    def first():
        print("  Trying first option...")
        raise ValueError("First failed")
    
    def second():
        print("  Trying second option...")
        raise RuntimeError("Second failed")
    
    try:
        result = try_or_try(first, second)
    except RuntimeError as e:
        print(f"  All options failed. Last error: {e}")
    print()


def example_api_fallback():
    """Practical example: API with fallback."""
    print("=" * 60)
    print("Example 5: API with fallback (simulated)")
    print("=" * 60)
    
    def fetch_from_api():
        print("  Attempting to fetch from API...")
        # Simulate API failure
        raise ConnectionError("API is down")
    
    def fetch_from_cache():
        print("  Fetching from cache...")
        return {"data": "cached response", "source": "cache"}
    
    result = try_or_try(fetch_from_api, fetch_from_cache)
    print(f"  Result: {result}")
    print()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("try_or_try Examples")
    print("=" * 60 + "\n")
    
    example_basic()
    example_multiple_fallbacks()
    example_immediate_success()
    example_all_fail()
    example_api_fallback()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)
