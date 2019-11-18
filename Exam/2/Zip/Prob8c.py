#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time


# In[2]:


class BinaryTreeNode: 
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
        
def inorder_traversal_height(T, h = 0): 
    if T: 
        h = inorder_traversal_height(T.left, h + 1)
    return h


# In[3]:


class Node():
    def __init__(self):
        self.leaf = False
        self.keys = []
        self.c    = []

    def __str__(self):
        if self.leaf:
            return "Leaf BTreeNode with {0} keys\n\tK:{1}\n\tC:{2}\n".format(len(self.keys), self.keys, self.c)
        else:
            return "Internal BTreeNode with {0} keys, {1} children\n\tK:{2}\n\n".format(len(self.keys), len(self.c), self.keys, self.c)
        
class BTree():
    def b_tree_create(self, t):
        x = Node()
        x.leaf = True
        self.t = t
        self.root = x
        
    def b_tree_split_child(self, x, i):
        z = Node()
        y = x.c[i]
        z.leaf = y.leaf
        t = self.t
        x.c.insert(i + 1, z)        
        x.keys.insert(i, y.keys[t - 1])  
        
        for j in range(t - 1):
            if len(z.keys) < t - 1:
                z.keys.append(0)
            z.keys[j] = y.keys[j  + t]
        y.keys = y.keys[0: (t - 1)]
        
        if not y.leaf:
            z.keys = y.keys[t: (2*t - 1)]
            y.keys = y.keys[0: (t-1)]

    def b_tree_insert(self, k):
        r = self.root
        if len(r.keys) == (2 * self.t) - 1:
            s = Node()
            self.root = s
            s.c.insert(0, r)
            self.b_tree_split_child(s, 0)  
            self.b_tree_insert_nonfull(s, k)
        else: self.b_tree_insert_nonfull(r, k)
    
    def b_tree_insert_nonfull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf or len(x.c) is 0:
            x.keys.insert(len(x.keys), 0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i = i - 1
            x.keys[i + 1] = k
        else: 
            while i >= 0 and k < x.keys[i]:
                i = i - 1            
            i = i + 1
            if len(x.c[i].keys) == (2 * self.t) - 1:
                self.b_tree_split_child(x, i)
                if k > x.keys[i]:
                    i = i + 1
            self.b_tree_insert_nonfull(x.c[i], k) 
    
    def b_tree_delete(self, k):
        (n, i) = self.find(k)
        if n is None:
            return None
        
        if n.leaf:
            del n.keys[i]
        else:
            k = n.keys[i]
            if len(n.c[i]) >= self.t:
                pred = n.c[i]
                while not curr.leaf:
                    pred = curr.c[len(curr.c) - 1]
                n.keys[i] = pred
                b_tree_delete(pred)
                
            elif len(n.c[i + 1]) >= self.t:
                succ = n.c[i + 1]
                while not curr.leaf:
                    succ = succ.c[0]
                n.keys[i] = succ
                b_tree_delete(succ)
    
    def find(self, k, x = None):
        if isinstance(x, Node):
            i = 0            
            while i < len(x.keys) and k > x.keys[i]:
                i = i + 1
            if i < len(x.keys) and k == x.keys[i]: return (x, i)
            elif x.leaf: return (None, 0)
            else: return self.find(k, x.c[i])
        else: return self.find(k, self.root)
    
    def print_tree(self):
        out = self.root.print_node()
        out += '\n'.join([child.print_node() for child in self.root.c])
        return out        
    
    def height(self):
        r = self.root
        return len(r.c)


# In[4]:


file_name = "Prob8cData"

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


# In[5]:


create_txt_files()
files = read_files()


# In[6]:


binary_tree_root = BinaryTreeNode(5000)
def time_binnary_tree():
    for file in files:
        for i in file:
            tree_insert(binary_tree_root, BinaryTreeNode(i)) 

start = time.time()
time_binnary_tree()
end = time.time()                   
final_time = (end - start)
    
print("Binary Tree Time:", final_time)  
print("Binary Tree Height:", inorder_traversal_height(binary_tree_root))


# In[7]:


b_tree_root = BTree()
b_tree_root.b_tree_create(100)
def time_b_tree():
    for file in files:
        for i in file:
            b_tree_root.b_tree_insert(i)

start = time.time()
time_b_tree()
end = time.time()                   
final_time = (end - start)
    
print("B-Tree Time:", final_time)  
print("B-Tree Height:", b_tree_root.height())


# In[ ]:




