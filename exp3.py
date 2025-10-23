import heapq
import random

def hill_climbing(cities, distance_matrix, max_iterations=1000):

    current_route = cities[:]
    random.shuffle(current_route)

    def route_cost(route):
        return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

    current_cost = route_cost(current_route)

    for _ in range(max_iterations):

        i, j = random.sample(range(len(cities)), 2)
        neighbor = current_route[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbor_cost = route_cost(neighbor)

        if neighbor_cost < current_cost:
            current_route, current_cost = neighbor, neighbor_cost

    return current_route, current_cost

def a_star(graph, start, goal):

    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

if __name__ == "__main__":
    # Hill Climbing Example
    cities = [0, 1, 2, 3]
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    best_route, best_cost = hill_climbing(cities, distance_matrix)
    print("Best route (Hill Climbing):", best_route)
    print("Best cost:", best_cost)

    graph = {
        (0,0): [((1,0), 1), ((0,1), 1)],
        (1,0): [((2,0), 1), ((1,1), 1), ((0,0), 1)],
        (0,1): [((0,0), 1), ((1,1), 1)],
        (1,1): [((1,0), 1), ((0,1), 1), ((2,1), 1)],
        (2,0): [((1,0), 1), ((2,1), 1)],
        (2,1): [((2,0), 1), ((1,1), 1)]
    }
    path = a_star(graph, (0,0), (2,1))
    print("Shortest path (A*):", path)
