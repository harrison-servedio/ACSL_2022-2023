def strToBin(s):
    return "".join([ "0"*(8-len(bin(ord(i)).replace("0b", ""))) + bin(ord(i)).replace("0b", "") for i in s])

# Assumes there is at least one occurence otherwise this functions should be run
def FindElim(s, elim):
    # Gets lenths to know where the splice from
    legth = len(elim)

    ind = str.find(s, elim)

    s = s[:ind]+s[ind+legth:]

    # Reverses the two lists
    s = s[::-1]
    elim = elim[::-1]

    # Checks to see if should look from the back
    if elim in s:
        ind = str.find(s, elim)
        s = s[:ind]+s[ind+legth:]

    s = s[::-1]
    return s

def findLastOctal(s):
    binaryString = strToBin(s)

    counter = 0
    binary_counter = bin(counter).replace("0b", "")
    while binary_counter in binaryString:
        binaryString = FindElim(binaryString, binary_counter)
        counter += 1
        binary_counter = bin(counter).replace("0b", "")

    octalString = oct(int(binaryString, 2)).replace("0o", "")
    
    counter = 0
    octal_counter = oct(counter).replace("0o", "")
    if octal_counter not in octalString:
        return -1
    
    while octal_counter in octalString:
        octalString = FindElim(octalString, octal_counter)
        counter += 1
        octal_counter = oct(counter).replace("0o", "")

    return int(octal_counter, 8) - 1


print(findLastOctal("Roses are red."))