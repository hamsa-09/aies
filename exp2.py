from collections import deque

def bfs_shortest_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

def dfs_website(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" -> ")

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_website(graph, neighbor, visited)


def main():
    print("Choose Algorithm:")
    print("1. BFS (Delivery Robot Shortest Path)")
    print("2. DFS (Website Crawling)")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":

        grid = [
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        start = (0, 0)
        goal = (4, 4)
        path = bfs_shortest_path(grid, start, goal)
        if path:
            print("Shortest Path found by BFS:", path)
        else:
            print("No path found!")

    elif choice == "2":

        website_graph = {
            "Home": ["About", "Products", "Contact"],
            "About": ["Team", "Careers"],
            "Products": ["Product1", "Product2"],
            "Contact": ["Email", "Phone"],
            "Team": [],
            "Careers": [],
            "Product1": [],
            "Product2": [],
            "Email": [],
            "Phone": []
        }
        print("DFS Website Crawling starting from 'Home':")
        dfs_website(website_graph, "Home")
        print("END")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
