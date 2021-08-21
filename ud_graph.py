# Course: CS 261
# Author: Alexandra Sciocchetti
# Assignment: Assignment 6
# Description: Implementation of an undirected graph and associated functions


import heapq
from collections import deque


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        method adds a new vertex to the graph. Vertex names can be any string. If a vertex
        with the same name is already present in the graph, the method does nothing
        """
        # if input vertex is not in dictionary, add v as the key and an empty list as the value pair
        if v not in self.adj_list:
            self.adj_list[v] = []

        
    def add_edge(self, u: str, v: str) -> None:
        """
        Method adds a new edge to the graph, connecting the two vertices with the provided
        names. If either (or both) vertex names do not exist in the graph, this method will first
        create them and then create an edge between them. If an edge already exists in the graph,
        or if u and v refer to the same vertex, the method does nothing
        """
        if u == v:
            return
        #if either u or v are in the dictionary and the corresponding edge is not already listed
        #add the edge
        if u in self.adj_list and v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if v in self.adj_list and u not in self.adj_list[v]:
            self.adj_list[v]. append(u)

        #if either u or v is not in the dictionary, add them and add the corresponding edge
        if u not in self.adj_list:
            self.adj_list[u] = [v]
        if v not in self.adj_list:
            self.adj_list[v] = [u]


    def remove_edge(self, v: str, u: str) -> None:
        """
        Removes an edge between the two vertices with provided names. If either (or
        both) vertex names do not exist in the graph, or if there is no edge between them, the
        method does nothing
        """
        if v not in self.adj_list or u not in self.adj_list:
            return
        if u not in self.adj_list[v]:
            return
        else:
            self.adj_list[v].remove(u)
            self.adj_list[u].remove(v)


    def remove_vertex(self, v: str) -> None:
        """
        method removes a vertex with a given name and all edges incident to it from the
        graph. If the given vertex does not exist, the method does nothing.
        """
        if v not in self.adj_list:
            return
        del self.adj_list[v]
        for key in self.adj_list:
            if v in self.adj_list[key]:
                self.adj_list[key].remove(v)



    def get_vertices(self) -> []:
        """
        Returns list of vertices in the graph (any order)
        """
        vertice_list = []
        for key in self.adj_list:
            vertice_list.append(key)
        return vertice_list
       

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order).  Each edge is returned as a tuple of two
        incident vertex names.
        """
        #create edge_list. Loop through dictionary and add (vertex, edge) pairs to list
        edge_list = []
        for key in self.adj_list:
            for vertex in self.adj_list[key]:
                key_value_tuple = (key, vertex)
                #see if reverse order is already in the list: (A, B) is the same as (B, A) in this case
                if key_value_tuple[::-1] not in edge_list:
                    edge_list.append(key_value_tuple)
        return edge_list
        

    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list of vertex names and returns True if the sequence of vertices
        represents a valid path in the graph. An empty path is considered valid.
        """
        #if length if 0 return true. If length is 1, check to see if single value is in the
        #dictionary. If not, return False
        if len(path) == 0:
            return True
        if len(path) == 1:
            if path[0] not in self.adj_list:
                return False
        #if length is greater than one, loop through the path list and check to see if each
        #corresponding dictionary key has a vertex that corresponds with the next item in the list
        for i in range(len(path) - 1):
            key = path[i]
            next = path[i+1]
            if key not in self.adj_list or next not in self.adj_list[key]:
                return False
        return True
       

    def dfs(self, v_start, v_end=None) -> []:
        """
        Performs a depth-first search (DFS) in the graph and returns a list of vertices
        visited during the search, in the order they were visited.
        """
        #create an empty stack using python list structure and a list of vertices visited
        stack = []
        if v_start not in self.adj_list:
            return []
        vertices_visited = []
        stack.append(v_start)
        #while stack length is not empty, pop a vertex, added to vertices visited (if not already visited)
        #if vertex equals end point, stop there
        while len(stack) != 0:
            vertex = stack.pop()
            if vertex not in vertices_visited:
                vertices_visited.append(vertex)
                if vertex == v_end:
                    break
                #sort list values so that they are added to the stack in required order
                self.adj_list[vertex].sort(reverse=True)
                for next_vertex in self.adj_list[vertex]:
                    stack.append(next_vertex)
        return vertices_visited



    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        #very similar to dfs except uses a queue to implement first in first out structure
        queue = deque([])
        if v_start not in self.adj_list:
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
                self.adj_list[vertex].sort()
                for next_vertex in self.adj_list[vertex]:
                    #use append left so that vertices are added to the queue on the left
                    queue.appendleft(next_vertex)
        return vertices_visited



    def count_connected_components(self):
        """
        Return number of connected components in the graph with help form the
        depth first search (dfs) function.
        """
        #initialize vertices visited and count.
        vertices_visited = []
        count = 0
        #iterate through each vertex in dictionary. If it isn't in the visited list, perform dfs, then add
        #all vertices visited from dfs to the vertices_visited list and increase count.
        for vertex in self.adj_list:
            if vertex not in vertices_visited:
                vertices = self.dfs(vertex)
                count += 1
                for item in vertices:
                    vertices_visited.append(item)
        return count
      

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise.
        """
        #relies on the logic that graph has no cycles it is tree, which will always
        #have edges = number of vertices -1
        #in this case, since there are often multiple connected graphs, the equation is modified to
        # edges = vertices - connected components
        connected_components = self.count_connected_components()
        vertices = len(self.get_vertices())
        edges = len(self.get_edges())
        if edges == vertices - connected_components:
            return False
        return True
       

   


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BD', 'BH', 'CD', 'CA', 'EF', 'QG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')




    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()

    print("\nPDF - method has_cycle() example 500")
    print("----------------------------------")
    edges = ['AE', 'AC', 'DB', 'CD', 'EF', 'BH', 'QG', 'DQ']
    g = UndirectedGraph(edges)
    print(g.has_cycle())


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
