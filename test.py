import re
s = "adv physics"
print(re.findall("[^e][a-hlr-y]*[\s]*[a-n]*[^mr]*[\S]*[0-9]*", s))