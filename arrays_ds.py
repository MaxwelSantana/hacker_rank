# Complete the reverseArray function below.
def reverseArray(a):
    for item in reversed(a):
        print(f"{item}", end=" ")


reverseArray([1, 4, 3, 2])
