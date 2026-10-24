def fibonacci(n: int) -> list[int]:
    """Devuelve los primeros n términos de la sucesión de Fibonacci."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n debe ser un entero")
    if n < 0:
        raise ValueError("n debe ser mayor o igual que 0")

    sequence = []
    first, second = 0, 1
    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second
    return sequence


if __name__ == "__main__":
    print(fibonacci(10))
