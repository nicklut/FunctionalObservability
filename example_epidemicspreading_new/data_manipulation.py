import numpy as np 
import matplotlib.pyplot as plt

def redo_numbering(arr, numbering):
    arr_new = np.zeros(arr.shape, dtype=int)
    
    for i in range(arr.shape[0]):
        arr_new[i] = np.where(numbering == arr[i])[0][0]
    
    return arr_new

def read_adj_list(fname, numbering):
    arr = [] 
    
    file1 = open(fname, 'r')
    Lines = file1.readlines()
    
    for line in Lines:
    
        arr.append(redo_numbering(np.array(line.split(), dtype=int), numbering))
    
    return arr 
        
def update_adj(adj_matrix, adj_lists):
    for list in adj_lists:
        val = list[0]
        #print(val)
        #print(list.shape)
        for i in range(1, list.shape[0]):
            adj_matrix[val, list[i]] = adj_matrix[val, list[i]] + 1
            
    
    #print(adj_matrix[7,:])
    return adj_matrix

def plot_res(X, Y):
    plt.xlabel("Target Node Set Size")
    plt.ylabel("Size Min Set of Sensor Node")
    plt.title("Number Target Nodes vs Sensor Node Set Size")
    plt.scatter(X, Y)
    plt.show()

# Alter node lists 

british_nodes = np.loadtxt('british_nodes.txt', delimiter=',')
lufthansa_nodes = np.loadtxt('lufthansa_nodes.txt', delimiter=',')
france_nodes = np.loadtxt('air_france_nodes.txt', delimiter=',')
node_numbering = np.loadtxt('node_numbering.txt')

british_new = redo_numbering(british_nodes, node_numbering)
lufthansa_new = redo_numbering(lufthansa_nodes, node_numbering)
france_new = redo_numbering(france_nodes, node_numbering)

np.savetxt('british_new.txt', british_new, fmt='%d')
np.savetxt('lufthansa_new.txt', lufthansa_new, fmt='%d')
np.savetxt('france_new.txt', france_new, fmt='%d')

# Alter adjacency lists 
france_adj_list = read_adj_list('air-france_adj_list.txt', node_numbering)
british_adj_list = read_adj_list('british_adj_list.txt', node_numbering)
lufthansa_adj_list = read_adj_list('lufthansa_adj_list.txt', node_numbering)

adj_matrix = np.zeros((node_numbering.shape[0], node_numbering.shape[0]))

#print(france_adj_list)
adj_matrix = np.zeros((node_numbering.shape[0], node_numbering.shape[0]))
adj_matrix = update_adj(adj_matrix, france_adj_list)
np.savetxt('adj_france.txt', adj_matrix, fmt='%d')

adj_matrix = np.zeros((node_numbering.shape[0], node_numbering.shape[0]))
adj_matrix = update_adj(adj_matrix, british_adj_list)
np.savetxt('adj_british.txt', adj_matrix, fmt='%d')
adj_matrix = np.zeros((node_numbering.shape[0], node_numbering.shape[0]))
adj_matrix = update_adj(adj_matrix, lufthansa_adj_list)
np.savetxt('adj_lufthansa.txt', adj_matrix, fmt='%d')



sensor_nodes = np.array([6, 2, 1, 1, 2, 2, 2, 1])
#sensor_nodes = np.array([6, 2, 1, 1,2, 2, 2, 1])
target_nodes = np.array([15, 10, 5, 1, 15, 10, 5, 1])
#candidate_nodes = np.array([106, 106, 106, 106, 65, 65, 59, 59, 59, 59])
#candidate_nodes = np.array([106, 106, 106, 106, 59, 59, 59, 59])

plot_res(target_nodes, sensor_nodes)
