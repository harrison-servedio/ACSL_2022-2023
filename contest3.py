# I originally started trying to hardcode everything but then realized like an idiot that the problem is just asking you
# to create a tree traversal. Both strings that the question requires you to create are just a simple traversal of a bst
# with the only different being that one appends to the string as soon as the node is reached and the other appends as soon
# as the node is left for good
class node():
    def __init__(self, value, depth=0) -> None:
        self.left = None
        self.right = None
        self.value = value
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
    
    def traverse(self, out="", out2=""):
        out += self.value

        if self.left:
            out, out2 = self.left.traverse(out, out2)
        
        if self.right:
            out, out2 = self.right.traverse(out, out2)

        out2 += self.value
        return (out, out2)


def getTraversals(input):
    # Write your code here
    x = node(input[0])
    for i in list(input)[1::]:
        x.putIn(i)
    a, b = x.traverse()
    return f"{a} {b}"

print(getTraversals(input()))