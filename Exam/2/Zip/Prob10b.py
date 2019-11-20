#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

file_name = "Data10.txt"
out_file_name = "OptMult10.txt"

with open(file_name) as f:
    data = f.readlines()
data = [int(x.strip()) for x in data]
print(len(data))


# In[2]:


def matrix_chain_order(p, n):
    m = [[0 for i in range(n)] for i in range(n)] 
    
    for l in range(2, n + 1):
        for i in range(n - l + 1): 
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j): 
                q = (m[i][k] + m[k + 1][j] + (p[i] * p[k + 1] * p[j + 1])); 
                if (q < m[i][j]): 
                    m[i][j] = q 
                    m[j][i] = k + 1
    return m

def clean_out_str():
    global out_lst
    for i in range(len(out_lst)):
        out_lst[i] = out_lst[i].replace(',]', ']')
        out_lst[i] = out_lst[i].replace(',[', '[')
        diff = out_lst[i].count('[') - out_lst[i].count(']')        
        if diff > 0:
            out_lst[i] = out_lst[i][diff:]
        elif diff < 0:
            out_lst[i] = out_lst[i][:len(out_lst[i]) - (diff * -1)]
        

def get_brackets(m, j, i):
    global out_str
    if j == i: 
        out_str += str(j + 1) + ','        
        return;
    else: 
        out_str += "["
        get_brackets(m, m[j][i] - 1, i) 
        get_brackets(m, j, m[j][i])
        out_str += "]"
        temp_str = out_str 
        out_lst.append(out_str)


# In[3]:


out_str = ""
out_lst = []
test_data = [1, 3, 9, 12, 10, 9, 13, 7, 2]
n = len(test_data) - 1
m = matrix_chain_order(test_data, n)

print("Number of multiplications:", str(len(m)))

get_brackets(m, n - 1, 0)
clean_out_str()

for s in reversed(out_lst):
    print(s)


# In[4]:


out_str = ""
out_lst = []
n = len(data) - 1
m = matrix_chain_order(data, n)

print("Number of multiplications:", str(len(m)))

get_brackets(m, n - 1, 0)
clean_out_str()

f = open(out_file_name, "w+")
for s in reversed(out_lst):
    f.write(s)
    f.write('\n\n')
f.close()


for s in reversed(out_lst):
    print(s)

