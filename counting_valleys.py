s = "UDDDUDUU"

sea_level = 0
garys_path = 0
count_valley = 0

for step in s:
    if step == "U":
        garys_path += 1
    elif step == "D":
        if garys_path == sea_level:
            count_valley += 1
        garys_path -= 1

print(count_valley)