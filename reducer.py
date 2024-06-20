import sys
import csv
from heapq import heappush, heappop

class Heap:
    def __init__(self):
        self.heap = []
    
    def push(self, priority, item):
        heappush(self.heap, (priority, item))
    
    def pop(self):
        return heappop(self.heap)[1]
    
    def is_empty(self):
        return len(self.heap) == 0

def reducer():
    # Initialize an empty dictionary to store nodes and their edges
    nodes_dict = {}

    # Iterate through each key-value pair in standard input
    for line in sys.stdin:
        # Extract the node and its edges from the key-value pair, and convert them to integers
        node, edges_str = line.strip().split("\t")
        edges = list(map(int, edges_str.split(",")))

        # Add the node and its edges to the dictionary
        nodes_dict[int(node)] = list(map(int, edges))
    print(nodes_dict)
    return nodes_dict
    # Output the final integer type dictionary
    

def shortest_path(graph, node1, node2):
    # Initialize a dictionary to store the distance of each node from the starting node
    distance_dict = {node1: 0}

    # Initialize a dictionary to store the path to each node from the starting node
    path_dict = {node1: [node1]}

    # Initialize a heap with the starting node and its distance from the starting node
    heap = Heap()
    heap.push(0, node1)

    # While the heap is not empty
    while not heap.is_empty():
        # Pop the node with the smallest distance from the heap
        curr_node = heap.pop()

        # If the current node is the goal node, return its path from the starting node
        if curr_node == node2:
            return path_dict[curr_node]

        # Iterate through each neighbor of the current node
        for neighbor in graph.get(curr_node, []):
            # Compute the distance from the starting node to the neighbor
            dist = distance_dict[curr_node] + 1

            # If the neighbor has not been visited yet, or if the new distance is shorter than the previously computed distance
            if neighbor not in distance_dict or dist < distance_dict[neighbor]:
                # Update the distance of the neighbor from the starting node
                distance_dict[neighbor] = dist

                # Update the path to the neighbor from the starting node
                path_dict[neighbor] = path_dict[curr_node] + [neighbor]

                # Push the neighbor onto the heap with its updated distance from the starting node
                heap.push(dist, neighbor)

    # If no path is found, return an empty list
    return []

if __name__ == '__main__':
    # Define the name of the output file
    graph=reducer()
    output_file = "shortest_paths_21i1675.csv"
    size = len(graph)
    #size
    # Initialize a 2D list to store the shortest paths
    shortest_paths = []

    # Loop over all nodes in the graph
    for i in range(size):
        
        shortest_path_1675 = shortest_path(graph, 2692, 1675)

        # Add the shortest path to the list of shortest paths
        shortest_paths.append(shortest_path_1675)

    # Open the output file in write mode
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write all the shortest paths to the output
        writer.writerows(shortest_paths)

