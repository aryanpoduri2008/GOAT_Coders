import random


def create_maze(width, height):
    maze = [[1] * width for _ in range(height)]

    for y in range(1, height, 2):
        for x in range(1, width, 2):
            maze[y][x] = 0
            if x > 1:
                maze[y][x - 1] = 0 if random.random() < 0.5 else 1
            if y > 1:
                maze[y - 1][x] = 0 if maze[y][x - 1] == 1 or x == 1 else 1

    maze[1][0] = maze[height - 2][width - 1] = 0  # Set start and end points
    return maze


def solve_maze(maze):
    start = (1, 0)
    end = (len(maze) - 2, len(maze[0]) - 1)
    path = []
    visited = set()

    def dfs(x, y):
        if (x, y) == end:
            return True
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                path.append((nx, ny))
                if dfs(nx, ny):
                    return True
                path.pop()
        return False

    visited.add(start)
    path.append(start)
    dfs(start[0], start[1])
    return path


def print_maze(maze, path=None):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if path and (y, x) in path:
                print("*", end="")
            elif cell == 1:
                print("█", end="")
            else:
                print(" ", end="")
        print()


# Generate and solve maze
width, height = 21, 21
maze = create_maze(width, height)
solution = solve_maze(maze)

print("Generated Maze:")
print_maze(maze)
print("\nSolved Maze:")
print_maze(maze, solution)