#!/usr/bin/env python
# coding: utf-8

# In[19]:


import sys
import time
import statistics


# In[11]:


class Node():
    """
    Class to contain a Red Black Tree Graph Bode properties.
    Specifically the key, p value, left, right and color. 
    """
    def __init__(self, key, left, right, color):
        self.key = key
        self.p = None
        self.left = left
        self.right = right
        self.color = color

class RBTree():
    """
    Class to contain a Red Black Tree Graph
    and preform insert and printing functionality.
    """
    def __init__(self):
        self.NIL = Node(0, None, None, "BLACK")
        self.root = self.NIL
        
    def print_tree(self):
        self.print_util(self.root, "", True)

    def print_util(self, node, tab, rightmost):
        if node != self.NIL:
            print(tab, end = "")            
            
            if rightmost:
                print("Right:", end = "")
            else:
                print("Left:", end = "")
            tab += "  "
                
            print("(" + str(node.key), node.color + ")")
            
            self.print_util(node.left, tab, False)
            self.print_util(node.right, tab, True)
    
    def get_height(self):
        return self.get_height_util(self.root, 0)
    
    def get_height_util(self, node, height):
        if node != self.NIL:
            height = self.get_height_util(node.right, height + 1)
        return height
        
    def rb_insert(self, z):
        """
        Inserts a new node with the value of z into this class instance's RB Tree.
        Uses the algorithm layed out in the book on p.315
        ----------
        Parameters
            z : int
                The value to insert into the tree.
        """
        z = Node(z, self.NIL, self.NIL, "RED")

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        if z.p == None:
            z.color = "BLACK"
            return

        if z.p.p == None:
            return

        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        """
        Preforms a "fixup" on the classes RBTree fixup implements the following logic.        
        If z is a root, color it black.
        If z's parent is red, then z's grandparent must be black.
        Let y be z's grandparent's other child.
        Fix depends on whether y is red or black.
        ----------
        Parameters
            z : Node
                The node to be "fixed".
        """
        while z.p.color == "RED":
            if z.p == z.p.p.right:
                u = z.p.p.left
                if u.color == "RED":
                    u.color = "BLACK"
                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)

                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    self.left_rotate(z.p.p)
            else:
                u = z.p.p.right

                if u.color == "RED":
                    u.color = "BLACK"
                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)

                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    self.right_rotate(z.p.p)

            if z == self.root:
                break

        self.root.color = "BLACK"

    def right_rotate(self, x):
        """
        Rotates the given node in a clockwise direction
        up the tree and adjests its siblings.
        ----------
        Parameters
            x : Node
                The node to be rotated.
        """        
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.p = x

        y.p = x.p
        if x.p == None:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y

        y.right = x
        x.p = y

    def left_rotate(self, x):
        """
        Rotates the given node in a counter-clockwise direction
        down the tree and adjests its siblings.
        ----------
        Parameters
            x : Node
                The node to be rotated.
        """           
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.p = x

        y.p = x.p
        if x.p == None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y


# In[21]:


tree = RBTree()
tree.rb_insert(7)
tree.rb_insert(4)
tree.rb_insert(11)
tree.rb_insert(3)
tree.rb_insert(6)
tree.rb_insert(9)
tree.rb_insert(18)
tree.rb_insert(2)
tree.rb_insert(14)
tree.rb_insert(19)
tree.rb_insert(12)
tree.rb_insert(17)
tree.rb_insert(22)
tree.rb_insert(20)

print("RBTree Height:", tree.get_height())
tree.print_tree()


# In[3]:


import random

for i in range(10):
    file_name = "Prob4bData{0}.txt".format(str(i))
    rn = [random.randint(1,10000) for i in range(10000)]
    f = open(file_name, "w+")
    for r in rn: 
        f.write(str(r) + "\n")

f.close()

data = []

for i in range(10):
    file_name = "Prob4bData{0}.txt".format(str(i))
    with open(file_name) as f:
        data_str = f.readlines()
    data.append([int(x.strip()) for x in data_str])

print(len(data))


# In[8]:


data = []

for i in range(10):
    file_name = "Data{0}.txt".format(str(i))
    with open(file_name) as f:
        data_str = f.readlines()
    data.append([int(x.strip()) for x in data_str])

print(len(data))


# In[20]:


heights = []
times = []

for i in range(10):
    start = time.time()
    
    tree = RBTree()
    for value in data[i]:
        tree.rb_insert(value)
    
    end = time.time()
    
    heights.append(tree.get_height())
    times.append(end - start)

    
print("RBTrees Heights:", str(heights))
print("RBTrees Times:", str(times))
print("")
print("RBTrees heights Mean:", statistics.mean(heights))
print("RBTrees heights median:", statistics.median(heights))
print("RBTrees heights Standard Dev:", statistics.stdev(heights))
print("")
print("RBTrees Times Mean:", statistics.mean(times))
print("RBTrees Times median:", statistics.median(times))
print("RBTrees Times Standard Dev:", statistics.stdev(times))


# In[ ]:




