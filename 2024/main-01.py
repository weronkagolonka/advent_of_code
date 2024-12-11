from typing import List
from common import readInputData

def calcDistance(locations: List[List[int]]):
    locations1 = locations[0]
    locations2 = locations[1]
    locations1.sort()
    locations2.sort()

    sorted = [locations1, locations2]
    distance = 0
    for i in range(len(sorted[0])):
        distance += abs(sorted[0][i] - sorted[1][i])

    return distance

def calcSimilarity(l1: List[int], l2: List[int]):
    similarity = 0
    for i in range(len(l1)):
        # find index where the num is
        # find the index where num + 1 is
        ocurrences = l2.count(l1[i])
        score = l1[i]*ocurrences
        similarity += score
    return similarity

def main():
    data = readInputData()
    distance = calcDistance(data)
    print(distance)

    similarity = calcSimilarity(data[0], data[1])
    print(similarity)
    

if __name__ == "__main__":
    main()