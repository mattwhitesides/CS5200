
# coding: utf-8

# In[1]:


import sys


# In[2]:


class Node():
    def __init__(self, key, left, right, color):
        self.key = key
        self.p = None
        self.left = left
        self.right = right
        self.color = color

class RBTree():
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


# In[3]:


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

