from functools import reduce


def increment_column(s, row_index, valor):
    for column_index in range(len(s[row_index])):
        new_column_value = s[row_index][column_index] + valor

        if new_column_value > 9:
            s[row_index][column_index] = 9
            valor = new_column_value - 9
            continue
        elif new_column_value < 1:
            s[row_index][column_index] = 1
            valor = new_column_value
            continue

        s[row_index][column_index] = new_column_value
        break


def get_skip_indexes(s):
    dimension = len(s)
    diagonal_left = [None] * dimension
    diagonal_right = [None] * dimension
    diagonal_right_column_index = dimension - 1
    valor = 15
    skip_indexes = []

    columns_matriz = [[row[i] for row in s] for i in range(dimension)]

    for i in range(dimension):
        row_sum = reduce(lambda a, b: a + b, s[i])

        if row_sum == valor:
            skip_indexes.extend([(i, j) for j in range(dimension)])

        column_sum = reduce(lambda a, b: a + b, columns_matriz[i])

        if column_sum == valor:
            skip_indexes.extend([(j, i) for j in range(dimension)])

        diagonal_left[i] = s[i][i]
        diagonal_right[i] = s[i][diagonal_right_column_index]
        diagonal_right_column_index -= 1

    diagonal_left_sum = reduce(lambda a, b: a + b, diagonal_left)

    if diagonal_left_sum == 15:
        skip_indexes.extend([(0, 0), (1, 1), (2, 2)])

    diagonal_right_sum = reduce(lambda a, b: a + b, diagonal_right)

    if diagonal_right_sum == 15:
        skip_indexes.extend([(0, 2), (1, 1), (2, 0)])

    return skip_indexes


def formingMagicSquare(s):
    dimension = len(s)
    valor = 15
    skip_indexes = get_skip_indexes(s)
    print(f"skip {skip_indexes}")
    for row_index, row in enumerate(s):
        row_sum = reduce(lambda a, b: a + b, row)
        diff = valor - row_sum

        if diff:
            for column_index in range(len(s[row_index])):
                if (row_index, column_index) in skip_indexes:
                    continue
                new_column_value = s[row_index][column_index] + diff

                if new_column_value > 9:
                    s[row_index][column_index] = 9
                    diff = new_column_value - 9
                    continue
                elif new_column_value < 1:
                    s[row_index][column_index] = 1
                    diff = new_column_value
                    continue

                s[row_index][column_index] = new_column_value
                break

    return s


input_example = [
    [5, 3, 4],
    [1, 5, 8],
    [6, 4, 2]
]

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
print(formingMagicSquare(input_0))
# print(get_skip_indexes(input_1))
