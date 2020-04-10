# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    total_clouds = len(c)
    index = 0
    while index < total_clouds:
        if index + 2 < total_clouds and c[index + 2] == 0:
            next_safer_and_further_cloud = 2
        elif index + 1 < total_clouds:
            next_safer_and_further_cloud = 1
        else:
            break
        index += next_safer_and_further_cloud
        jumps += 1
    return jumps


# print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds(
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1,
     0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
     0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0]))
