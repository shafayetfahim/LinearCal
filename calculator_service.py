import numpy

''' MATRIX FUNCTIONS BELOW '''
def add_matrices(matrix_a, matrix_b):
    """
    Adds two matrices element-wise.

    :param matrix_a: First matrix (list of lists).
    :param matrix_b: Second matrix (list of lists).
    :return: Resulting matrix after addition.
    :raises ValueError: If the dimensions of the matrices are not the same.
    """
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]

def subtract_matrices(matrix_a, matrix_b):
    """
    Subtracts the second matrix from the first matrix element-wise.

    :param matrix_a: First matrix (list of lists).
    :param matrix_b: Second matrix (list of lists).
    :return: Resulting matrix after subtraction.
    :raises ValueError: If the dimensions of the matrices are not the same.
    """
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    return [[matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]

def scalar_multiply_matrix(scalar, matrix):
    """
    Multiplies a matrix by a scalar.

    :param scalar: The scalar value (int or float).
    :param matrix: The matrix to multiply (list of lists).
    :return: Resulting matrix after scalar multiplication.
    """
    return [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

def rref(matrix):
    """
    Computes the Reduced Row Echelon Form (RREF) of a given matrix.

    :param matrix: A list of lists representing the matrix (rows of numbers).
    :return: The matrix in RREF.
    """
    # Copy the matrix to avoid modifying the original
    m = [row[:] for row in matrix]
    rows, cols = len(m), len(m[0])
    lead = 0

    for r in range(rows):
        if lead >= cols:
            break
        i = r
        while m[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    return m
        # Swap rows to move the non-zero element to the pivot position
        m[i], m[r] = m[r], m[i]

        # Normalize the pivot row (make the leading entry 1)
        pivot = m[r][lead]
        m[r] = [x / pivot for x in m[r]]

        # Make all entries in the current column (except pivot) zero
        for i in range(rows):
            if i != r:
                multiplier = m[i][lead]
                m[i] = [x - multiplier * y for x, y in zip(m[i], m[r])]

        lead += 1

    return m

def row_space(matrix):
    """
    Computes the row space of a matrix.

    :param matrix: A list of lists representing the matrix.
    :return: A list of rows forming the row space (basis for row space).
    """
    rref_matrix = rref(matrix)
    return [row for row in rref_matrix if any(x != 0 for x in row)]

def column_space(matrix):
    """
    Computes the column space of a matrix.

    :param matrix: A list of lists representing the matrix.
    :return: A list of columns forming the column space (basis for column space).
    """
    rref_matrix = rref(matrix)
    pivot_columns = [j for j in range(len(rref_matrix[0])) if any(rref_matrix[i][j] != 0 for i in range(len(rref_matrix)))]

    return [[matrix[i][j] for i in range(len(matrix))] for j in pivot_columns]

def rank(matrix):
    """
    Computes the rank of a matrix.

    :param matrix: A list of lists representing the matrix.
    :return: An integer representing the rank of the matrix.
    """
    rref_matrix = rref(matrix)
    return sum(1 for row in rref_matrix if any(x != 0 for x in row))

def inverse_matrix(matrix):
    """
    Computes the inverse of a given square matrix using Gaussian elimination.

    :param matrix: A list of lists representing the square matrix.
    :return: The inverse of the matrix as a list of lists.
    :raises ValueError: If the matrix is not square or not invertible.
    """
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square.")

    # Create the augmented matrix [matrix | identity]
    augmented = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    # Perform Gaussian elimination to transform [matrix | identity] -> [identity | inverse]
    for i in range(n):
        # Find the pivot element
        pivot = augmented[i][i]
        if pivot == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")

        # Normalize the pivot row
        augmented[i] = [x / pivot for x in augmented[i]]

        # Eliminate the current column in all other rows
        for j in range(n):
            if i != j:
                factor = augmented[j][i]
                augmented[j] = [x - factor * y for x, y in zip(augmented[j], augmented[i])]

    # Extract the inverse matrix from the augmented matrix
    inverse = [row[n:] for row in augmented]
    return inverse

''' VECTOR FUNCTIONS BELOW'''

def add_vectors(vector_a, vector_b):
    """
    Adds two vectors element-wise.

    :param vector_a: First vector (list of numbers).
    :param vector_b: Second vector (list of numbers).
    :return: Resulting vector after addition.
    :raises ValueError: If the vectors have different lengths.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length for addition.")

    return [vector_a[i] + vector_b[i] for i in range(len(vector_a))]

def subtract_vectors(vector_a, vector_b):
    """
    Subtracts the second vector from the first vector element-wise.

    :param vector_a: First vector (list of numbers).
    :param vector_b: Second vector (list of numbers).
    :return: Resulting vector after subtraction.
    :raises ValueError: If the vectors have different lengths.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length for subtraction.")

    return [vector_a[i] - vector_b[i] for i in range(len(vector_a))]

def scalar_multiply_vector(scalar, vector):
    """
    Multiplies a vector by a scalar.

    :param scalar: The scalar value (int or float).
    :param vector: The vector to multiply (list of numbers).
    :return: Resulting vector after scalar multiplication.
    """
    return [scalar * element for element in vector]

def dot_product(vector_a, vector_b):
    """
    Computes the dot product of two vectors.

    :param vector_a: First vector (list of numbers).
    :param vector_b: Second vector (list of numbers).
    :return: The dot product of the two vectors.
    :raises ValueError: If the vectors have different lengths.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length for dot product.")

    return sum(a * b for a, b in zip(vector_a, vector_b))

def cross_product(vector_a, vector_b):
    """
    Computes the cross product of two 3D vectors.

    :param vector_a: First vector (list of 3 numbers).
    :param vector_b: Second vector (list of 3 numbers).
    :return: The cross product as a 3D vector.
    :raises ValueError: If the vectors are not 3D.
    """
    if len(vector_a) != 3 or len(vector_b) != 3:
        raise ValueError("Vectors must be 3D for cross product.")

    return [
        vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1],
        vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2],
        vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
    ]

import math

def normalize_vector(vector):
    """
    Normalizes a vector to have a magnitude of 1.

    :param vector: The input vector (list of numbers).
    :return: The normalized vector.
    :raises ValueError: If the vector is the zero vector.
    """
    magnitude = math.sqrt(sum(x ** 2 for x in vector))
    if magnitude == 0:
        raise ValueError("Cannot normalize the zero vector.")

    return [x / magnitude for x in vector]



