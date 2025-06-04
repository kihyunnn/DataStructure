from Graph import UndiretedGraph, DiretedGraph

if __name__ == "__main__":
    # Undirected Graph
    ug = UndiretedGraph()
    ug.add_edge('A', 'B')
    ug.add_edge('B', 'C')
    ug.add_edge('B', 'D')
    ug.add_edge('C', 'F')
    ug.add_edge('C', 'G')
    ug.add_edge('D', 'E')
    ug.add_edge('D', 'F')

    print("Undirected Graph:")
    ug.print_graph()
    ug.to_adjacency_matrix()

    # Directed Graph
    dg = DiretedGraph(directed=True)
    dg.add_edge('A', 'B')
    dg.add_edge('B', 'C')
    dg.add_edge('B', 'D')
    dg.add_edge('C', 'F')
    dg.add_edge('C', 'G')
    dg.add_edge('D', 'E')
    dg.add_edge('D', 'F')

    print("\nDirected Graph:")
    dg.print_graph()
    dg.to_adjacency_matrix()