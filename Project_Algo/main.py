import heapq


def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    pq = [(0, source)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]['neighbors'].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def construct_graph(pm25_values, edges):
    graph = {}
    for station, nearest_stations in edges.items():
        pm25_value = pm25_values[int(station.replace("Station", "")) - 1]
        neighbors = {neighbor: distance for neighbor, distance in nearest_stations}
        graph[station] = {'pm25': pm25_value, 'neighbors': neighbors}
    return graph


def find_least_pollution_path(pm25_values, edges, source_station, destination_station):
    graph = construct_graph(pm25_values, edges)
    distances = dijkstra(graph, source_station)

    path = [destination_station]
    current_node = destination_station
    while current_node != source_station:
        for neighbor, weight in graph[current_node]['neighbors'].items():
            if distances[current_node] == distances[neighbor] + weight:
                path.append(neighbor)
                current_node = neighbor
                break
    path.reverse()

    pollution_values = [graph[station]['pm25'] for station in path]

    total_distance = distances[destination_station]

    return path, pollution_values, total_distance


pm25_values_foreach_station = [
    24.2, 23.9, 22.7, 16.1, 24.6, 18.4, 18, 18.6, 17.1, 17.4,
    16.7, 14.9, 10.9, 28.1, 18, 27, 24.8, 16.6, 19.9, 23.7,
    23, 19.5, 17.4, 24.1, 17.8, 18, 23.6, 28.6, 24.2, 18.3,
    20, 16.7, 27, 23, 23.2, 30.3, 17.2, 15.6, 29.8, 16.2
]

edges = {
    'Station1': [('Station2', 2), ('Station16', 5), ('Station25', 10), ('Station33', 8), ('Station26', 3)],
    'Station2': [('Station1', 2), ('Station3', 3), ('Station15', 7), ('Station17', 4), ('Station26', 2)],
    'Station3': [('Station2', 3), ('Station4', 3), ('Station16', 4), ('Station18', 5), ('Station27', 4)],
    'Station4': [('Station3', 3), ('Station5', 3), ('Station17', 2), ('Station19', 6), ('Station28', 5)],
    'Station5': [('Station4', 3), ('Station6', 3), ('Station18', 5), ('Station20', 4), ('Station29', 6)],
    'Station6': [('Station5', 3), ('Station7', 3), ('Station19', 6), ('Station21', 3), ('Station30', 5)],
    'Station7': [('Station6', 3), ('Station8', 3), ('Station20', 7), ('Station22', 2), ('Station31', 6)],
    'Station8': [('Station7', 3), ('Station9', 3), ('Station21', 5), ('Station23', 4), ('Station32', 7)],
    'Station9': [('Station8', 3), ('Station10', 3), ('Station22', 4), ('Station24', 5), ('Station33', 8)],
    'Station10': [('Station9', 3), ('Station11', 3), ('Station23', 6), ('Station25', 4), ('Station34', 7)],
    'Station11': [('Station10', 3), ('Station12', 3), ('Station24', 4), ('Station26', 2), ('Station35', 5)],
    'Station12': [('Station11', 3), ('Station13', 3), ('Station25', 5), ('Station27', 3), ('Station36', 6)],
    'Station13': [('Station12', 3), ('Station14', 3), ('Station26', 4), ('Station28', 3), ('Station37', 9)],
    'Station14': [('Station13', 3), ('Station15', 3), ('Station27', 4), ('Station29', 4), ('Station38', 10)],
    'Station15': [('Station14', 3), ('Station16', 3), ('Station28', 4), ('Station30', 4), ('Station39', 11)],
    'Station16': [('Station1', 5), ('Station3', 4), ('Station15', 3), ('Station17', 3), ('Station31', 7)],
    'Station17': [('Station2', 4), ('Station4', 2), ('Station16', 3), ('Station18', 3), ('Station32', 5)],
    'Station18': [('Station3', 5), ('Station5', 5), ('Station17', 3), ('Station19', 3), ('Station33', 6)],
    'Station19': [('Station4', 6), ('Station6', 6), ('Station18', 3), ('Station20', 3), ('Station34', 6)],
    'Station20': [('Station5', 4), ('Station7', 7), ('Station19', 3), ('Station21', 3), ('Station35', 7)],
    'Station21': [('Station6', 3), ('Station8', 5), ('Station20', 3), ('Station22', 3), ('Station36', 5)],
    'Station22': [('Station7', 2), ('Station9', 4), ('Station21', 3), ('Station23', 3), ('Station37', 6)],
    'Station23': [('Station8', 4), ('Station10', 6), ('Station22', 3), ('Station24', 3), ('Station38', 7)],
    'Station24': [('Station9', 5), ('Station11', 4), ('Station23', 3), ('Station25', 4), ('Station39', 8)],
    'Station25': [('Station1', 10), ('Station10', 4), ('Station12', 5), ('Station24', 4), ('Station40', 12)],
    'Station26': [('Station1', 3), ('Station2', 2), ('Station11', 2), ('Station13', 4), ('Station27', 3)],
    'Station27': [('Station3', 4), ('Station12', 3), ('Station14', 4), ('Station26', 3), ('Station28', 4)],
    'Station28': [('Station4', 5), ('Station13', 3), ('Station15', 4), ('Station27', 4), ('Station29', 3)],
    'Station29': [('Station5', 6), ('Station14', 4), ('Station16', 4), ('Station28', 3), ('Station30', 3)],
    'Station30': [('Station6', 5), ('Station15', 4), ('Station17', 3), ('Station29', 3), ('Station31', 3)],
    'Station31': [('Station7', 6), ('Station16', 7), ('Station18', 6), ('Station30', 3), ('Station32', 2)],
    'Station32': [('Station8', 7), ('Station17', 5), ('Station19', 6), ('Station31', 2), ('Station33', 3)],
    'Station33': [('Station1', 8), ('Station9', 8), ('Station18', 6), ('Station20', 3), ('Station32', 3)],
    'Station34': [('Station10', 7), ('Station19', 6), ('Station21', 5), ('Station33', 3), ('Station35', 3)],
    'Station35': [('Station11', 5), ('Station20', 7), ('Station22', 6), ('Station34', 3), ('Station36', 4)],
    'Station36': [('Station12', 6), ('Station21', 5), ('Station23', 7), ('Station35', 4), ('Station37', 5)],
    'Station37': [('Station13', 9), ('Station22', 6), ('Station24', 7), ('Station36', 5), ('Station38', 6)],
    'Station38': [('Station14', 10), ('Station23', 7), ('Station25', 12), ('Station37', 6), ('Station39', 6)],
    'Station39': [('Station15', 11), ('Station24', 8), ('Station26', 5), ('Station38', 6), ('Station40', 3)],
    'Station40': [('Station25', 12), ('Station27', 3), ('Station39', 3), ('Station1', 4), ('Station2', 4)]
}

source_station = 'Station1'
destination_station = 'Station4'

path, pollution_values, total_distance = find_least_pollution_path(pm25_values_foreach_station, edges, source_station,
                                                                   destination_station)
print(f"Shortest path from {source_station} to {destination_station}: {path}")
print("PM2.5 values along the path:", pollution_values)
print("Total distance along the path:", total_distance, "km")
