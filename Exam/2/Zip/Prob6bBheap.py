#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math


# In[33]:


def make_binomial_heap():
    return BinomialHeap()

class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.degree = 0

    def leftmost_child(self, t):
        self.children.append(t)
        self.degree = self.degree + 1

class BinomialHeap:
    def __init__(self):
        self.head = []

    def binomial_heap_minimum(self):
        if self.head == []:
            return None
        
        y = None
        x = self.head
        min = x[0].key

        for tree in x:
            if tree.key < min:
                min = tree.key                
        
        return min

    def binomial_link(self, n, y, z):
        n.leftmost_child(y)
        del self.head[z]        

    def binomial_heap_union(self, h):
        self.binomial_heap_merge(h)
        
        if self.head == []:
            return
        
        i = 0
        while i < len(self.head) - 1:
            prev = self.head[i]
            next = self.head[i + 1]

            if prev.degree == next.degree:
                if len(self.head) - 1 > i + 1 and self.head[i + 2].degree == next.degree:                    
                    next_x = self.head[i + 2]
                    
                    if next.key < next_x.key:
                        self.binomial_link(next, next_x, i + 2)
                    else:
                        self.binomial_link(next_x, next, i + 1)
                else:
                    if prev.key < next.key:
                        self.binomial_link(prev, next, i + 1)
                    else:
                        self.binomial_link(next, prev, i)            
            i += 1

    def binomial_heap_merge(self, h):
        self.head.extend(h.head)
        self.head.sort(key=lambda tree: tree.degree)

    def binomial_heap_insert(self, key):
        h = make_binomial_heap()
        h.head.append(BinomialTree(key))
        self.binomial_heap_union(h)        

    def binomial_heap_extract_min(self):
        if self.head == []:
            return None

        x = self.head[0]
        
        for tree in self.head:
            if tree.key < x.key:
                x = tree
        
        self.head.remove(x)
        
        h = make_binomial_heap()
        h.head = x.children
        self.binomial_heap_union(h)

        return x.key


# In[47]:


A = [11, 1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
H = make_binomial_heap()

for a in A:
    H.binomial_heap_insert(a)
    
print('Min:', H.binomial_heap_minimum())
print('Head:', H.head[0].key)
print('Head Children:', [child.key for child in H.head[1:]])


# In[ ]:




