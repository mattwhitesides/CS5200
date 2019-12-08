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

    def pretty_print(self):
        self.__print_helper(self.root, "", True)

    def __print_helper(self, node, indent, last):
        if node != self.NIL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == "RED" else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)