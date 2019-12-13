#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


txt_data = [line.rstrip('\n').rstrip(')').lstrip('(') for line in open('GraphData.txt')]
graph_data = []

# Put graph data into a array of tuples.
for line in txt_data:
    split = line.split(',')
    if len(split) == 2:
        x = int(split[0])
        y = int(split[1])
        graph_data.append((x, y, abs(x - y)))


# In[3]:


class Forest():
    """
    Class to take in an unconnected list of tuples containing (vert1, vert2, weight) data.
    Split it into individual connected components.
    Convert the node labels into integers (0 ... n).
    Create an adjacency list for graph.
    Do the same for each found subgraph in the data.
    """
    def __init__(self, graph_data):
        """
        Initializes a new instance of the Forest class
        ----------
        Parameters
            graph_data : [(int, int, int)]
                The graph data to build the dict off of.
        """          
        self.graph_data = graph_data

        dicts = self.build_graph_dict(self.graph_data)        
        self.graph_dict = dicts[0]
        self.graph_dict_rev = dicts[1]                
        
        self.V = len(self.graph_dict)
        
        self.graph = self.build_adj_list(self.graph_data, self.graph_dict, self.V)
        self.cc = self.get_connected_components()
        
        self.forest_dicts = []
        self.forest = []
        self.forest_data = []
        self.build_connected_forest()

        print("Forest Info:")
        print("\tNumber of vertices:", str(self.V))
        print("\tNumber of edges:", len(self.graph_data))
        print("\tNumber of connected components in forest:", len(self.cc))
        
        for i in range(len(self.forest)):
            print("\t\tSubgraph {0}: ".format(i))
            print("\t\t\t# vertices:", len(self.forest_dicts[i][0]))            
            print("\t\t\t# edges:", len(self.forest_data[i]))            
        
    def build_graph_dict(self, graph_data):
        """
        Builds a dictionary containing the labels in the graph.
        ----------
        Parameters
            graph_data : [(int, int, int)]
                The graph data to build the dict off of.
        """        
        graph_dict = {}
        graph_dict_rev = {}
        i = 0

        for x in graph_data:
            if x[0] not in graph_dict:
                graph_dict[x[0]] = i
                graph_dict_rev[i] = x[0]
                i += 1
            if x[1] not in graph_dict:
                graph_dict[x[1]] = i
                graph_dict_rev[i] = x[1]
                i += 1

        return (graph_dict, graph_dict_rev)
        
    def build_adj_list(self, graph_data, graph_dict, length):
        """
        Builds an adjacency list of the given graph data.
        ----------
        Parameters
            graph_data : [(int, int, int)]
                The graph data to build the adj list off of.
            graph_dict : {}
                The graph data's dict.
            length : int
                The number of nodes in the graph.
        """          
        graph = [[(0, 0) for i in range(length)] for j in range(length)]

        for d in graph_data:
            x = graph_dict[d[0]]
            y = graph_dict[d[1]]
            graph[x][y] = (y, d[2])
            graph[y][x] = (x, d[2])
        
        return graph
            
    def build_connected_forest(self):
        """
        Builds an array of graphs from the separate components
        in the class's total graph data.
        """                  
        for c in self.cc:
            graph_data = []
            for x in c:
                for edge in self.find_edges(x):
                    if not self.edge_in_edges(edge, graph_data):
                        graph_data.append(edge)   

            d = self.build_graph_dict(graph_data)
            adj = self.build_adj_list(graph_data, d[0], len(d[0]))
            
            self.forest_dicts.append(d)
            self.forest_data.append(graph_data)
            self.forest.append(adj)
                
    def find_edges(self, v):
        """
        Gets the edges matching the given vertex from the graph data.
        ----------
        Parameters
            v : int
                The requested vertex.
        """                  
        edges = []
        for edge in self.graph_data:
            if edge[0] == self.graph_dict_rev[v] or edge[1] == self.graph_dict_rev[v]:
                edges.append(edge)

        return edges
    
    def edge_in_edges(self, edge, edges):
        """
        Checks if an edge already exists in the edges list.
        ----------
        Parameters
            edge : (int, int)
                The requested edge.
            edge : [(int, int)]
                The list of edges.
        """          
        for e in edges:
            if edge[0] == e[0] and edge[1] == e[1]:
                return True

        return False
            
    def print_cc_list(self):
        """
        Prints out the separate componets from the forest.
        """          
        i = 0
        for cc in self.forest_data:
            print("\nComponent {0}:".format(str(i)))
            i += 1
            for c in cc:
                s = "["
                for x in c:
                    s += str(x) + ','
                s = s[:-1]
                s += "]"
                print(s)        
                
    def get_connected_components(self): 
        """
        Uses DFS to find connected components in the total graph.
        """           
        cc = [] 
        repeat = [] 
        
        for i in range(self.V): 
            repeat.append(False) 

        for v in range(self.V): 
            if not repeat[v]: 
                t = [] 
                cc.append(self.dfs(t, v, repeat)) 
        
        return cc 
    
    def dfs(self, t, v, repeat):
        """
        Uses the DFS algorithm to recursively scan through the graph looking for connected edges.
        ----------
        Parameters
            t : []
                The temp list used for checking existing values.
            v : int
                The new vertex to add.
            repeat : []
                The list of vertices that already exist in the component.
        """         
        repeat[v] = True
        t.append(v) 

        for i in self.graph[v]: 
            if not repeat[i[0]]: 
                t = self.dfs(t, i[0], repeat) 

        return t


# In[4]:


class Graph():
    """
    Class to contain the algorithms for MST-Prim and graph data.
    Graph data should be stored a an adjacency list with the matching nodes containing the weight of the edge.
    """
    def __init__(self, vertices, graph_dict):
        """
        Initializes a new instance of the Graph class
        ----------
        Parameters
            graph_dict : {}
                The graph dictionary containing the node labels.
        """        
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
        self.graph_dict = graph_dict        
        
    def dfs(self, v, repeat = None, path = None):
        """
        Uses the DFS algorithm to recursively scan through the graph looking for 
        the longest path possible.
        ----------
        Parameters
            t : []
                The temp list used for checking existing values.
            v : int
                The new vertex to add.
            repeat : []
                The list of vertices that already exist in the component.
        """         
        if repeat is None: 
            repeat = []
        if path is None: 
            path = [v]

        repeat.append(v)

        paths = []
        for t in self.graph[v[0]]: 
            if int(self.graph_dict[t[0]]) > int(self.graph_dict[path[-1][0]]) and not self.in_vertex_list(t, repeat): 
                new_path = path + [t]
                paths.append(tuple(new_path))
                paths.extend(self.dfs(t, repeat[:], new_path)) 

        return paths
    
    def in_vertex_list(self, v, verticies):
        """
        Helper method to check if a tuple vert is in a list of tuples
        ----------
        Parameters
            v : (,)
                The vert in question.
            verticies: []
                The list of verticies to check aginst.
        """  
        t = [vert for vert in verticies if vert[0] == v[0]]
        return len(t) > 0


# In[6]:


forest = Forest(graph_data) 

def in_path_list(path, paths):
    if len(paths) is 0:
        return False
    for p in paths:
        if len(p) is not len(path):
            continue
        if in_tup(p, path):
            return True
    return False

def in_tup(p, path):
    for i in range(len(p)):
        if p[i][0] is not path[i][0]:
            return False
    return True

for i in range(len(forest.forest)):
    max_paths = []
    max_length = 0
    verticies = len(forest.forest_dicts[i][0])
    data = forest.forest[i]
    graph_dict = forest.forest_dicts[i][1]
    g = Graph(verticies, graph_dict)
    g.graph = data
    
    # Find max possible paths.
    for vertex in graph_dict:
        paths = g.dfs((vertex, 0))
        for p in paths:
            length = len(p)
            if length >= max_length:
                if length > max_length:
                    max_paths = []
                    max_length = length                
                if not in_path_list(p, max_paths):
                    max_paths.append(p)
                    
    print("\nMax paths that exist in subgraph {0} of GraphData.txt have a length of {1}.".format(i, len(max_paths[0])))
    # Print Possible Paths
    for p in max_paths:
        s = ""
        for t in p:            
            s += str(graph_dict[t[0]]) + " -> "
        s = s[:-3]
        print(s)


# In[ ]:





# In[ ]:




