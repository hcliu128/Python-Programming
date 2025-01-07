from collections import deque

from utils.map import MAP
from utils.visual import visualize_maze

def bfs(start, goal):
    '''
    MAP: 2D list, 1: path, 0: wall
    start (start_x, start_y) and goal (goal_x, goal_y) are tuples
    If exists, return the path from start to goal.
    Else, return None.
    '''
    # check if start and goal are valid
    if MAP[start[0]][start[1]] == 0:
        print("Start position is a wall")
        return None
    if MAP[goal[0]][goal[1]] == 0:
        print("Goal position is a wall")
        return None
    
    queue = deque([start])
    visited = set()
    parents = dict() # to store the parent of each node
    search_path = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    parents[(start[0], start[1])] = None
    while queue:
        current = queue.popleft()
        search_path.append(current)
        if current == goal:
            return reconstruct_path(parents, goal), search_path
        for direction in directions:
            next_x = current[0] + direction[0]
            next_y = current[1] + direction[1]
            if 0 <= next_x < len(MAP) and 0 <= next_y < len(MAP[0]) and MAP[next_x][next_y] == 1 and (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                parents[(next_x, next_y)] = (current[0], current[1])
        visited.add((current[0], current[1]))

    return None, search_path

def reconstruct_path(parents, goal):
    '''
    Reconstruct the path from start to goal using the parent dictionary
    '''
    path = []
    current = goal
    while current:
        path.append(current)
        current = parents[current]
    return path[::-1]

if __name__ == "__main__":
    start = (1, 1)
    goal = (13, 13)
    path, search_path = bfs(start, goal)
    if path:
        visualize_maze(MAP, path, search_path, 'BFS')
    else:
        visualize_maze(MAP, None, search_path, 'BFS')