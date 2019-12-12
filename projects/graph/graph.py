"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # vertices is a dict, so we can call it and pass in the vertex_id and add a new set
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.

        plan -- 
        if v1 and v2 in vertices:
            vertices v1 set add v2
        else:
            print error
        """
        print("-----")
        if v1 and v2 in self.vertices:
            print(f"Found vertex:{v1}, attempting to add {v2} to the set")
            self.vertices[v1].add(v2)
            print("    Addition successful")
        else:
            print(f"Sorry, we cant add an edge based on vertice's {v1} & {v2}")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.

        If vertex_id is in self.vertices
            return vertices[vertex_id]

        """
        if vertex_id in self.vertices:
            print(f"looking for vertex {vertex_id}'s edges, which should be {self.vertices[vertex_id]}")
            return self.vertices[vertex_id]
        else:
            print(f"Error finding {vertex_id}. This value may not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        plan -- 
        make a new empty queue
        add the starting vert id to the queue
        make an empty set to store a list of visited verts
        while the queue isnt empty
            remove the remove the first vert from the queue
            if the vert has not been visited
                add it to the set of visitied verts
                add its neighbors to the queue
        """

        # make a new queue & pass it the starting vert
        the_queue = Queue()
        the_queue.enqueue(starting_vertex)

        # create a new set to keep track of visited verts
        visited_verts = set()

        print(f"BFT ----")
        # If there is something in the queue
        while the_queue.size() > 0:
            print(f"    queue has {the_queue.size()}")
            # Remove the starting vertex from queue
            vert = the_queue.dequeue()
            print(f"        now it has {the_queue.size()}")

            # If the starting vert is not in the visited verts set
            if vert not in visited_verts:
                print(f"    vertex {vert} is not in visited_verts, so we are going to add it")
                # add it to the set
                visited_verts.add(vert)
                
                # Add the neighbors of the current vert to the queue
                print(f"    We are now going to pass the vert {vert}, to get_neighbors() and add the neighbors to the queue")
                for next_vertex in self.vertices[vert]:
                    print(f"    neighbor of {vert} found, enqueueing {next_vertex}")
                    the_queue.enqueue(next_vertex)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    ''' should print:
        {3, 4}
        {5}
        error
    '''
    print(graph.get_neighbors(2))
    print(graph.get_neighbors(3))
    print(graph.get_neighbors(1))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
