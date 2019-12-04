class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.G = [[0 for y in range(vertices)] for x in range(vertices)] 
  
    def print_mst(self, pi): 
        for i in range(1, self.V):
            if pi[i] is not None:
                print("Edge: ({0},{1}), Weight: {2}".format(pi[i], i, self.G[i][pi[i]]))
  
    def extract_min(self, key, Q): 
        min = sys.maxsize 
  
        for v in range(self.V): 
            if key[v] < min and Q[v] == 0: 
                min = key[v] 
                min_index = v 
  
        return min_index 

    def mst_prim(self):
        key = [sys.maxsize] * self.V 
        pi = [None] * self.V 

        key[0] = 0 
        Q = [0] * self.V 
  
        pi[0] = -1
        
        for v in range(self.V): 
            u = self.extract_min(key, Q) 
            Q[u] = 1
            for v in range(self.V): 
                if self.G[u][v] > 0 and Q[v] == 0 and key[v] > self.G[u][v]: 
                    pi[v] = u
                    key[v] = self.G[u][v] 
 
  
        self.print_mst(pi)