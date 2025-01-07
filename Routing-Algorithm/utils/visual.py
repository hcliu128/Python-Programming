# By: Claude
import matplotlib.pyplot as plt
import numpy as np

def visualize_maze(maze, final_path=None, search_path=None, algo_name=None):
    """
    Visualize the maze as a grid with both the final path and search path
    maze: 2D list of the maze
    final_path: list of tuples containing final path coordinates
    search_path: list of tuples containing all searched coordinates
    """
    fig, ax = plt.subplots(figsize=(12, 12))
    
    # 原有的格子繪製代碼...
    rows, cols = len(maze), len(maze[0])
    
    # Draw the grid
    for i in range(rows + 1):
        ax.axhline(y=i, color='gray', linewidth=1)
    for j in range(cols + 1):
        ax.axvline(x=j, color='gray', linewidth=1)
    
    # Fill walls
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 0:
                ax.fill([j, j+1, j+1, j], [i, i, i+1, i+1], 'black')
    
    # [新增] 繪製搜尋路徑（用淺色標記）
    if search_path:
        for y, x in search_path:
            ax.fill([x, x+1, x+1, x], [y, y, y+1, y+1], 'lightblue', alpha=0.3)
    
    # 繪製最終路徑
    if final_path:
        path_y = [coord[0] + 0.5 for coord in final_path]
        path_x = [coord[1] + 0.5 for coord in final_path]
        ax.plot(path_x, path_y, 'g-', linewidth=3, label='Final Path')
        
        # 起點和終點
        ax.plot(path_x[0], path_y[0], 'bo', markersize=15, label='Start')
        ax.plot(path_x[-1], path_y[-1], 'ro', markersize=15, label='End')
    
    # 設置視圖屬性
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_xlim(0, cols)
    ax.set_ylim(rows, 0)
    
    # 添加座標標籤
    ax.set_xticks(np.arange(0.5, cols, 1))
    ax.set_yticks(np.arange(0.5, rows, 1))
    ax.set_xticklabels(range(cols))
    ax.set_yticklabels(range(rows))
    
    plt.title(f'Maze Grid with {algo_name} Path and Search Area')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()