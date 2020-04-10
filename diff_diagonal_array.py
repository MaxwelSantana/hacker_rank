arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]

leftSum = 0
rightSum = 0

leftIndex = 0
rightIndex = len(arr) - 1
for index, item in enumerate(arr):
    leftSum += item[leftIndex]
    leftIndex += 1
    rightSum += item[rightIndex]
    rightIndex -= 1

print(abs(leftSum - rightSum))
