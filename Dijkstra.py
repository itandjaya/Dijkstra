# Dijkstra.py
# Dijkstra's algorithm implementation.
# Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph.

DEBUG = 0;
class Graph:
    # Graph class, with directed edges and weight/distance.

    def __init__(   self, edges = []):
        ## Graph constructor.
        ## Initialize graph in the form of 2D hash table: self.graph[u][v].
        ## Save the edges under self.edges.
        ## Save the vertices under self.vertices.

        self.edges      =   [];
        self.graph      =   {};
        self.vertices   =   set();

        for u, v, dist in edges:
            self.add_edge(u, v, dist);
        
        return;   
            

    def add_edge(self, u, v, dist):
        ## Add a single edge into the graph.

        if u not in self.graph:         self.graph[u] = {};

        self.graph[u][v] = dist;
        self.vertices |= {u,v};
        self.edges.append( (u,v,dist));

        return;

    def generate_2D_map(self):
        ## Returns hash_map of distances between vertices.
        ## If there's no path, the distance is infinity.
        ## Complexity: O(V**2), Space: O(V**2). V is number of vertices.

        hash_map = {};

        for u in self.vertices:
            for v in self.vertices:

                dist = 0;

                if u != v:
                    try:        dist = self.graph[u][v];
                    except:     dist = float('inf');
                    
                hash_map[(u,v)] = dist;   

        return hash_map;

    def find_distance(self, start, dest):  
        ## Dijkstra's algorithm, breath-first-search, greedy algorthm approach.
        ## Returns the shortest distance from u to v, if it exists.
        ## Otherwise, returns None.
        ## Complexity: O(V**2) + O(E**2), Space: O(V**2 + E. 
        ## V is number of vertices. E is number of edges.

        if start not in self.vertices or dest not in self.vertices:
            return None;

        hash_2D_map =   self.generate_2D_map();

        visited = set();
        to_be_visited   =   [   (start, start, 0)];
        
        if DEBUG:   visit_sequences =   [];

        while to_be_visited and dest not in visited:

            #u, v, dist =   to_be_visited.pop(0);

            u, v, ind        =   None, None, None;
            dist = float('inf');

            for i, (tu, tv, tdist) in enumerate(to_be_visited):
                if tdist<dist:
                    ind, dist    =   i, tdist;

            u, v, dist  =   to_be_visited.pop(ind);

            hash_2D_map[(start,v)] = min(   hash_2D_map[(start,v)],
                                            hash_2D_map[(start,u)] + hash_2D_map[(u,v)]
                                        );

            visited.add(v);
            if DEBUG:       visit_sequences.append(v);

            try:
                next_visits = [   (v, next_v, self.graph[v][next_v])   for next_v in self.graph[v].keys()];
                to_be_visited.extend(next_visits);
            
            except:
                None
            

        if DEBUG:       print(visit_sequences);

        if dest not in visited:     return None;
        else:                       return hash_2D_map[(start, dest)];
