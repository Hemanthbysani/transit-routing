"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
from collections import defaultdict
import heapq
import copy
def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
    graph_object: variable containing network information.
    """
    try:
        filename = r'python_exam\\ChicagoSketch_net.tntp'
        with open(filename, 'r') as file:
            lines = [line.rstrip() for line in file]

        data_lines = lines[9:]
        adjacency_list = defaultdict(list)


        for line in data_lines:
            if line:
                line_as_list = line.rsplit('\t')
                init_node = int(line_as_list[1])
                term_node = int(line_as_list[2])
                length = float(line_as_list[4])
                # print(f'{init_node} {term_node} {length}')
                if init_node in adjacency_list:
                    adjacency_list[init_node].append([term_node, length])
                else:
                    adjacency_list[init_node] = [[term_node, length]]
                # adjacency_matrix[init_node][term_node] = length
        ## adjacency list is the intended graph object for q1  
        graph_object = adjacency_list
        return graph_object
    except:
        return graph_object

def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1

    minHeap = [(0, (source, []))]
    visit = set()
    while minHeap:
        w1, (n1, p1) = heapq.heappop(minHeap)
    
        
        if n1 == destination:
            shortest_path_distance =  w1
            # print(shortest_path_distance)
            print("\n\nPath taken by Dijkstra Algorithm: ",p1)
            return shortest_path_distance
        
        visit.add(n1)
        # t = max(t, w1)
        for n2, w2 in graph_object[n1]:
            if n2 not in visit:
                p2 = copy.deepcopy(p1)
                p2.append(n2)
                # print(p1, " ", n2)
                # import pdb; pdb.set_trace() 
                heapq.heappush(minHeap, (w1+w2, (n2, p2)))

