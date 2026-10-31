import numpy as np


def matrix_inverse(matrix):
    """
    Calcule l'inverse d'une matrice carrée.

    Args:
        matrix (numpy.ndarray): La matrice carrée.

    Returns:
        numpy.ndarray: L'inverse de la matrice, ou None si la matrice n'est pas inversible.
    """
    # Vérifier que la matrice est carrée
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("La matrice doit être carrée.")

    # Calculer l'inverse de la matrice en utilisant la fonction numpy
    try:
        inverse = np.linalg.inv(matrix)
        return inverse
    except np.linalg.LinAlgError:
        # Si la matrice n'est pas inversible, renvoyer None
        return None


if __name__ == "__main__":
    e = np.array([[1, 2], [4, 5]])
    print("Matrice originale :")
    print(e)
    print("\nMatrice inverse :")
    print(matrix_inverse(e))
