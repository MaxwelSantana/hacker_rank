from functools import reduce


# Complete the formingMagicSquare function below.
def transform(s, valor):
    qtd = 0
    for index, row in enumerate(s):
        qtd += transform_row(s, index, valor, qtd)
    print(f"QTD: {qtd}")


def transform_row(s, row_index, valor, qtd):
    row = s[row_index]
    row_sum = reduce(lambda a, b: a + b, row)
    diff = valor - row_sum
    fix = 0
    if diff > 0:
        fix = 1
        index_row_column = get_column_to_add(s, valor)
    elif diff < 0:
        fix = -1
        index_row_column = get_column_to_sub(s, valor)
    elif diff == 0:
        return qtd

    row[index_row_column] += fix
    qtd += 1
    return transform_row(s, row_index, valor, qtd)


def get_column_to_add(s, valor):
    columns = [[row[i] for row in s] for i in range(len(s[0]))]

    for index, column in enumerate(columns):
        column_sum = reduce(lambda a, b: a + b, column)
        diff = valor - column_sum
        if diff > 0:
            return index
    return 0


def get_column_to_sub(s, valor):
    columns = [[row[i] for row in s] for i in range(len(s[0]))]

    for index, column in enumerate(columns):
        column_sum = reduce(lambda a, b: a + b, column)
        diff = valor - column_sum
        if diff < 0:
            return index
    return 0


def get_diagonal(s):
    dimension = len(s)
    diagonal_left = [None] * dimension
    diagonal_right = [None] * dimension
    diagonal_right_column_index = dimension - 1

    for i in range(dimension):
        diagonal_left[i] = s[i][i]
        diagonal_right[i] = s[i][diagonal_right_column_index]
        diagonal_right_column_index -= 1
    return [diagonal_left, diagonal_right]


def working_values(values):
    print(values)


def formingMagicSquare(s):
    dimension = len(s)
    columns = [[row[i] for row in s] for i in range(dimension)]
    diagonal = get_diagonal(s)
    print(f"linhas: {s}")
    print(f"colunas: {columns}")
    print(f"diagonais: {diagonal}")

    working_values(s + columns + diagonal)
    s[0][0] = 1
    working_values(s + columns + diagonal)
    '''
    transform(s, 15)

    columns = [[row[i] for row in s] for i in range(dimension)]
    diagonal = get_diagonal(s)
    print(f"linhas: {s}")
    print(f"colunas: {columns}")
    print(f"diagonais: {diagonal}")
'''
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
print(formingMagicSquare(input_1))
# print(formingMagicSquare(input_1_1))
