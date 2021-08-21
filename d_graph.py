# Course: CS261 - Data Structures
# Author: Alexandra Sciocchetti
# Assignment: Assignment 6
# Description: Implementation of a directed graph and associated functions

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Method adds a new vertex to the graph and returns the number of vertices in the graph
        """
        #if there are currently no vertices, add an empty list
        current_vertices = len(self.adj_matrix)
        if current_vertices == 0:
            self.adj_matrix.append([])
            self.v_count += 1
        #if vertices already exist, add a list with the number of 0's corresponding to the number of vertices
        #in the adj_matrix
        else:
            self.adj_matrix.append([0] * current_vertices)
            self.v_count += 1
        #add one 0 to each vertices to account for new vertice
        for item in self.adj_matrix:
            item.append(0)
        return len(self.adj_matrix)


    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        adds a new edge to the graph, connecting the two vertices with the provided
        indices. If either (or both) vertex indices do not exist in the graph, or if the weight is not a
        positive integer, or if src and dst refer to the same vertex, the method does nothing. If an
        edge already exists in the graph, the method will update its weight.
        """
        #check whether src, dst, and weight meet requirements
        current_length = len(self.adj_matrix)
        if src > current_length-1 or src < 0 or dst > current_length-1 or dst < 0 or src == dst:
            return
        if weight < 1:
            return
        #set edge
        else:
            self.adj_matrix[src][dst] = weight


    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between the two vertices with provided indices. If either vertex indices
        do not exist in the graph, or if there is no edge between them, method does nothing
        """
        #check to see if src and dst meet requirements
        current_vertices = self.v_count
        if src < 0 or src > current_vertices -1 or dst < 0 or dst > current_vertices -1:
            return
        #if requirements met, set edge to 0
        else:
            self.adj_matrix[src][dst] = 0


    def get_vertices(self) -> []:
        """
        Returns a list of the vertices of the graph. The order of the vertices in the list
        does not matter
        """
        vertice_list = []
        for i in range(self.v_count):
            vertice_list.append(i)
        return vertice_list

    def get_edges(self) -> []:
        """
        Returns a list of edges in the graph. Each edge is returned as a tuple of two
        incident vertex indices and weight. The first element in the tuple refers to the source vertex.
        The second element in the tuple refers to the destination vertex. The third element in the
        tuple is the weight of the edge.
        """
        edge_list = []
        #iterate through adj_matrix and each vertex in adj_matrix to find edges (values > 0)
        for i in range(self.v_count):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] != 0:
                    edge_list.append((i, j, self.adj_matrix[i][j]))
        return edge_list



    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list of vertex indices and returns True if the sequence of vertices
        represents a valid path in the graph. An empty path is valid.
        """
        if len(path) == 0:
            return True
        for i in range(len(path)-1):
            path_location = path[i]
            next_location = path[i+1]
            if self.adj_matrix[path_location][next_location] == 0:
                return False
        return True


    def dfs(self, v_start, v_end=None) -> []:
        """
        Method performs a depth-first search (DFS) in the graph and returns a list of vertices
        visited during the search, in the order they were visited.
        """
        #initial condition
        if v_start < 0 or v_start > self.v_count -1:
            return []
        visited_vertices = []
        stack = []
        stack.append(v_start)
        # while stack length is not empty, pop a vertex, added to vertices visited (if not already visited)
        # if vertex equals end point, stop there
        while len(stack) != 0:
            vertex = stack.pop()
            if vertex not in visited_vertices:
                visited_vertices.append(vertex)
                if vertex == v_end:
                    break
                #iterate through edges starting with highest index so that vertices are picked
                #from the stack in ascending order:
                for i in range(self.v_count-1, -1, -1):
                    if self.adj_matrix[vertex][i] != 0:
                        stack.append(i)
        return visited_vertices


    def bfs(self, v_start, v_end=None) -> []:
        """
        Method works the same as DFS above, except it implements a breadth-first search.
        """
        queue = deque([])
        if v_start < 0 or v_start > self.v_count -1:
            return []
        vertices_visited = []
        queue.appendleft(v_start)
        while len(queue) != 0:
            #pop from the right of the queue
            vertex = queue.pop()
            if vertex not in vertices_visited:
                vertices_visited.append(vertex)
                if vertex == v_end:
                    break
                for i in range(self.v_count):
                #for i in range(self.v_count - 1, -1, -1):
                    if self.adj_matrix[vertex][i] != 0:
                        queue.appendleft(i)
        return vertices_visited


    def has_cycle(self):
        """
        Returns True if there is at least one cycle in the graph. If the graph is acyclic,
        the method returns False.
        """
        #iterate through each vertice in adj_matrix and create two empty sets to keep track of position,
        #as well as an empty stack. Use bfs logic to append and pop from the stack
        for v in range(self.v_count):
            discovered = set()
            finished = set()
            start = v
            stack = []
            stack.append(v)
            while len(stack) != 0:
                vertex = stack.pop()
                if vertex in finished and vertex == start:
                    return True
                if vertex not in discovered:
                    discovered.add(vertex)
                    for i in range(self.v_count):
                        if self.adj_matrix[vertex][i] != 0:
                            stack.append(i)
                #once vertex has been checked it is moved to finished set
                finished.add(vertex)
        return False


    def dijkstra(self, src: int) -> []:
        """
        Implements the Dijkstra algorithm to compute the length of the shortest path
        from a given vertex to all other vertices in the graph and returns a list with one value per
        vertex. If a certain vertex is not reachable from SRC, the returned value is infinity (inf).
        """
        #logic is very similar to psuedo-code provided in lecture, utilizing a priority queue
        #initialize dictionary for visited vertices, and priority queue. Push start value into queue with weight 0
        visited_vertices = dict()
        priority_queue = []
        heapq.heappush(priority_queue, (0,src))
        #while priority queue is not empty, pop value with smallest weight (shortest distance)
        while len(priority_queue) != 0:
            vertex = heapq.heappop(priority_queue)
            v = vertex[1]
            d = vertex[0]

            #if not visited, add, to visited, and then iterate through all edges of vertex
            if v not in visited_vertices:
                visited_vertices[v] = d

                for e in range(self.v_count):
                    if self.adj_matrix[v][e] != 0:
                        #if edge exists, add to queue and calculate distance as weight plus distances to v
                        heapq.heappush(priority_queue, (self.adj_matrix[v][e] + d, e))
        #format output
        output_list = []
        for i in range(self.v_count):
            #if vertex was unreachable, return set that vertex distance to inf
            try:
                output_list.append(visited_vertices[i])
            except KeyError:
                output_list.append(float('inf'))
        return output_list





if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
