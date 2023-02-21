def strToBin(s):
    # the zero "0"*(8-...) pads the front of the string with zeros so each string is eight characters in length
    return "".join([ "0"*(8-len(bin(ord(i)).replace("0b", ""))) + bin(ord(i)).replace("0b", "") for i in s])

def FindElim(s, elim):
    return s[:str.find(s, elim)]+ s[str.find(s, elim)+len(elim): str.rfind(s,elim)] + s[str.rfind(s,elim)+len(elim):] if elim in s[:str.find(s, elim)]+ s[str.find(s, elim)+len(elim):] else s[:str.find(s, elim)]+ s[str.find(s, elim)+len(elim):]

print(FindElim("11tt111t1", "tt"))