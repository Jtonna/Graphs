# Create the queue
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

# Import the word list
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())


'''
Given two wods (begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from being_word to end_word such that:
Only one letter can be changed at a time
Each Transformed word must exist in the word list
Note that begin_word is not a transformed word

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume that no duplicated are in the word's list
You may assime begin_word and end_word are non-empty and are not the same

sameple:

begin_word: = "hit"
end_word: = "cog"
return ['hit', 'hot', 'cat', 'cog']

begin_word = "sail"
end_word = "boat"
return ['sail', 'bail', 'boil', 'ball', 'bolt', 'boat']

'''

# Find Neighbor's
def get_neighbors(word):
    neighbors = []

    # for each letter in the word
        # for each letter in the alphabet
            # change the word letter to the alphabet letter
            # if the new word is in the word_set
                # add it to neighbors
    

# 3 Steps
# Build our graph
# Words are "nodes" aka Vertex's & one-letter-apart is the edge
# Do a BFS from start_word to end_word

def find_ladders(begin_word, end_word):
    # BFS
    # Create a queue
    q = Queue()
    # Enqueue a path to the starting word
    q.enqueue( [begin_word] )
    # Create a visited set
    visited = set()
    # While the queue is not empty
    while q.size() > 0:
        # Dequeue the next path
        path = q.dequeue()
        # Grab the last word (vertex) from the path
        v = path[-1]
        # if v (the word) has not been visited
        if v not in visited:
            # Check if the word is end_word if not return path
            if v == end_word:
                return path
            # mark it as visited
            visited.add(v)
            # enqueue a path to each neighbor
            for neighbor in get_neighbors(v):
                path_copy = path.copy() # We are going to use shallow copy so we dont modify the original
                path_copy.append(neighbor)
                q.enqueue(path_copy)

find_ladders("sail", "boat")