def birthdayCakeCandles(ar):
    ar.sort()
    higher = ar[len(ar) - 1]
    return ar.count(higher)


print(birthdayCakeCandles([3, 2, 1, 3]))
