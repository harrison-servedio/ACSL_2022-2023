def makeArr(n, points, arrows):
    # makes an empty array of size n by n
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(0)

    # Adds in the points where they are needed
    for target in points.split(" "):
        arr[int(target[0])][int(target[1])] = 1
    for arrow in arrows.split(" "):
        arr[int(arrow[0])][int(arrow[1])] = arrow[2]
    return arr

def isPointed(arr, target):
    # checks if a point is pointed
    counter = 1
    target = [int(target[0]), int(target[1])]
    bad = [0 for i in range(8)]
    while True:
        # Checks top left
        if target[0] - counter >= 0 and target[1] - counter >= 0 and bad[0] == 0:
            if arr[target[0] - counter][target[1] - counter] == "G":
                return True
            elif arr[target[0] - counter][target[1] - counter] != 0:
                bad[0] = 1
        # Checks top middle
        if target[0] - counter >= 0 and bad[1] == 0:
            if arr[target[0] - counter][target[1]] == "D":
                return True
            elif arr[target[0] - counter][target[1]] != 0:
                bad[1] = 1
        # Checks top right
        if target[0] - counter >= 0 and target[1] + counter < len(arr) and bad[2] == 0:
            if arr[target[0] - counter][target[1] + counter] == "H":
                return True
            elif arr[target[0] - counter][target[1] + counter] != 0:
                bad[2] = 1
        # Checks middle right
        if target[1] + counter < len(arr) and bad[3] == 0:
            if arr[target[0]][target[1] + counter] == "A":
                return True
            elif arr[target[0]][target[1] + counter] != 0:
                bad[3] = 1
        # Checks bottom right
        if target[0] + counter < len(arr) and target[1] + counter < len(arr) and bad[4] == 0:
            if arr[target[0] + counter][target[1] + counter] == "E":
                return True
            elif arr[target[0] + counter][target[1] + counter] != 0:
                bad[4] = 1
        # Checks bottom middle
        if target[0] + counter < len(arr) and bad[5] == 0:
            if arr[target[0] + counter][target[1]] == "B":
                return True
            elif arr[target[0] + counter][target[1]] != 0:
                bad[5] = 1
        # Checks bottom left
        if target[0] + counter < len(arr) and target[1] - counter >= 0 and bad[6] == 0:
            if arr[target[0] + counter][target[1] - counter] == "F":
                return True
            elif arr[target[0] + counter][target[1] - counter] != 0:
                bad[6] = 1
        # Checks middle left
        if target[1] - counter >= 0 and bad[7] == 0:
            if arr[target[0]][target[1] - counter] == "C":
                return True
            elif arr[target[0]][target[1] - counter] != 0:
                bad[7] = 1
        counter += 1
        if counter > len(arr) or sum(bad) == 8:
            return False
    
def findPoint(n, targets, numbers):
    rows = [0 for i in range(n)]
    cols = [0 for i in range(n)]
    numbers = numbers.split(" ")
    iRows = [int(i) for i in numbers[0]]
    iCols = [int(i) for i in numbers[1]]
    for target in targets.split(" "):
        rows[int(target[0])] += 1
        cols[int(target[1])] += 1
    point = [0,0]
    for i in range(n):
        if rows[i] != iRows[i]:
            point[0] = i
        if cols[i] != iCols[i]:
            point[1] = i
    return str(point[0]) + str(point[1])


def checkPoints(n, targets, arr):
    points = targets.split(" ")
    for point in points:
        if not isPointed(arr, point):
            return True
    return False



def missingArrow(size, targets, numbers, arrows):
    arr = makeArr(size, targets, arrows)
    point = findPoint(size, arrows, numbers)

    options = list("ABCDEFGH")
    for i in options:
        arr[int(point[0])][int(point[1])] = i
        if not checkPoints(size, targets, arr):
            return point +i

x = makeArr(4, "02 11 20 21", "13E 30B 33E")


# print(findPoint(4, "13E 30B 33E", "0103 1012"))
print(missingArrow(4, "02 11 20 21", "0103 1012", "13E 30B 33E"))
