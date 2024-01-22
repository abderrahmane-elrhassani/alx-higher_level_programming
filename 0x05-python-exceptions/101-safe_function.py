#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_function(fct, *args):
    """Safely executes a given function with the provided arguments.

    If an exception occurs, it prints an error message to standard error.

    Args:
        fct (function): The function to execute.
        *args: Variable number of arguments to pass to the function.

    Returns:
        If an exception occurs - None.
        Otherwise - Result of the function.
    """
    try:
    
        result = fct(*args)
    except Exception as e:
    
        print(f"Exception: {e}", file=sys.stderr)
    
        return None
    else:
        
        return result
