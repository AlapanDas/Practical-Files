class Node:
    def __init__(self, value):
        self.parent = self
        self.children = [self]
        self.value = value

def MakeSet(x):
    return Node(x)

def FindSet_tree(x):
    while x.parent != x:
        x = x.parent
    return x

def Union(x, y):
    xRoot = FindSet_tree
