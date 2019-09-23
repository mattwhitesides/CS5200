#!/usr/bin/env python
# coding: utf-8

# In[258]:


import collections


# In[259]:


class Graph:    
    graph_dict = {}
    adj = []
    num_edges = 0

    def addEdge(self, vert, connected_vert):  
        if vert not in self.graph_dict:
            self.graph_dict[vert] = [connected_vert]
        else:
            self.num_edges += 1
            self.graph_dict[vert].append(connected_vert)
            
        if connected_vert not in self.graph_dict:
            self.graph_dict[connected_vert] = [vert]
        else:
            self.graph_dict[connected_vert].append(vert)            

    def printGraphDict(self):
        print(self.graph_dict)

    def getNumVerts(self):
        return len(self.graph_dict)
    
    def getNumEdges(self):
        return self.num_edges
    
    def sortDict(self):
        self.adj = collections.OrderedDict(sorted(self.graph_dict.items()))
        for key in self.adj:
            self.adj[key].sort()
    
    def getAdjList(self):
        self.sortDict();
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
                
    def getConnectedComp(self):
        visited = [] 
        cc = [] 
        for i in range(list(self.adj.items())[-1][0] + 1):
            visited.append(False) 
        for v in self.adj: 
            if visited[v] == False: 
                cc.append(self.DFS([], v, visited)) 
        return cc
    
    def printCCList(self):        
        cc = self.getConnectedComp()        
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
            
    
graph_data = [line.rstrip('\n').rstrip(')').lstrip('(') for line in open('GraphData.txt')]

g = Graph()

for line in graph_data:
    split = line.split(',')
    if len(split) == 2:
        g.addEdge(int(split[0]), int(split[1]))


# In[260]:


f = open('GraphDataOut.txt','w+')


# In[261]:


s = "The number of vertices in the graph is {0}.\n\n".format(g.getNumVerts())
f.write(s)
print(s)


# In[262]:


s = "The number of edges in the graph is {0}.\n\n".format(g.getNumEdges())
f.write(s)
print(s)


# In[263]:


s = "Below is the adjacency list for this graph with the verrtices sorted.\n"
f.write(s)
print(s)


# In[264]:


s = g.getAdjList()
f.write(s)
print('Printing getAdjList().\n')


# In[265]:


s = g.printCCList()
f.write(s)
print('Printing getCCList().\n')


# In[266]:


f.close()

