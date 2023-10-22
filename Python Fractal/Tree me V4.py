import matplotlib.pyplot as plt
import numpy as np

def generate_numbers(num_trees):
    numbers = []
    
    while len(numbers) < num_trees:
        num = np.random.randint(0, 400)
        valid = True
        
        for n in numbers:
            if abs(num - n) < 40:
                valid = False
                break
        
        if valid:
            numbers.append(num)
    
    return numbers

def draw_tree(x, y, length, angle, depth, branch_width, pause_time, leaf_start):
    shrink_factor = np.random.uniform(0.6, 0.8)
    
    if plt.get_fignums():
        
        if length < leaf_start:
            draw_leaf(x, y)
    
        if depth > 0:
            x_end = x + length * np.cos(np.radians(angle))
            y_end = y + length * np.sin(np.radians(angle))
            color_list = ['sandybrown', 'chocolate', 'saddlebrown', 'sienna', 'peru', 'burlywood']
            random_color = np.random.choice(color_list)
            plt.plot([x, x_end], [y, y_end], color=random_color, linewidth=branch_width)
            plt.pause(pause_time)

            draw_tree(x_end, y_end, length * shrink_factor, angle - 20, depth - 1, branch_width * shrink_factor, pause_time, leaf_start)

            draw_tree(x_end, y_end, length * shrink_factor, angle + 20, depth - 1, branch_width * shrink_factor, pause_time, leaf_start)
            
def draw_leaf(x, y):            
    leaf_color = ['green', 'darkgreen', 'forestgreen', 'greenyellow', 'limegreen', 'lime', 'olivedrab']
    leaf_color = np.random.choice(leaf_color)
    marker_size = np.random.randint(5, 10)
    plt.plot(x, y, marker='^', color=leaf_color, markersize=marker_size)            

def main():
    num_trees = 5
    plt.figure(figsize=(20 / 2.54, 20 / 2.54), dpi=100)
    plt.axis('off')
    
    start_x = generate_numbers(num_trees)
    start_y = generate_numbers(num_trees)
    start_positions = list(zip(start_x, start_y))
        
    trunk_length = 100
    trunk_angle = 90
    tree_depth = 10
    leaf_start = 2/ tree_depth * trunk_length
    initial_branch_width = 10
    pause_time = 0.001
    
    for start_x, start_y in start_positions:
        draw_tree(start_x, start_y, trunk_length, trunk_angle, tree_depth, initial_branch_width, pause_time, leaf_start)
    
    global total_iterations
    min_value_x = min(start_positions, key=lambda x: x[0])[0]
    max_value_x = max(start_positions, key=lambda x: x[0])[0]
    min_value_y = min(start_positions, key=lambda x: x[1])[1]
    plt.text((min_value_x + max_value_x) / 2, min_value_y - 20, f"Branch iterations: {tree_depth}", fontsize=12, color='black',
            ha='center', va='bottom')
    
    if plt.get_fignums():
        plt.show()
        
if __name__ == "__main__":
    main()
