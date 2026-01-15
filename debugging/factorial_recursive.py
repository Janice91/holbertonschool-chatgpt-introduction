#!/usr/bin/env python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer recursively.

    Function:
        Calculates the factorial of the given integer `n` using recursion.
        Factorial of 0 is defined as 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the argument from the command line, convert to int, compute factorial
f = factorial(int(sys.argv[1]))
print(f)
