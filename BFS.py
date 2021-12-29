from queue import Queue
import networkx as nx

'''
graph = {
  1 : [2, 3, 4, 5],
  2 : [1, 3],
  3 : [1, 2, 4, 6],
  4 : [1, 3, 5, 6],
  5 : [1, 4, 6],
  6 : [3, 4, 5]
}   
'''
'''
graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ["I"],
    'E': [],
    "F": [],
    'G': [],
    "I": []
}
'''

graph = {
  1 : [2, 3],
  2 : [1, 3, 4, 5],
  3 : [4, 5, 6],
  4 : [1, 2, 3, 6],
  6 : [1, 4, 5],
  5 : [4, 6]
}


G = nx.DiGraph()
G.add_nodes_from(graph.keys())
#print(G.nodes())
for i in G.nodes():
    values = graph[i]
    #print(values)
    for j in values:
        #print('j: ', j)
        G.add_edges_from([(i,j)])
        #print('edge: ', i, j)
#print(G.edges())


def BFS(graph, start_node, target_node):
    # Set of visited nodes to prevent loops
    visited = set()
    queue = Queue()

    # Add the start_node to the queue and visited list
    queue.put(start_node)
    visited.add(start_node)
    
    # start_node has not parents
    parent = dict()
    parent[start_node] = 'No Parent'

    # Perform step 3
    path_found = False
    while not queue.empty():
        print('In Queue: ', list(queue.queue))
        current_node = queue.get()
        print('current_node: ', current_node)
        if current_node == target_node:
            path_found = True
            break
        
        print('current_node_neighbours: ', graph[current_node])

        for next_node in graph[current_node]:
            #print(next_node)
            if next_node not in visited:
                queue.put(next_node)
                visited.add(next_node)
                parent[next_node] = current_node
                print('parent: ', parent)
                
    print('Last in Queue: ', list(queue.queue))            
    # Path reconstruction
    path = []
    if path_found:
        #add target node
        path.append(target_node)
        print('path: ', path)
        while parent[target_node] is not 'No Parent':
            #add the parent of target node
            path.append(parent[target_node])
            '''
            make the target node the parent to dive in
            all parents until reach the start node
            '''
            target_node = parent[target_node]
            print('target_node: ', target_node)
        path.reverse()
    return path


path = BFS(graph, 1, 6)
#path = BFS(graph, 'A', 'I')
print('---------------------------------')
print('The way is: ', path)

colors = []
for node in G.nodes():
    if node in [n for n in path]:
        colors.append('red')
    else:
        colors.append('blue')

nx.draw(G, with_labels = True, node_size = 700, font_color = 'w'
        , node_color = colors)

import matplotlib.pyplot as plt
plt.show()
