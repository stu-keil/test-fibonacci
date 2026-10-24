def fibonacci(n: int) -> list[int]:
    """Return the first n terms of the Fibonacci sequence."""
    if n < 0:
        raise ValueError("n must be non-negative")

    sequence = []
    first, second = 0, 1
    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second
    return sequence
