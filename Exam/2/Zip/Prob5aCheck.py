
# coding: utf-8

# In[1]:


import random
import math


# In[2]:


file_name = "Prob5aHeap.txt"

def create_txt_file():
    f = open(file_name,"w+")
    for i in range(10000):
        f.write(str(random.randrange(10000)) + ",")
    f.close()

def read_file():
    f = open(file_name, "r")
    txt = f.read()
    return [int(x) for x in txt.split(',') if x.strip().isdigit()]


# In[3]:


def build_max_heap(A, n):
    for i in range(parent(n), -1, -1): 
        max_heapify(A, i) 

def max_heapify(A, i):    
    l = left(i)
    r = right(i)
    largest = i

    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
        
    if r < len(A) and A[r] > A[largest]:
        largest = r

    if largest is not i:
        A[i], A[largest] = A[largest], A[i]        
        max_heapify(A, largest)

def parent(i):
    return int((i / 2)) - 1
        
def left(i):
    return 2 * i + 1

def right(i):
    return (2 * i) + 2

def is_heap(A, i): 
    if i > parent(i):  
        return True  
    
    if A[i] >= A[left(i)] and A[i] >= A[right(i)]:
        if is_heap(A, left(i)) and is_heap(A, right(i)):
            return True
      
    return False


# In[4]:


create_txt_file()
A = read_file()


# In[5]:


build_max_heap(A, len(A))
is_heap(A, 0)


# In[6]:


f = open(file_name, "a+")
f.write('\r\n\r\nResult:\r\n')
f.write(str(A))
f.close()

