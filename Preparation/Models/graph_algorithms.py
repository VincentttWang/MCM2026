import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class GraphAnalyzer:
    def __init__(self):
        self.G = nx.Graph() # Undirected by default. Use nx.DiGraph() for directed.
        
    def add_edges(self, edges):
        """
        edges: list of tuples (u, v, weight)
        """
        self.G.add_weighted_edges_from(edges)
        
    def visualize(self, title="Graph Visualization", save_path=None):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.G)
        weights = nx.get_edge_attributes(self.G, 'weight')
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', 
                node_size=500, font_size=12, font_weight='bold')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=weights)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def shortest_path(self, source, target):
        """
        Dijkstra's algorithm for shortest path.
        """
        try:
            path = nx.dijkstra_path(self.G, source, target)
            length = nx.dijkstra_path_length(self.G, source, target)
            return path, length
        except nx.NetworkXNoPath:
            return None, float('inf')

    def mst(self):
        """
        Minimum Spanning Tree (Kruskal's / Prim's).
        Returns a new GraphAnalyzer object for the MST.
        """
        T = nx.minimum_spanning_tree(self.G)
        mst_analyzer = GraphAnalyzer()
        mst_analyzer.G = T
        return mst_analyzer

    def centrality(self):
        """
        Calculates Degree, Closeness, and Betweenness centrality.
        """
        deg = nx.degree_centrality(self.G)
        close = nx.closeness_centrality(self.G)
        bet = nx.betweenness_centrality(self.G)
        return pd.DataFrame({
            'Degree': deg,
            'Closeness': close,
            'Betweenness': bet
        })

    def network_efficiency(self):
        """
        Global efficiency of the graph.
        """
        return nx.global_efficiency(self.G)

import pandas as pd

if __name__ == "__main__":
    print("--- Graph Theory Test ---")
    
    # Create graph
    model = GraphAnalyzer()
    # Edges: (u, v, weight)
    edges = [
        ('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 4),
        ('C', 'D', 1), ('B', 'D', 5), ('D', 'E', 3), ('C', 'E', 6)
    ]
    model.add_edges(edges)
    
    # 1. Shortest Path
    path, dist = model.shortest_path('A', 'E')
    print(f"Shortest path A->E: {path}, Length: {dist}")
    
    # 2. MST
    mst_model = model.mst()
    print("MST Edges:", mst_model.G.edges(data=True))
    
    # 3. Centrality
    print("\nCentrality Measures:")
    print(model.centrality())
    
    # 4. Efficiency
    print("\nGlobal Efficiency:", model.network_efficiency())
    
    print("\nVisualizing graph (check window)...")
    # model.visualize() # Blocking call, commented out for automation
