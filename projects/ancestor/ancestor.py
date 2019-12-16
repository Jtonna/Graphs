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
        self.vertices = {}
    
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

        # Build the edges in reverse because we want a directional link from the kids to the parents.
        graph.add_edges(pair[1], pair[0])

    # We need a queue because we are doing a BFS, as well as enqueue the starting node
    q = Queue()
    q.enqueue([starting_node])

    # We need to keep track of the longest path so we know when we are done
    max_path_length = 1
    earliest_ancestor = -1

    #
    while q.size() > 0:
        path = q.dequeue()
        vertex = path[-1]

        # We need to check to se if there is two paths with the same length
        if (len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = vertex
            max_path_length = len(path)

        for neighbor in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    
    return earliest_ancestor
