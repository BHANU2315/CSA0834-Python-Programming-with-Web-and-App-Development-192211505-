def matrix_addition(matrix1, matrix2):
    # Check if dimensions are compatible
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices are not of the same dimensions, addition not possible."
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Adding matrices
result_matrix = matrix_addition(matrix1, matrix2)

# Printing result
for row in result_matrix:
    print(row)
