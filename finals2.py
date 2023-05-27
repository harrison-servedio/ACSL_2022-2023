class node():
    def __init__(self, value, depth=0) -> None:
        self.left = None
        self.right = None
        self.value = value
        self.data = value
        self.depth = depth
    
    def putIn(self, value, depth=0):
        depth = depth + 1
        if value > self.value:
            if self.right == None:
                self.right = node(value, depth=depth)
            else:
                self.right.putIn(value, depth=depth)
        else:
            if self.left == None:
                self.left = node(value, depth=depth)
            else:
                self.left.putIn(value, depth=depth)
    
    def traverse(self):
        t = self.traverserStarter()
        if self.left:
            t += self.left.traverse()
        if self.right:
            t += self.right.traverse()
        return sorted(t)

    def traverserStarter(self):
        
        if self.left:
            leftP = self.left.traverseHelp(0)
        if self.right:
            rightP = self.right.traverseHelp(0)
        
        if self.left and self.right:
            total = leftP + rightP
            for i in leftP:
                for j in rightP:
                    total.append(i+j)
        elif self.left:
            total = leftP
        elif self.right:
            total = rightP
        else:
            total = []
        total = [i + self.data for i in total]
        return sorted(total)
        
    def traverseHelp(self, current=0):
        t = [self.data + current]
        current = current + self.data
        if self.left:
            t += self.left.traverseHelp(current)
        if self.right:
            t += self.right.traverseHelp(current)
        return t
    
    

def countUniqueSums(inputString):
    # Write your code here
    inputString = [int(i) for i in list(inputString)]
    root = node(inputString[0])
    for i in inputString[1::]:
        root.putIn(i)
    # print(root.left.traverserStarter())
    return len(list(set(root.traverse())))
    


countUniqueSums("31415926")
