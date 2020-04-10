arr = [-4, 3, -9, 0, 4, 1]

positive = len([x for x in arr if x > 0])
negative = len([x for x in arr if x < 0])
zero = len([x for x in arr if x == 0])

totalItems = len(arr)

print("{:.6f}".format(positive/totalItems))
print("{:.6f}".format(negative/totalItems))
print("{:.6f}".format(zero/totalItems))