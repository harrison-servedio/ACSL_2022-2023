def strToBin(s):
    # the zero "0"*(8-...) pads the front of the string with zeros so each string is eight characters in length
    return "".join([ "0"*(8-len(bin(ord(i)).replace("0b", ""))) + bin(ord(i)).replace("0b", "") for i in s])

def FindElim(s, elim):
    # Some simple string splicing forced all on one line that makes it seem complicated
    return s[:str.find(s, elim)]+ s[str.find(s, elim)+len(elim): str.rfind(s,elim)] + s[str.rfind(s,elim)+len(elim):] if elim in s[:str.find(s, elim)]+ s[str.find(s, elim)+len(elim):] else s[:str.find(s, elim)]+ s[str.find(s, elim)+len(elim):]


def findLastOctal(s):
    binaryString = strToBin(s)

    counter = 0
    binary_counter = bin(counter).replace("0b", "")
    
    while binary_counter in binaryString: binaryString = FindElim(binaryString, binary_counter); counter += 1;binary_counter = bin(counter).replace("0b", "")

    octalString = oct(int(binaryString, 2)).replace("0o", "")
    
    counter = 0
    octal_counter = oct(counter).replace("0o", "")
    
    while octal_counter in octalString: octalString = FindElim(octalString, octal_counter); counter += 1; octal_counter = oct(counter).replace("0o", "")

    # This could just be: return counter-1 but this also works and again, can't retest so will never know for sure
    return counter - 1



print(findLastOctal("Test are red."))