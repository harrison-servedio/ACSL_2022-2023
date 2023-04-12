def missingArrow(size, targets, numbers, arrows):
    board = [["" for j in range(size)] for i in range(size)]
    targets = targets.split(' ')
    for t in targets:
        row, col = int(t[0]), int(t[1])
        board[row][col] = t

    directions = [[[-1, 0], "A"], [[0, -1], "B"], [[1, 0], "C"], [[0, 1], "D"],
                  [[-1, -1], "E"], [[1, -1], "F"], [[1, 1], "G"], [[-1, 1], "H"]]

    ndirections = dict([[b, a] for a, b in directions])

    coln, rown = list(map(int, list(numbers.split(" ")[0]))), list(
        map(int, list(numbers.split(" ")[1])))
    for a in arrows.split(" "):
        board[int(a[0])][int(a[1])] = 'a'

        adir = ndirections[a[2]]
        apos = (int(a[0]), int(a[1]))
        for i in range(1, size + 1):
            aa = apos[0] + adir[1]*i
            bb = apos[1] + adir[0]*i
            if board[aa][bb] != '':
                board[aa][bb] = ''
                break

        coln[int(a[0])] -= 1
        rown[int(a[1])] -= 1
    newarrow = (coln.index(1), rown.index(1))

    direction = ''
    for vector, letter in directions:
        try:
            for i in range(1, size + 1):
                b = newarrow[0] + vector[1]*i
                a = newarrow[1] + vector[0]*i
                if b < 0 or a < 0:
                    break

                if board[b][a] == 'a':
                    break
                elif board[b][a] != '':
                    direction = letter
                    break
        except IndexError:
            continue
    return ''.join(list(map(str, [newarrow[0], newarrow[1], direction])))


# print(missingArrow(4, "02 11 20 21", "0103 1012", "13E 30B 33E"))
print(missingArrow(6, "01 10 23 42 53 12 04 52 00",
      "200232 111024", "05H 34H 35H 54E 55E 40F 45A 41B"))