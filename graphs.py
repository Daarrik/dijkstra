import numpy as np

rng = np.random.default_rng()
n = 3
m = 3

mat_ns = rng.integers(1, 10, size=(n, m))
mat_ew = rng.integers(1, 10, size=(n, m))

rand_x = int(rng.random() * n)
rand_y = int(rng.random() * m)

# print((rand_x, rand_y))

print(mat_ns)
print(mat_ew)

neighbor_graph = {}
for x in range(n):
    for y in range(m):
        coord_neighbors = {}
        if not y == 0: coord_neighbors[(x, y-1)] = (mat_ns[x][y-1])
        if not y == m-1: coord_neighbors[(x, y+1)] = (mat_ns[x][y+1])
        if not x == 0: coord_neighbors[(x-1, y)] = (mat_ew[x-1][y])
        if not x == n-1: coord_neighbors[(x+1, y)] = (mat_ew[x+1][y])
        neighbor_graph[(x, y)] = coord_neighbors


# for coordinate, neighbors in neighbor_graph.items():
#     print(f'{coordinate}: {neighbors}')

# print(list(neighbor_graph.keys()))

def dijkstra(graph: dict, source):
    MAX_VALUE = 100000

    unvisited_coordinates = list(graph.keys())
    shortest_path_from_source = {}
    previous_coordinates = {}

    for coordinate in graph:
        shortest_path_from_source[coordinate] = MAX_VALUE
    shortest_path_from_source[source] = 0

    while unvisited_coordinates:
        # Takes first coordinate in shortest_path_from_source and then compares it to the rest of the list
        current_coordinate_with_shortest_distance_from_source = None
        for coordinate in unvisited_coordinates:
            if current_coordinate_with_shortest_distance_from_source == None:
                current_coordinate_with_shortest_distance_from_source = coordinate
            elif shortest_path_from_source[coordinate] < shortest_path_from_source[current_coordinate_with_shortest_distance_from_source]:
                current_coordinate_with_shortest_distance_from_source = coordinate
        
        unvisited_coordinates.remove(current_coordinate_with_shortest_distance_from_source)

        neighbors = graph[current_coordinate_with_shortest_distance_from_source]
        for neighbor in neighbors:
            alt_path = shortest_path_from_source[current_coordinate_with_shortest_distance_from_source] + graph[current_coordinate_with_shortest_distance_from_source][neighbor]
            if alt_path < shortest_path_from_source[neighbor]:
                shortest_path_from_source[neighbor] = alt_path
                previous_coordinates[neighbor] = current_coordinate_with_shortest_distance_from_source

    return shortest_path_from_source, previous_coordinates

dij1, dij2 = dijkstra(neighbor_graph, (rand_x, rand_y))
print(dij1)

def translate_to_matrix(shortest_path: dict):
    matrix = []
    cur_row = []
    cur_row_num = 0
    for coordinate, weight in shortest_path.items():
        if cur_row_num != coordinate[0]:
            matrix.append(cur_row)
            cur_row = []
            cur_row_num = coordinate[0]
        cur_row.append(weight)
    
    matrix.append(cur_row)
    return matrix

result = translate_to_matrix(dij1)

for row in result:
    print(row)