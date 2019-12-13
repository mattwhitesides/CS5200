
# coding: utf-8

# In[1]:


import sys
import time
import statistics


# In[2]:


class Node: 
    def __init__(self, v): 
        self.key = v 
        self.left = None
        self.right = None
                
def tree_insert(T, z): 
    y = None
    x = T
    while x:
        y = x
        if z.key < x.key:
            x = x.left
        else: x = x.right
    if y is None:
        T = z
    elif z.key < y.key:
        y.left = z
    else: y.right = z
                
def inorder_traversal(T): 
    if T: 
        inorder_traversal(T.left) 
        print(T.key, end=", ") 
        inorder_traversal(T.right)
        
def get_height(T):
    return get_height_util(T, 0)

def get_height_util(T, height):
    if T:
        height = get_height_util(T.left, height + 1)
    return height


# In[3]:


data = []

for i in range(10):
    file_name = "Prob4bData{0}.txt".format(str(i))
    with open(file_name) as f:
        data_str = f.readlines()
    data.append([int(x.strip()) for x in data_str])

print(len(data))


# In[4]:


heights = []
times = []

for i in range(10):
    start = time.time()
    
    tree = Node(10000)
    for value in data[i]:
        tree_insert(tree, Node(value))
    
    end = time.time()
    
    heights.append(get_height(tree))
    times.append(end - start)

    
print("BST Heights:", str(heights))
print("BST Times:", str(times))
print("")
print("BST heights Mean:", statistics.mean(heights))
print("BST heights median:", statistics.median(heights))
print("BST heights Standard Dev:", statistics.stdev(heights))
print("")
print("BST Times Mean:", statistics.mean(times))
print("BST Times median:", statistics.median(times))
print("BST Times Standard Dev:", statistics.stdev(times))

