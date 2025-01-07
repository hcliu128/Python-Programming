from utils.map import MAP
from utils.visual import visualize_maze


def heuristic(a, b):
    '''
    Manhattan distance between two points a and b.
    Can be dynamically changed to other heuristics.
    '''
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_star(start, goal):
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
    
    open_set = {start}
    closed_set = set()
    search_path = []
    parents = dict() # to store the parent of each node
    parents[start] = None
    g_score = {start: 0} # cost from start along best known path
    h_score = {start: heuristic(start, goal)} # estimated cost from start to goal
    f_score = {start: 0 + heuristic(start, goal)} # f = g + h
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == goal:
            return reconstruct_path(parents, goal), search_path
        
        search_path.append(current)
        for direction in directions:
            next_x = current[0] + direction[0]
            next_y = current[1] + direction[1]
            if 0 <= next_x < len(MAP) and 0 <= next_y < len(MAP[0]) and MAP[next_x][next_y] == 1 and (next_x, next_y) not in closed_set:
                tentative_g_score = g_score[current] + 1
                if (next_x, next_y) not in g_score or tentative_g_score < g_score[(next_x, next_y)]:
                    parents[(next_x, next_y)] = (current[0], current[1])
                    g_score[(next_x, next_y)] = tentative_g_score
                    h_score[(next_x, next_y)] = heuristic((next_x, next_y), goal)
                    f_score[(next_x, next_y)] = g_score[(next_x, next_y)] + h_score[(next_x, next_y)]
                    if (next_x, next_y) not in open_set:
                        open_set.add((next_x, next_y))
        closed_set.add(current)
        open_set.remove(current)

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
    path, search_path = A_star(start, goal)
    if path:
        visualize_maze(MAP, path, search_path, 'A*')
    else:
        visualize_maze(MAP, None, search_path, 'A*')

    