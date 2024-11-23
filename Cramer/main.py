import numpy as np

from Cramer.cramer import input_matrix
from cramer import cramer_method

if __name__ == "__main__":
    A, B = input_matrix()

    solutions = cramer_method(A, B)
    print("\nРешение системы:")
    for i, val in enumerate(solutions):
        print(f"x{i + 1} = {val:.2f}")
