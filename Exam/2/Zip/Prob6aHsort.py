#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math


# In[8]:


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


# In[9]:


A = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

heap_sort(A)

print(A)


# In[ ]:




