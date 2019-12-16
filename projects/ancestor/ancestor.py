'''
Since we are looking for the shortest path we know we are doing a BFT
so we will need a queue
'''

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        vertices = {}
    
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
            # TODO: We need error checking here
        
    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

def earliest_ancestor(ancestors, starting_node):
    # Build our graph by initializing it
    # ancestors is going to pass in a pair of data [2,3] or [9,2] etc
    graph = Graph()

    # for each variable in the pair passed in add the vertex
    for pair in ancestors:
        # Adding vertex for pair 0 & 1
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # Build the edges in reverse to create a bi directional relationship between the data
        graph.add_edges(pair[1], pair[0])
