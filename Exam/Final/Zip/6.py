#!/usr/bin/env python
# coding: utf-8

# In[27]:


def gcd(p, q):
    p = format(p, 'b')
    q = format(q, 'b')
    result = gcd_util(p, q)
    return int(result, 2)

def gcd_util(p, q):
    # Base Cases
    if p == q:
        return p

    if is_zero(p):
        return p

    if is_zero(q):
        return q

    # Proof 6a: If p is even divide by two.
    if is_even(p):
        if is_even(q):
            return shift_left(gcd_util(shift_right(p), shift_right(q)))
        else:
            return gcd_util(shift_right(p), q)

    # Proof 6b: If p is odd and q is even.
    if (is_even(q)):
        return gcd_util(p, shift_right(q))

    # Proof 6c: If p and q are both odd and p > q.
    if is_greater(p, q):
        return gcd_util(shift_right(minus(p, q)), q)

    return gcd_util(shift_right(minus(q, p)), p)

def is_zero(s):
    return s == len(s) * '0'

def is_even(s):
    return s[len(s) - 1] == '0'

# Multiply by two, by adding a zero to the end.
def shift_left(s):
    return s + '0'

# Divide by two, by removing the last char.
def shift_right(s):
    return s[: -1]

def is_greater(x, y):
    if len(x) > len(y):
        return True
    return int(x, 2) > int(y, 2)

def minus(x, y):
    return format(int(x, 2) - int(y, 2), 'b')


# In[28]:


import math
import random


# In[34]:


rand_nums = [(random.randrange(0, 10000000), random.randrange(0, 10000000)) for i in range(100)]

for n in rand_nums:
    my_gcd = gcd(n[0], n[1])
    math_gcd = math.gcd(n[0], n[1])
    valid = my_gcd == math_gcd
    s = "GCD({},{}) = {}: Valid = {}".format(str(n[0]), str(n[1]), str(my_gcd), str(valid))
    print(s)

