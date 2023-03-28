

def mkLs(input): 
    # This fucntion sorts the string alphabetically but it takes into account the specific rules give for numbering each string
    input = list(input)
    out = [(input[0], 0)]
    for inChar in input[1::]:
        lock = len(out)
        for i, char in enumerate(out):
            if not inChar > char[0]:
                lock = i
                break
        if lock == 0:
            out.insert(lock, (inChar, out[lock][1]+1))
        elif lock == len(out):
            out.insert(lock, (inChar, out[lock-1][1]+1))
        else:
            out.insert(lock, (inChar, max([out[lock-1][1]+1, out[lock][1]+1])))
        
        
        
    return out

def fString(oList):
    
    ind = 0
    for i, val in enumerate(oList):
        if val[1] == 0:
            ind = i
            break
    iList = [i for i in oList]
    output = [iList[ind]]
    val = 0
    iList.pop(ind)
    while True:
        stop = False
        if ind != 0:
            # This goes down the list and checks for the next consecutive number
            # Need to add a clause so it reverses when it finds 
            for i in reversed(range(0, ind)):
                if iList[i][1] == val+1:
                    stop = True
                    output.append(iList[i])
                    iList.pop(i)
                    ind = i
                    break
        

def getTraversals(input):
    ordered = mkLs(input)


print(mkLs("BINARYSEARCHTREE"))