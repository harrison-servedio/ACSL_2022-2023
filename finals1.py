def beforee(orig, illegal, ind):
    retStr = ""
    for j in range(3):
        ind-=1
        if orig[ind].lower() not in illegal:
            retStr = orig[ind] + " " + retStr
        else:
            return retStr.strip(" ")
    return retStr.strip(" ")

def afterr(orig, illegal, ind):
    retStr = ""
    for j in range(3):
        ind+=1
        if orig[ind].lower() not in illegal:
            retStr += orig[ind] + " "
        else:
            return retStr.strip(" ")
    return retStr.strip(" ")


def findARow(original, unused, rows):
    original = original.replace(",", " ,").replace(".", " .").replace("?", " ?").split(" ")

    illegal = unused.split(" ") + [".", "?", ","]
    wb = []
    wa = []
    w = []
    ra = [int(i) for i in rows.split(" ")]

    for i, word in enumerate(original):
        if word.lower() not in illegal:
            w.append(word)
            wb.append(beforee(original, illegal, i))
            wa.append(afterr(original, illegal, i))
    all = []
    for i in range(len(w)):
        all.append([wb[i], w[i], wa[i]])
    all = sorted(all, key=lambda x:x[1].lower())

    all = all[ra[0]-1:ra[1]]

    # Right justify
    loig = 0
    for i in all:
        loig = max(loig, len(i[0]))
    for i in all:
        i[0] = "-"*(loig-len(i[0])) + i[0]
    
    # Left justify done twice
    for j in range(2):
        loig = 0
        for i in all:
            loig = max(loig, len(i[1+j]))
        for i in all:
            i[1+j] =  i[1+j] + "-"*(loig-len(i[1+j]))

    ind = 0
    smallest = 1000000
    for i, line in enumerate(all):
        cnt = line[0].count("-") + line[1].count("-") + line[2].count("-")
        if cnt < smallest:
            smallest = cnt
            ind = i
    
    return f"{all[ind][0]} <{all[ind][1]}> {all[ind][2]}"

        






print(findARow("KWIC is an acronym for Key Word In Context, the most common format for concordance lines which is used for indexing in context.", "for in the", "7 15"))
    

