from functools import reduce


# Complete the formingMagicSquare function below.
def working_list(values):
    print(values)
    values[0][0] = 9
    print(values)


def formingMagicSquare(s):
    dimension = len(s)
    rows = [[0 for i in range(dimension)] for j in range(dimension)]
    columns = [None] * dimension
    diagonal_left = [None] * dimension
    diagonal_right = [None] * dimension
    diagonal_right_column_index = dimension - 1

    for row_index in range(dimension):
        diagonal_left[row_index] = s[row_index][row_index]
        diagonal_right[row_index] = s[row_index][diagonal_right_column_index]
        diagonal_right_column_index -= 1

        for column_index in range(dimension):
            rows[row_index][column_index] = s[row_index][column_index]

    rows.append(diagonal_left)
    working_list(rows)

    return ''


input_1 = [
    [4, 8, 2],
    [4, 5, 7],
    [6, 1, 6]
]
print(formingMagicSquare(input_1))
