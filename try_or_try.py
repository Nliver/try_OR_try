"""
try_or_try - A simple utility for chaining fallback operations.

This module provides a function that tries multiple operations in sequence,
returning the result of the first successful operation or raising an exception
if all operations fail.
"""


def try_or_try(*funcs):
    """
    Try multiple functions in sequence until one succeeds.
    
    This function attempts to execute each function in the order provided.
    If a function succeeds (doesn't raise an exception), its return value
    is returned immediately. If a function raises an exception, the next
    function is tried. If all functions fail, the last exception is raised.
    
    Args:
        *funcs: Variable number of callables to try in sequence.
    
    Returns:
        The return value of the first function that succeeds.
    
    Raises:
        Exception: The exception from the last function if all functions fail.
        ValueError: If no functions are provided.
    
    Examples:
        >>> def primary():
        ...     raise ValueError("Primary failed")
        >>> def fallback():
        ...     return "Success from fallback"
        >>> try_or_try(primary, fallback)
        'Success from fallback'
        
        >>> def always_works():
        ...     return 42
        >>> try_or_try(always_works, fallback)
        42
    """
    if not funcs:
        raise ValueError("At least one function must be provided")
    
    last_exception = None
    
    for func in funcs:
        try:
            return func()
        except Exception as e:
            last_exception = e
    
    # If we get here, all functions failed
    raise last_exception
