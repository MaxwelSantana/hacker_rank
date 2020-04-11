from functools import reduce


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    dimension = len(s)
    rows_sum = [None] * dimension
    columns_sum = [None] * dimension
    diagonal_sum = [None] * 2
    diagonal_left = [None] * dimension
    diagonal_right = [None] * dimension
    diagonal_left_column_index = 0
    diagonal_right_column_index = dimension - 1

    columns_matriz = [[row[i] for row in s] for i in range(dimension)]

    for i in range(dimension):
        rows_sum[i] = reduce(lambda a, b: a + b, s[i])
        columns_sum[i] = reduce(lambda a, b: a + b, columns_matriz[i])
        diagonal_left[i] = s[i][diagonal_left_column_index]
        diagonal_left_column_index += 1
        diagonal_right[i] = s[i][diagonal_right_column_index]
        diagonal_right_column_index -= 1

    diagonal_sum[0] = reduce(lambda a, b: a + b, diagonal_left)
    diagonal_sum[1] = reduce(lambda a, b: a + b, diagonal_right)

    print(rows_sum, columns_sum)
    print(diagonal_sum)

    return ''


input_0 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 5]
]

input_1 = [
    [4, 8, 2],
    [4, 5, 7],
    [6, 1, 6]
]

input_1_1 = [
    [4, 8, 4],
    [4, 5, 7],
    [6, 1, 6]
]
print(formingMagicSquare(input_1))
print(formingMagicSquare(input_1_1))
