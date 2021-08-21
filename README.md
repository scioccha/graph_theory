# Undirected and Directed graphs
The following two files (ud_graph.py and d_graph.py) should contain undirected and directed graphs classes and associated methods

The UndirectedGraph class should include the following methods implemented for an undirected graph: add_vertex(), add_edge() remove_edge(), remove_vertex() get_vertices(), get_edges() is_valid_path(), dfs(), bfs() count_connected_components(), has_cycle()

All undirected graphs are stored as a Python dictionary of lists where keys are vertex names (strings) and associated values are Python lists with names (in any order) of vertices connected to the 'key' vertex.

The DirectedGraph class should include the following methods implemented for a directed graph: add_vertex(), add_edge() remove_edge(), get_vertices(), get_edges() is_valid_path(), dfs(), bfs() has_cycle(), dijkstra()

All directed graphs are stored as a two dimensional matrix, which is a list of lists in Python. Element on the i-th row and j-th column in the matrix is the weight of the edge going from the vertex with index i to the vertex with index j. If there is no edge between those vertices, the value is zero.

Function specifids for both the UndirectedGraph and DirectedGraph classes are listed below:

# Undirected Graph
add_vertex: This method adds a new vertex to the graph. Vertex names can be any string. If a vertex with the same name is already present in the graph, the method does nothing (no exception needs to be raised).

add_edge: This method adds a new edge to the graph, connecting the two vertices with the provided names. If either (or both) vertex names do not exist in the graph, this method will first create them and then create an edge between them. If an edge already exists in the graph, or if u and v refer to the same vertex, the method does nothing (no exception needs to be raised).

remove_edge: This method removes an edge between the two vertices with provided names. If either (or both) vertex names do not exist in the graph, or if there is no edge between them, the method does nothing (no exception needs to be raised).

remove_vertex: This method removes a vertex with a given name and all edges incident to it from the graph. If the given vertex does not exist, the method does nothing (no exception needs to be raised).

get_vertices: This method returns a list of vertices of the graph. The order of the vertices in the list does not matter

get_edges: This method returns a list of edges in the graph. Each edge is returned as a tuple of two incident vertex names. The order of the edges in the list or the order of the vertices incident to each edge does not matter.

is_valid_path: This method takes a list of vertex names and returns True if the sequence of vertices represents a valid path in the graph (so one can travel from the first vertex in the list to the last vertex in the list, at each step traversing over an edge in the graph). An empty path is considered valid.

dfs: This method performs a depth-first search (DFS) in the graph and returns a list of vertices visited during the search, in the order they were visited. It takes one required parameter, name of the vertex from which the search will start, and one optional parameter - name of the ‘end’ vertex that will stop the search once that vertex is reached. If the starting vertex is not in the graph, the method should return an empty list (no exception needs to be raised). If the name of the ‘end’ vertex is provided but is not in the graph, the search should be done as if there was no end vertex. When several options are available for picking the next vertex to continue the search, your implementation should pick the vertices in ascending lexicographical order (so, for example, vertex ‘APPLE’ is explored before vertex ‘BANANA’).

bfs: This method works the same as DFS above, except it implements a breadth-first search.

count_connected_components: This method returns the number of connected components in the graph.

has_cycle: This method returns True if there is at least one cycle in the graph. If the graph is acyclic, the method returns False.

# Directed Graph

add_vertex: This method adds a new vertex to the graph. A vertex name does not need to be provided; instead the vertex will be assigned a reference index (integer). The first vertex created in the graph will be assigned index 0, subsequent vertices will have indexes 1, 2, 3 etc. This method returns a single integer - the number of vertices in the graph after the addition.

add_edge: This method adds a new edge to the graph, connecting the two vertices with the provided indices. If either (or both) vertex indices do not exist in the graph, or if the weight is not a positive integer, or if src and dst refer to the same vertex, the method does nothing. If an edge already exists in the graph, the method will update its weight.

remove_edge: This method removes an edge between the two vertices with provided indices. If either (or both) vertex indices do not exist in the graph, or if there is no edge between them, the method does nothing (no exception needs to be raised).

get_vertices: This method returns a list of the vertices of the graph. The order of the vertices in the list does not matter.

get_edges: This method returns a list of edges in the graph. Each edge is returned as a tuple of two incident vertex indices and weight. The first element in the tuple refers to the source vertex. The second element in the tuple refers to the destination vertex. The third element in the tuple is the weight of the edge. The order of the edges in the list does not matter.

is_valid_path: This method takes a list of vertex indices and returns True if the sequence of vertices represents a valid path in the graph (one can travel from the first vertex in the list to the last vertex in the list, at each step traversing over an edge in the graph). An empty path is considered valid.

dfs: This method performs a depth-first search (DFS) in the graph and returns a list of vertices visited during the search, in the order they were visited. It takes one required parameter, the index of the vertex from which the search will start, and one optional parameter - the index of the ‘end’ vertex that will stop the search once that vertex is reached. If the starting vertex is not in the graph, the method should return an empty list (no exception needs to be raised). If the ‘end’ vertex is provided but is not in the graph, the search should be done as if there was no end vertex. When several options are available for picking the next vertex to continue the search, your implementation should pick the vertices by vertex index in ascending order (so, for example, vertex 5 is explored before vertex 6).

bfs: This method works the same as DFS above, except it implements a breadth-first search.

has_cycle: This method returns True if there is at least one cycle in the graph. If the graph is acyclic, the method returns False.

dijkstra: This method implements the Dijkstra algorithm to compute the length of the shortest path from a given vertex to all other vertices in the graph. It returns a list with one value per each vertex in the graph, where the value at index 0 is the length of the shortest path from vertex SRC to vertex 0, the value at index 1 is the length of the shortest path from vertex SRC to vertex 1 etc. If a certain vertex is not reachable from SRC, the returned value should be INFINITY (in Python, use float(‘inf’)).
