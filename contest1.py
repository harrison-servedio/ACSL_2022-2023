
# Here I attemped to solve the problem in as few lines as possible
# I was able to shorten everything down to two lines but because I used recursion to convert numbers to different bases I was unable to shorten it further
convertToBase = lambda num, base : list("0123456789ABCDEF")[num] if num < base else convertToBase(int(num/base), base) + list("0123456789ABCDEF")[num%base]
def findModeCount(num, base, start): return max(["".join([convertToBase(i, base) for i in range(int(str(start), base), int(str(start), base)+num)]).count(i) for i in list("0123456789ABCDEF")])

print(findModeCount(15,8,2))


# This is my actual solution
# Counter is a library built into python that counts the frequency of characters in a string
from collections import Counter
# These digits are the digits 
digs = list("0123456789ABCDEF")

def convertToBase(num, base):
    if num < base:
        return digs[num]
    return convertToBase(num//base, base) + digs[num%base]

def findModeCount(num, base, start):
    nums = "".join([convertToBase(i, base) for i in range(int(str(start), base), int(str(start), base)+num)])
    return max(list(Counter(nums).values()))

print(findModeCount(15,8,2))
