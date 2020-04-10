n = 40

for index in range(1, n+1, 1):
    hash_tags = '#' * index
    spaces = ' ' * (n-index)
    print(f"{spaces}{hash_tags}")
