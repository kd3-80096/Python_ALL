
## Importing the min_heap

import heapq 

## Dijkstra's Algorithm

def calculate_distances(graph,starting_vertex):
    distances =  {vertex: float('infinity') for vertex in graph}  ## initial cost of the vertices in a graph to infinity in dictionary format
    print(distances)
    distances[starting_vertex] = 0 ## initializing the starting index distance to 0 from infinity
    print(distances)

    pq = [(0,starting_vertex)] #distances of the vertices in the graph from the starting vertex
    print(len(pq))

    while (len(pq)>0):
        current_distance, current_vertex = heapq.heappop(pq) #Pop the smallest item off the heap, maintaining the heap
        
        if current_distance > distances[current_vertex]:
            """This line of code checks if the distance of the current vertex is greater than the distance 
            of the current vertex in the distances dictionary. If this is true, it means the vertex is
            already visited and the algorithm has already found the shortest path to this vertex, so the 
            algorithm can skip this vertex and continue to the next one."""
            continue

        for neighbor,weight in graph[current_vertex].items():  ## neighbour is the keys and weight is the distance value from graph[current_vertex]
            #print(graph[current_vertex].items())
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've  already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance ## decreasekey_operation
                heapq.heappush(pq,(distance,neighbor))  ##Push item onto heap, maintaining the heap

    return distances



        



distances = {
    'A' :{'B':2, 'C':5, 'D':2, 'E':7, 'F':50 },
    'B' :{'C':2, 'D':1, 'E':2, 'F':60},
    'C' :{'B':3, 'E':2, 'F':90},
    'D' :{'E':1, 'F':3},
    'E' :{'D':4, 'F':4},
    'F' :{}
}

print(f"Dijkstra's Algorithms shortest distances", calculate_distances(distances, 'A'))

