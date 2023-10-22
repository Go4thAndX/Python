# TODO Hoe pas ik de code aan zodat aan delen van de boom een blad wordt getekend ?

import matplotlib.pyplot as plt
import numpy as np

total_iterations = 0

def draw_tree(x, y, length, angle, depth, branch_width, pause_time, leaf_start):
    global total_iterations
    if length < leaf_start:
        draw_leaf(x, y)
    
    if plt.get_fignums():

        if depth > 0:
            x_end = x + length * np.cos(np.radians(angle))
            y_end = y + length * np.sin(np.radians(angle))
            color_list = ['brown', 'sandybrown', 'chocolate', 'saddlebrown', 'sienna', 'peru', 'burlywood']
            random_color = np.random.choice(color_list)
            plt.plot([x, x_end], [y, y_end], color=random_color, linewidth=branch_width)
            total_iterations += 1
            plt.pause(pause_time)

            draw_tree(x_end, y_end, length * 0.7, angle - 20, depth - 1, branch_width * 0.7, pause_time, leaf_start)

            draw_tree(x_end, y_end, length * 0.7, angle + 20, depth - 1, branch_width * 0.7, pause_time, leaf_start)


            
def draw_leaf(x, y):            
    leaf_color = ['green', 'darkgreen', 'forestgreen', 'greenyellow', 'limegreen', 'lime', 'olivedrab']
    leaf_color = np.random.choice(leaf_color)
    plt.plot(x, y, marker='^', color=leaf_color, markersize=15)            

def main():
    plt.figure(figsize=(20 / 2.54, 20 / 2.54), dpi=100)
    plt.axis('off')
    start_x = 0.0
    start_y = 0.0
    trunk_length = 100
    trunk_angle = 90
    tree_depth = 6
    leaf_start = 1.5 / tree_depth * trunk_length
    print(leaf_start)
    initial_branch_width = 10
    pause_time = 0.1
    draw_tree(start_x, start_y, trunk_length, trunk_angle, tree_depth, initial_branch_width, pause_time, leaf_start)
    global total_iterations
    plt.text(0, -20, f"Tree depth: {tree_depth} Total Iterations: {total_iterations}", fontsize=12, color='black',
            ha='center', va='bottom')
    
    if plt.get_fignums():
        plt.show()

if __name__ == "__main__":
    main()
