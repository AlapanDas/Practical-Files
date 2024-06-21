class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0

def MakeSet(x):
    return Node(x)

def FindSet_ranked(x):
    while x.parent != x:
        x.parent = x.parent.parent
        x = x.parent
    return x

def Union_ranked(x, y):
    xRoot = FindSet_ranked(x)
    yRoot = FindSet_ranked(y)
    if xRoot == yRoot:
        return
    if xRoot.rank < yRoot.rank:
        xRoot.parent = yRoot
    elif xRoot.rank > yRoot.rank:
        yRoot.parent = xRoot
    else:
        yRoot.parent = xRoot
        xRoot.rank += 1
