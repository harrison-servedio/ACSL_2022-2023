def strToBin(s):
    # the zero "0"*(8-...) pads the front of the string with zeros so each string is eight characters in length
    return "".join([ "0"*(8-len(bin(ord(i)).replace("0b", ""))) + bin(ord(i)).replace("0b", "") for i in s])

# Assumes there is at least one occurence otherwise this functions should be run
def FindElim(s, elim):
    # Gets lenths to know where the splice from
    legth = len(elim)

    # Find function finds the first occurence of a string in another string
    ind = str.find(s, elim)

    # Uses string indexes to splice the string into to piece around the string that had to be removes and then adds them together
    s = s[:ind]+s[ind+legth:]

    # Reverses the two lists because then looking from the front would be from the back
    s = s[::-1]
    elim = elim[::-1]

    # Checks to see if should look from the back 
    if elim in s:
        ind = str.find(s, elim)
        s = s[:ind]+s[ind+legth:]

    # Un-reverses the string to the original order so it doesn't mess up the program
    return s[::-1]

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

    # I really don't think this is needed but I have no ways of retesting so I'm keeping it
    if octal_counter not in octalString:
        return -1
    
    while octal_counter in octalString:
        octalString = FindElim(octalString, octal_counter)
        counter += 1
        octal_counter = oct(counter).replace("0o", "")

    # This could just be: return counter-1 but this also works and again, can't retest so will never know for sure
    return int(octal_counter, 8) - 1


print(findLastOctal("Test are red."))
