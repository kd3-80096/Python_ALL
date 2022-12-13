## **Depth First Search Implementation**
## **Used Data Structure : Stack**

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

## method definition

def depth_first_search(visited,graph,node):
    ## to check if element is present or not
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        ## checking for all the adjacent ones
        for adjacent in graph[node]:
            depth_first_search(visited,graph,adjacent)

## Driver code
depth_first_search(visited,graph,'A')


## The time complexity of the DFS algorithm is O(V+E), where V is the number of vertices and
E is the number of edges in the graph.

