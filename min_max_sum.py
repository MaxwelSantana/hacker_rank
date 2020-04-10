import functools

arr = [1, 2, 3, 4, 5]

arr.sort()
sumMax = functools.reduce(lambda a, b: a+b, arr[1:])
sumMin = functools.reduce(lambda a, b: a+b, arr[:len(arr)-1])

print(f"{sumMin} {sumMax}")