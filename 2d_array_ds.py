from functools import reduce
import sys


def hourglassSum(arr):
    bigger_sum = -sys.maxsize - 1
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            hourglass_sum = hourglassSumByIndex(i, j, arr)
            if hourglass_sum > bigger_sum:
                bigger_sum = hourglass_sum
    return bigger_sum


def hourglassSumByIndex(i, j, arr):
    top = arr[i][j:j + 3]
    mid = arr[i + 1][j + 1]
    base = arr[i + 2][j:j + 3]
    top_sum = list_sum(top)
    mid_sum = mid
    base_sum = list_sum(base)
    return top_sum + mid_sum + base_sum


def list_sum(arr):
    return reduce(lambda a, b: a + b, arr)


input_1 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

input_2 = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
]
print(hourglassSum(input_2))
