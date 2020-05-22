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


def rotate_queue_v2(index, value, initial_queue):
    if value not in initial_queue:
        return -1
    index_queue = initial_queue.index(value)

    distance = (value - 1) - index
    distance_invert_sinal = distance * -1
    direction = 1 if distance_invert_sinal >= 0 else -1

    rotate_count = 0
    for i in range(index_queue, index_queue - abs(distance), direction):
        if rotate_count == 2:
            return -1
        aux = initial_queue[i + direction]
        initial_queue[i + direction] = initial_queue[i]
        initial_queue[i] = aux
        rotate_count += 1

    return rotate_count


# Complete the minimumBribes function below.
def tiny_list(arr):
    if len(arr) < 8:
        arr = arr[0:]
    else:
        arr = arr[1:]
    last = arr[len(arr) - 1]
    arr.append(last + 1)
    arr.append(last + 2)
    return arr


def minimumBribes(q):
    total_bribes = 0
    initial_queue = list(range(1, 3 + 1))
    is_too_chaotic = False
    for index, value in enumerate(q):
        initial_queue = tiny_list(initial_queue)
        rotate_count = rotate_queue_v2(index, value, initial_queue)
        if rotate_count < 0:
            is_too_chaotic = True
            break
        total_bribes += rotate_count

    if is_too_chaotic:
        print("Too chaotic")
    else:
        print(total_bribes)


def minimumBribes_v2(Q):
    #
    # initialize the number of moves
    moves = 0
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    Q = [P - 1 for P in Q]
    #
    # Loop through each person (P) in the queue (Q)
    for i, P in enumerate(Q):
        # i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of
        # its original position
        if P - i > 2:
            print("Too chaotic")
            return
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P - 1, 0), i):
            if Q[j] > P:
                moves += 1
    print(moves)


if __name__ == '__main__':
    minimumBribes_v2([1, 2, 5, 3, 7, 8, 6, 4])
