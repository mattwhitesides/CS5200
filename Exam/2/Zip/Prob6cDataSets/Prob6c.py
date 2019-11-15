#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math
import time


# In[8]:


file_name = "Prob6cDataSets\Prob6cDataSet"

def create_txt_files():
    for j in range(10):
        f = open(file_name + str(j) + ".txt","w+")
        for i in range(10000):
            f.write(str(random.randrange(10000)) + ",")
        f.close()

def read_files():
    l = []
    for i in range(10):
        f = open(file_name + str(i) + ".txt","r")
        txt = f.read()
        f.close()
        l.append([int(x) for x in txt.split(',') if x.strip().isdigit()])
    return l


# In[3]:


def heap_sort(A):
    build_min_heap(A, len(A))
    for i in range(len(A) - 1, 0, -1):
        A[1], A[i] = A[i], A[1]
        min_heapify(A, 0)

def build_min_heap(A, n):
    for i in range(parent(n), -1, -1): 
        min_heapify(A, i) 

def min_heapify(A, i):    
    l = left(i)
    r = right(i)
    smallest = i

    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
        
    if r < len(A) and A[r] < A[smallest]:
        smallest = r

    if smallest is not i:
        A[i], A[smallest] = A[smallest], A[i]        
        min_heapify(A, smallest)

def parent(i):
    return int((i / 2)) - 1
        
def left(i):
    return 2 * i + 1

def right(i):
    return (2 * i) + 2


# In[4]:


def build_binomial_heap(A):
    H = make_binomial_heap()
    for a in A:
        H.binomial_heap_insert(a)
    return H

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


# In[11]:


create_txt_files()
A = read_files()
A2 = A.copy()


# In[12]:


def time_binnary_heap():
    for i in range(len(A)):
        heap_sort(A[i])

def time_binomial_heap():
    for i in range(len(A2)):
        build_binomial_heap(A2[i])

start = time.time()
time_binnary_heap()
end = time.time()                   
avg = (end - start) / 10
                   
start = time.time()
time_binomial_heap()
end = time.time()                   
avg2 = (end - start) / 10
    
print("Binary Heap Avg Time:", avg)    
print("Binomial Heap Avg Time", avg2)


# In[ ]:




