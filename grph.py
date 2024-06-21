import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0
        self.size = 1

class LinkedListDisjointSet:
    def __init__(self):
        self.num_comparisons = 0
    
    def MakeSet(self, x):
        return Node(x)
    
    def FindSet(self, x):
        self.num_comparisons = 0
        while x.parent != x:
            x = x.parent
            self.num_comparisons += 1
        return x
    
    def Union(self, x, y):
        x.parent = y

class RankedLinkedListDisjointSet:
    def __init__(self):
        self.num_comparisons = 0
    
    def MakeSet(self, x):
        return Node(x)
    
    def FindSet(self, x):
        self.num_comparisons = 0
        while x.parent != x:
            x = x.parent
            self.num_comparisons += 1
        return x
    
    def Union(self, x, y):
        x_root = self.FindSet(x)
        y_root = self.FindSet(y)
        if x_root == y_root:
            return
        self.num_comparisons += 1
        if x_root.rank < y_root.rank:
            x_root.parent = y_root
            y_root.size += x_root.size
        elif x_root.rank > y_root.rank:
            y_root.parent = x_root
            x_root.size += y_root.size
        else:
            y_root.parent = x_root
            x_root.rank += 1
            x_root.size += y_root.size

class TreeDisjointSet:
    def __init__(self):
        self.num_comparisons = 0
    
    def MakeSet(self, x):
        return Node(x)
    
    def FindSet(self, x):
        self.num_comparisons = 0
        if x.parent != x:
            x.parent = self.FindSet(x.parent)
            self.num_comparisons += 1
        return x.parent
    
    def Union(self, x, y):
        x_root = self.FindSet(x)
        y_root = self.FindSet(y)
        if x_root == y_root:
            return
        self.num_comparisons += 1
        if x_root.rank < y_root.rank:
            x_root.parent = y_root
        elif x_root.rank > y_root.rank:
            y_root.parent = x_root
        else:
            y_root.parent = x_root
            x_root.rank += 1

def count_comparisons(n, m, implementation):
    sets = [implementation.MakeSet(i) for i in range(n)]
    comparisons = 0
    for i in range(m):
        if i < n:
            implementation.MakeSet(i)
        else:
            x = np.random.randint(0, n)
            y = np.random.randint(0, n)
            if np.random.random() < 0.5:
                implementation.Union(sets[x], sets[y])
            else:
                implementation.FindSet(sets[x])
                implementation.FindSet(sets[y])
            comparisons += implementation.num_comparisons
    return comparisons

m_values = [200, 300, 500, 1000, 1200, 1500, 1800, 2000, 2400, 2800, 3000]

linked_list_comparisons = []
ranked_linked_list_comparisons = []
tree_comparisons = []
for m in m_values:
    linked_list_comparisons.append(count_comparisons(100, m, LinkedListDisjointSet()))
    ranked_linked_list_comparisons.append(count_comparisons(100, m, RankedLinkedListDisjointSet()))
    tree_comparisons.append(count_comparisons(100, m, TreeDisjointSet()))

plt.plot(m_values, linked_list_comparisons, label='Linked List')
plt.plot(m_values, ranked_linked_list_comparisons, label='Ranked Linked List')
plt.plot(m_values, tree_comparisons, label='Tree')
plt.xlabel('m')
plt.ylabel('Number of Comparisons')
plt.title('Comparisons vs m')
plt.legend()
plt.show()