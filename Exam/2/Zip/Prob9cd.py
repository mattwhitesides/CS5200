#!/usr/bin/env python
# coding: utf-8

# In[1]:


import collections
import math
from math import sqrt


# In[2]:


out_file = "Prob9GraphDataOut.txt"    
graph_data = [line.rstrip('\n').rstrip(')').lstrip('(') for line in open('GraphData.txt')]


# In[3]:


class Graph:    
    graph_dict = {}
    adj = []
    num_edges = 0
    path_str = ""
    euler_edge_count = 0

    def add_edge(self, vert, connected_vert):  
        if vert not in self.graph_dict:
            self.graph_dict[vert] = [connected_vert]
        else:
            self.num_edges += 1
            self.graph_dict[vert].append(connected_vert)
            
        if connected_vert not in self.graph_dict:
            self.graph_dict[connected_vert] = [vert]
        else:
            self.graph_dict[connected_vert].append(vert)            

    def print_graph_dict(self):
        print(self.graph_dict)

    def get_num_verts(self):
        return len(self.graph_dict)
    
    def get_num_edges(self):
        return self.num_edges
    
    def sort_dict(self):
        self.adj = collections.OrderedDict(sorted(self.graph_dict.items()))
        for key in self.adj:
            self.adj[key].sort()
    
    def get_adj_list(self):
        self.sort_dict();
        s = ''
        for key in self.adj:
            x = ''
            for value in self.adj[key]:
                x += '{0},'.format(value)
            s += "{0},{1}\n".format(key, x).replace(',\n', '\n')
        return s + '\n'        
    
    def DFS(self, temp, vert, visited): 
        visited[vert] = True
        temp.append(vert) 
        for i in self.adj[vert]: 
            if visited[i] == False:                   
                temp = self.DFS(temp, i, visited) 
        return temp 
                
    def get_connected_comp(self):
        self.sort_dict();
        visited = [] 
        cc = [] 
        for i in range(list(self.adj.items())[-1][0] + 1):
            visited.append(False) 
        for v in self.adj: 
            if visited[v] == False: 
                cc.append(self.DFS([], v, visited)) 
        return cc
    
    def get_euler_comp(self, is_circuit):        
        cc = self.get_connected_comp()
        ec = []
        for c in cc:
            is_euler_check = self.is_euler(c)
            if is_euler_check == 2 and is_circuit:
                ec.append(c)        
            elif is_euler_check == 1 and not is_circuit:
                ec.append(c)
        return ec
        
    def is_euler(self, c):        
        is_odd = 0
        for i in c:            
            if len(self.graph_dict[i]) % 2 is not 0:                 
                is_odd += 1
        # Is Euler Circuit
        if is_odd == 0:
            return 2
        # Is Euler Path
        elif is_odd == 2:
            return 1
        # Not Euler
        elif is_odd > 2:
            return 0
    
    def print_euler_comp_list(self, is_circuit):
        out = ""
        ec = self.get_euler_comp(is_circuit)  
        for i in range(len(ec)):
            self.path_str = ""
            self.euler_edge_count = 0
            self.get_euler_path(ec[i][0])
            f = "\nThe following {} lines list the edges for an Euler {} in the Component {}.\n\n"            
            out += f.format(self.euler_edge_count, "circuit" if is_circuit else "path", i + 1)
            out += self.path_str
        return out
                
    def is_valid_next_edge(self, x, y): 
        if len(self.graph_dict[x]) == 1: 
            return True
        else:   
            is_visited = [False] * (100000) 
            first_v_count = self.DFS_Count(x, is_visited) 
            
            self.delete_edge(x, y)

            is_visited = [False] * (100000) 
            connected_v_count = self.DFS_Count(x, is_visited) 

            self.add_edge(x,y) 

            if first_v_count > connected_v_count:
                return False
            return True

    def get_euler_path(self, x):
        for y in self.graph_dict[x]: 
            if self.is_valid_next_edge(x, y): 
                self.path_str += "{},{}\n".format(x, y)
                self.euler_edge_count += 1
                self.delete_edge(x, y) 
                self.get_euler_path(y)
                
    def delete_edge(self, x, y): 
        for index, key in enumerate(self.graph_dict[x]): 
            if key == y: 
                self.graph_dict[x].pop(index) 
        for index, key in enumerate(self.graph_dict[y]): 
            if key == x: 
                self.graph_dict[y].pop(index) 
                
    def DFS_Count(self, y, is_visited): 
        count = 1
        is_visited[y] = True
        for i in self.graph_dict[y]:
            if is_visited[i] == False: 
                count = count + self.DFS_Count(i, is_visited)          
        return count              
    
    def print_components_list(self):
        cc = self.get_connected_comp()        
        s = 'The number of connected components of the graph is {0}.\n'.format(len(cc))
        for c in cc:
            if len(c) > 0:
                c.sort()
                s += str(c[0]) + ', '
                s += str(len(c)) + ', '
                
                e = 0
                for i in range(len(c)):
                    for j in c[i:]:
                        if c[i] in self.graph_dict[j]:
                            e += 1
                            
                s += str(e)
                s += ' \n'
        return s


# In[4]:


out_txt = ""
g = Graph()

for line in graph_data:
    split = line.split(',')
    if len(split) == 2:
        g.add_edge(int(split[0]), int(split[1]))


# In[5]:


ec = g.get_euler_comp(True)
f = "\nThe number of connected components of the graph that have an Euler circuit is {}.\n\n"
out_txt = f.format(len(ec))
out_txt += g.print_euler_comp_list(True)
print(out_txt)


# In[6]:


file_out = open(out_file, "a+")
file_out.write(out_txt)
file_out.close()

