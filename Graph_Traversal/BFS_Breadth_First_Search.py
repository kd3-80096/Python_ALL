## **Breadth First Search Implementation**
## **Used Data Structure : Queue**

## Graph Representation
graph = {
    'A':['B','C','D'],
    'B':['E'],
    'C':['E','F'],
    'D':['F'],
    'E':['G'],
    'F':['G'],
    'G':[]
}

## creating set to keep track of visited nodes

visited = set()

## queue used to implementation of the BFS

from collections import deque
queue = deque()

## method definition

def breadth_first_search(visited,graph,node):
    ## checking if the nodes visited or not and storing them into the visited set
    if node not in visited:
        visited.add(node)
        queue.appendleft(node)

    ## storing the elements into queue and popping
    while queue:
        node = queue.pop()
        print(node,end=" ")

    ## checking for all the adjacent nodes in the level

        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent) ## adding to the set
                queue.appendleft(adjacent) ## adding to the queue



## Driver_code

breadth_first_search(visited,graph,'A')

## The Time complexity of BFS is O(V + E) when Adjacency List is used and O(V^2) when
# Adjacency Matrix is used, where V stands for vertices and E stands for edges.


