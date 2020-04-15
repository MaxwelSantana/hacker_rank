def rotLeft(a, d):
    a_len = len(a)
    control_number = d % a_len
    return a[control_number:] + a[0:control_number]


print(rotLeft([1, 2, 3, 4, 5], 506))
