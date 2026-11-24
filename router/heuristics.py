

def nearest_neighbor(tt_matrix, depot = 0):
    visited = set()
    curr_stop = depot
    route = [depot]

    while True:
        visited.add(curr_stop)
        available_stops = tt_matrix[curr_stop]
        best_dist = float("inf")
        best_stop = None
        for i in range(len(available_stops)):
            if i in visited:
                continue
            if available_stops[i] < best_dist:
                best_dist = available_stops[i]
                best_stop = i
        if best_stop is None:
            break
        curr_stop = best_stop
        route.append(best_stop)

    route.append(depot)

    return route

def route_duration(route, tt_matrix):
    total_time = 0

    for a, b in zip(route, route[1:]):
        total_time += tt_matrix[a, b]
    
    return total_time

