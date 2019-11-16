#!/usr/bin/env python
# coding: utf-8

# In[6]:


def G(n):
    if n == 0:
        return 5
    elif n == 1:
        return 15
    elif n == 2:
        return 40    
    elif n > 2:
        return G(n - 1) + G(n - 2) + G(n - 3)
    
def G2(n, lookup = {}):
    if n == 0:
        return 5
    elif n == 1:
        return 15
    elif n == 2:
        return 40    
    elif n > 2:
        if n not in lookup:
            lookup[n] = G2(n - 1, lookup) + G2(n - 2, lookup) + G2(n - 3, lookup)            
        return lookup[n]


# In[16]:


print(G(20))
print(G2(20))


# In[17]:


print(G2(500))


# In[ ]:




