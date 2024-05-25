import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Define the colors and edges
colors = "qddqqqddqqdqddddddqdqqddddqdqdqqdddqddqdqqdqqqqqddqddqqddqqqdqqqqdqdddddqdq"
edges = [
    [0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [4, 5], [3, 6], [5, 6], [6, 7], [5, 7], [3, 7], [6, 8], [5, 8], [4, 8], 
    [8, 9], [9, 10], [10, 11], [9, 11], [9, 12], [11, 12], [6, 12], [11, 13], [9, 13], [13, 14], [12, 14], [10, 14], 
    [11, 14], [13, 15], [14, 15], [12, 16], [9, 16], [7, 16], [15, 17], [13, 17], [17, 18], [11, 18], [17, 19], 
    [18, 19], [13, 19], [17, 20], [18, 20], [19, 21], [17, 21], [12, 22], [21, 22], [16, 22], [22, 23], [21, 23], 
    [16, 24], [22, 24], [15, 25], [24, 25], [20, 25], [12, 25], [23, 26], [26, 27], [13, 27], [27, 28], [21, 28], 
    [26, 28], [28, 29], [15, 30], [27, 30], [24, 30], [21, 30], [27, 31], [30, 31], [25, 32], [29, 32], [17, 33], 
    [31, 33], [32, 33], [25, 34], [33, 35], [31, 35], [34, 35], [30, 36], [35, 37], [36, 37], [26, 38], [36, 38], 
    [34, 38], [37, 38], [38, 39], [22, 39], [39, 40], [40, 41], [38, 41], [20, 41], [41, 42], [37, 42], [40, 43], 
    [42, 43], [43, 44], [41, 44], [32, 44], [38, 44], [39, 44], [43, 45], [44, 45], [44, 46], [45, 46], [45, 47], 
    [42, 47], [43, 48], [45, 49], [45, 50], [48, 51], [30, 51], [46, 52], [48, 52], [38, 52], [51, 52], [47, 53], 
    [45, 53], [53, 54], [48, 54], [30, 54], [50, 55], [30, 55], [36, 55], [55, 56], [39, 56], [54, 56], [50, 57], 
    [56, 58], [32, 58], [57, 59], [49, 59], [38, 60], [60, 61], [35, 61], [54, 61], [53, 61], [54, 62], [58, 62], 
    [62, 63], [40, 63], [58, 63], [49, 64], [63, 64], [47, 64], [39, 64], [45, 64], [62, 65], [64, 65], [54, 65], 
    [52, 66], [61, 66], [60, 66], [55, 67], [65, 67], [45, 68], [56, 68], [36, 68], [67, 69], [66, 69], [27, 70], 
    [60, 70], [67, 70], [48, 71], [70, 71], [53, 71], [62, 72], [72, 73], [73, 74]
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes with colors
for i, color in enumerate(colors):
    G.add_node(i, color=color)

# Add edges
G.add_edges_from(edges)

# Define a color map based on the node colors
color_map = [plt.cm.viridis(ord(data['color']) - ord('a')) for node, data in G.nodes(data=True)]

# Draw the graph
plt.figure(figsize=(20, 20))
pos = nx.spring_layout(G, k=0.1)  # Position nodes using Fruchterman-Reingold force-directed algorithm
nx.draw(G, pos, node_color=color_map, with_labels=True, font_weight='bold', node_size=700, cmap=plt.cm.viridis)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u}->{v}" for u, v in edges})

plt.title("Graph Visualization")
plt.show
