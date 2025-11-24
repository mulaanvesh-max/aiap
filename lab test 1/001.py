def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the n-th term.

    Args:
        n (int): Number of terms to generate. Must be a positive integer.

    Returns:
        list: A list containing the first n Fibonacci numbers.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# -------------------------------
# Example usage and testing
# -------------------------------
print(fibonacci(1))   # [0]
print(fibonacci(5))   # [0, 1, 1, 2, 3]
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Edge case tests
try:
    fibonacci(0)
except ValueError as e:
    print(e)  # Input must be a positive integer

try:
    fibonacci(-5)
except ValueError as e:
    print(e)  # Input must be a positive integer
