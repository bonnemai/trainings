import random
import itertools

def generate_graph_with_scc(n, m, target_scc_size):
    # First, create a strongly connected component of target_scc_size
    scc_nodes = list(range(1, target_scc_size + 1))
    edges = set()
    
    # Create a cycle in the SCC
    for i in range(target_scc_size):
        edges.add((scc_nodes[i], scc_nodes[(i + 1) % target_scc_size]))
    
    # Add remaining edges to reach m total edges
    remaining_edges = m - len(edges)
    while remaining_edges > 0:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v and (u, v) not in edges:
            edges.add((u, v))
            remaining_edges -= 1
    
    return list(edges)

def is_strongly_connected(nodes, edges):
    # Check if every node has an edge to every other node
    for u in nodes:
        for v in nodes:
            if u != v and (u, v) not in edges:
                return False
    return True

def find_smallest_scc(n, edges):
    # Create adjacency list for the graph
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
    
    # Find all possible subsets of nodes
    all_nodes = list(range(1, n + 1))
    sccs = []
    
    # Check all possible subsets of nodes
    for size in range(2, n + 1):
        for subset in itertools.combinations(all_nodes, size):
            if is_strongly_connected(subset, edges):
                sccs.append(list(subset))
    
    # Find the size of the smallest SCC
    smallest_scc_size = min(len(scc) for scc in sccs) if sccs else 0
    
    return smallest_scc_size, sccs

def find_smallest_largest_scc(n, edges):
    # Create adjacency list for the graph
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
    
    # Find all possible subsets of nodes
    all_nodes = list(range(1, n + 1))
    sccs = []
    
    # Check all possible subsets of nodes
    for size in range(2, n + 1):
        for subset in itertools.combinations(all_nodes, size):
            if is_strongly_connected(subset, edges):
                sccs.append(list(subset))
    
    # Find the size of the largest SCC
    largest_scc_size = max(len(scc) for scc in sccs) if sccs else 0
    
    return largest_scc_size, sccs

def find_min_largest_scc(n, m):
    print(f"\nFinding smallest possible size of largest SCC in graph with {n} nodes and {m} edges")
    
    # Generate all possible combinations of m edges
    all_possible_edges = list(itertools.combinations(range(1, n + 1), 2))
    min_largest_scc = n  # Start with worst case
    best_edges = None
    best_sccs = None
    
    # Try all possible combinations of m edges
    for edges in itertools.combinations(all_possible_edges, m):
        largest_scc_size, sccs = find_smallest_largest_scc(n, edges)
        if largest_scc_size < min_largest_scc:
            min_largest_scc = largest_scc_size
            best_edges = edges
            best_sccs = sccs
    
    print(f"Smallest possible size of largest SCC: {min_largest_scc}")
    
    if best_edges:
        print(f"\nExample graph achieving this minimum:")
        print(f"Edges: {best_edges}")
        print(f"Number of edges: {len(best_edges)}")
        print(f"\nStrongly Connected Components:")
        for i, scc in enumerate(best_sccs, 1):
            print(f"SCC {i}: {scc} (size: {len(scc)})")
            print(f"Edges in this SCC:")
            for u in scc:
                for v in scc:
                    if u != v and (u, v) in best_edges:
                        print(f"  {u} -> {v}")

def find_scc_with_size(n, edges, target_size):
    # Create adjacency list for the graph
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
    
    # Find all possible subsets of nodes
    all_nodes = list(range(1, n + 1))
    sccs = []
    
    # Check all possible subsets of nodes
    for size in range(2, n + 1):
        for subset in itertools.combinations(all_nodes, size):
            if is_strongly_connected(subset, edges):
                sccs.append(list(subset))
    
    # Check if we have an SCC of exactly target_size
    target_scc = None
    for scc in sccs:
        if len(scc) == target_size:
            target_scc = scc
            break
    
    return target_scc is not None, sccs

def analyze_graph_with_scc(n, m, target_size):
    print(f"\nAnalyzing graph with {n} nodes and {m} edges")
    
    # Generate all possible combinations of m edges
    all_possible_edges = list(itertools.combinations(range(1, n + 1), 2))
    best_edges = None
    best_sccs = None
    
    # Try all possible combinations of m edges
    for edges in itertools.combinations(all_possible_edges, m):
        has_target_scc, sccs = find_scc_with_size(n, edges, target_size)
        if has_target_scc:
            best_edges = edges
            best_sccs = sccs
            break
    
    if best_edges:
        print(f"\nFound graph with SCC of size {target_size}:")
        print(f"Edges: {best_edges}")
        print(f"Number of edges: {len(best_edges)}")
        print(f"\nStrongly Connected Components:")
        for i, scc in enumerate(best_sccs, 1):
            print(f"SCC {i}: {scc} (size: {len(scc)})")
    else:
        print(f"No graph found with SCC of size {target_size}")

def generate_all_graphs(n, m):
    print(f"\nGenerating all possible graphs with {n} nodes and {m} edges")
    
    # Generate all possible combinations of m edges
    all_possible_edges = list(itertools.combinations(range(1, n + 1), 2))
    graphs = []
    
    # Try all possible combinations of m edges
    for edges in itertools.combinations(all_possible_edges, m):
        graphs.append(edges)
    
    print(f"Total number of possible graphs: {len(graphs)}")
    return graphs

def analyze_graph(n, edges):
    # Find SCCs in the graph
    has_target_scc, sccs = find_scc_with_size(n, edges, 3)
    
    print(f"\nGraph edges: {edges}")
    print(f"Number of edges: {len(edges)}")
    print(f"Strongly Connected Components:")
    for i, scc in enumerate(sccs, 1):
        print(f"SCC {i}: {scc} (size: {len(scc)})")
    print("-" * 50)

def analyze_all_graphs(n, m):
    graphs = generate_all_graphs(n, m)
    
    print("\nAnalyzing all graphs:")
    for i, edges in enumerate(graphs, 1):
        print(f"\nGraph {i}:")
        analyze_graph(n, edges)

def find_graph_with_scc_size(n, m, target_size):
    print(f"\nFinding graph with {n} nodes and {m} edges where largest SCC is {target_size}")
    
    # Generate all possible combinations of m edges
    all_possible_edges = list(itertools.combinations(range(1, n + 1), 2))
    
    # Try all possible combinations of m edges
    for edges in itertools.combinations(all_possible_edges, m):
        # Create a complete subgraph of size target_size
        scc_edges = []
        for i in range(1, target_size + 1):
            for j in range(i + 1, target_size + 1):
                scc_edges.append((i, j))
        
        # Check if all required edges for the SCC are present
        if all(edge in edges for edge in scc_edges):
            # Find all SCCs in this graph
            _, sccs = find_smallest_largest_scc(n, edges)
            largest_scc_size = max(len(scc) for scc in sccs) if sccs else 0
            
            if largest_scc_size == target_size:
                print(f"\nFound graph with largest SCC of size {target_size}:")
                print(f"Edges: {edges}")
                print(f"Number of edges: {len(edges)}")
                print(f"\nStrongly Connected Components:")
                for i, scc in enumerate(sccs, 1):
                    print(f"SCC {i}: {scc} (size: {len(scc)})")
                    print(f"Edges in this SCC:")
                    for u in scc:
                        for v in scc:
                            if u != v and (u, v) in edges:
                                print(f"  {u} -> {v}")
                return edges, sccs
    
    print(f"No graph found with largest SCC of size {target_size}")
    return None, None



# Test with 3 nodes and 2 edges
# find_min_largest_scc(3, 2)
find_min_largest_scc(5,7)
