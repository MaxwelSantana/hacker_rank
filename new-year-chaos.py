def rotate_queue(index, value, initial_queue):
    index_queue = initial_queue.index(value)

    distance = (index_queue - index) * -1
    direction = 1 if distance >= 0 else -1

    rotate_count = 0
    for i in range(index_queue, index, direction):
        if rotate_count == 2:
            return -1
        aux = initial_queue[i + direction]
        initial_queue[i + direction] = initial_queue[i]
        initial_queue[i] = aux
        rotate_count += 1

    return rotate_count


# Complete the minimumBribes function below.
def minimumBribes(q):
    total_bribes = 0
    initial_queue = list(range(1, len(q) + 1))
    is_too_chaotic = False
    for index, value in enumerate(q):
        rotate_count = rotate_queue(index, value, initial_queue)
        if rotate_count < 0:
            is_too_chaotic = True
            break
        total_bribes += rotate_count

    if is_too_chaotic:
        print("Too chaotic")
    else:
        print(total_bribes)


print(minimumBribes([2, 1, 5, 3, 4]))
