#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[4]:


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


# In[5]:


root = Node(50)

rn = []
for i in range(10):
    rn.append(random.randrange(100))
    
for i in range(10):
    tree_insert(root, Node(rn[i]))    
    
inorder_traversal(root)


# In[ ]:




