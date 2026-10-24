import argparse


def fibonacci(n):
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci usando recursión.

    La secuencia de Fibonacci se define como:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2)  para n > 1

    Args:
        n (int): posición en la secuencia (debe ser >= 0).

    Returns:
        int: el n-ésimo número de Fibonacci.
    """
    if n <= 1:
        # Casos base: F(0) = 0, F(1) = 1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    parser = argparse.ArgumentParser(
        description="Calcula el n-ésimo número de la secuencia de Fibonacci (versión recursiva)."
    )
    parser.add_argument(
        "n",
        type=int,
        help="Posición en la secuencia de Fibonacci a calcular (entero >= 0).",
    )
    args = parser.parse_args()

    resultado = fibonacci(args.n)
    print(f"Fibonacci({args.n}) = {resultado}")


if __name__ == "__main__":
    main()