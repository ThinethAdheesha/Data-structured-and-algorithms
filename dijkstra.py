def dijkstra(start_node, graph):
    visited = {}  # Stores the shortest distance to each node
    unvisited = {}  # Stores nodes that haven't been visited

    # Initialize all distances to infinity
    for node in graph:
        unvisited[node] = float('inf')

    current = start_node
    current_distance = 0
    unvisited[current] = 0  # Distance to start node is 0

    while unvisited:
        # Update distances for neighbors
        for neighbour, distance in graph[current].items():
            if neighbour not in unvisited:
                continue  # Ignore already visited nodes

            new_distance = current_distance + distance
            if unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance

        # Mark the current node as visited
        visited[current] = current_distance
        del unvisited[current]

        if not unvisited:
            break  # Stop if all nodes are visited

        # Find the next node with the shortest distance
        sorted_items = sorted(unvisited.items(), key=lambda x: x[1])
        current, current_distance = sorted_items[0]  # Pick the closest node

    return visited


# Define the graph
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 35, 'E': 10},
    'C': {'A': 10, 'D': 20},
    'D': {'C': 20, 'B': 35, 'E': 10},
    'E': {'D': 10, 'B': 10}
}

# Run Dijkstra's algorithm
start_node = 'A'
min_distance = dijkstra(start_node, graph)

# Print the shortest distance from A to all nodes
print(min_distance)
