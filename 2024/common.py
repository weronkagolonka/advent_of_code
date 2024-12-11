import re

def readInputData():
    locations = [[], []]
    with open("input-01.txt") as f:
        for line in f:
            l1, l2 = re.sub(r'\s+', " ",line.strip()).split(" ")
            locations[0].append(int(l1))
            locations[1].append(int(l2))
    return locations