#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

file_name = "Data10.txt"
rn = [random.randint(1,10000) for i in range(1000)]
f = open(file_name, "w+")

for r in rn: 
    f.write(str(r) + "\n")

f.close()


# In[ ]:




