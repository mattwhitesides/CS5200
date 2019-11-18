#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[22]:


class Node(object):
    def __init__(self):
        self.leaf = False
        self.keys = []
        self.c    = []
        
    def print_node(self):
        if self.leaf:
            return "Leaf node:{}".format(self.keys)
        return "Node: {}\nChildren: {}\n".format(self.keys, [child.print_node() for child in self.c])

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


# In[24]:


A = [15, 68, 25, 8, 41, 23, 96, 3, 89, 53, 31, 92, 83, 30, 16, 51, 76, 88, 70, 90]
root = BTree()
root.b_tree_create(5)


T = root
for a in A:
    T.b_tree_insert(a)

print(root.print_tree())
    
T.b_tree_delete(15)

print(root.print_tree())


# In[25]:


A = [random.randint(0,100) for i in range(25)]
root = BTree()
root.b_tree_create(5)

T = root
for a in A:
    T.b_tree_insert(a)
    
print(root.print_tree())

