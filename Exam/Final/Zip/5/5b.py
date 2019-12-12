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
        
print(graph_data)


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


# In[13]:


import sys 
  
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

    def print_all_pairs_shortest_path(self, s, i): 
        """
        Prints out the path length for each node in the graph.
        ----------
        Parameters
            s : int
                The starting node.
            i : []
                The starting node paths.
        """     
        print("(v1 -> v2) - Weighted Distance")
        max_weight = 0
        max_str = ""
        for node in range(self.V): 
            out = "({0} -> {1}) - {2}".format(self.graph_dict[s], self.graph_dict[node], i[node])
            print(out)
            if i[node] > max_weight:
                max_weight = i[node]
                max_str = out
        print("Max Path:", max_str)

    def extract_min(self, w, S): 
        """
        Gets the minimum weighted node from the start to each of the graph vertices.
        ----------
        Parameters
            w : int
                The starting node weights.
            S : []
                The set of node paths.
        """     
        min = sys.maxsize 

        for v in range(self.V): 
            if w[v] < min and S[v] == False: 
                min = w[v] 
                min_index = v 

        return min_index 

    def dijkstra(self, s): 
        """
        Preforms the Disjkstra Shortest Paths algorithm from the book p.658 (... and Wikipedia)
        ----------
        Parameters
            w : int
                The shortest path weight.
            s : []
                The source node.
        """           
        # Essentially INITIALIZE-SINGLE-SOURCE
        w = [sys.maxsize] * self.V 
        S = [False] * self.V 
        w[s] = 0

        for i in range(self.V): 
            u = self.extract_min(w, S) 
            S[u] = True

            # For each Vertex in Adj Graph
            for v in range(self.V): 
                if self.graph[u][v][1] > 0 and not S[v]:
                    if w[v] > w[u] + self.graph[u][v][1]: 
                        w[v] = w[u] + self.graph[u][v][1] 

        self.print_all_pairs_shortest_path(s, w) 


# In[14]:


forest = Forest(graph_data)
print("")
print("Dijkstra Shortest-Paths on Subgraph:", "1")
verticies = len(forest.forest_dicts[1][0])

for v in range(verticies):
    print("Path starting at vertex:", forest.forest_dicts[1][1][v])
    data = forest.forest[1]
    graph_dict = forest.forest_dicts[1][1]
    g = Graph(verticies, graph_dict)
    g.graph = data
    g.dijkstra(v)
    print("")


# In[ ]:





# In[ ]:




