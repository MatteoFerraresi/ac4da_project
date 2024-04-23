def find_top_genes_for_disease(G, disease_name):
    # Finding the node ID for the disease
    disease_id = next((node for node, attrs in G.nodes(data=True)
                       if attrs.get('name') == disease_name and attrs.get('kind') == 'Disease'), None)
    
    if not disease_id:
        print(f"Disease '{disease_name}' not found in the graph.")
        return None

    # Retrieves connected genes
    connected_genes = {neighbor: G.nodes[neighbor]['name'] for neighbor in G.successors(disease_id)
                       if G.nodes[neighbor].get('kind') == 'Gene'}

    # Calculates the degree of each connected gene
    gene_degrees = {gene_id: G.degree(gene_id) for gene_id in connected_genes.keys()}

    # Sorts genes by their degree and select the top 5
    top_genes = sorted(gene_degrees.items(), key=lambda item: item[1], reverse=True)[:5]

    # Gets gene names and their average connections
    top_genes_info = [(connected_genes[gene_id], degree) for gene_id, degree in top_genes]

    return top_genes_info

top_genes_for_breast_cancer = find_top_genes_for_disease(H, "breast cancer")
if top_genes_for_breast_cancer:
    print("Top 5 connected genes to Breast Cancer and their degrees:")
    for gene, degree in top_genes_for_breast_cancer:
        print(f"{gene}: Total Connections = {degree}")

#########################################################################################################

def find_top_connected_compounds_for_gene(G, gene_name):
    # Finds the node ID for the gene
    gene_id = next((node for node, attrs in G.nodes(data=True)
                    if attrs.get('name') == gene_name and attrs.get('kind') == 'Gene'), None)
    
    if not gene_id:
        print(f"Gene '{gene_name}' not found in the graph.")
        return None

    # Retrieves compounds that connect to this gene
    connected_compounds = {neighbor: G.nodes[neighbor]['name'] for neighbor in G.predecessors(gene_id)
                           if G.nodes[neighbor].get('kind') == 'Compound'}

    # Calculates the degree of each connected compound
    compound_degrees = {compound_id: G.degree(compound_id) for compound_id in connected_compounds.keys()}

    # Sorts compounds by their degree and select the top 5
    top_compounds = sorted(compound_degrees.items(), key=lambda item: item[1], reverse=True)[:5]

    # Gets compound names and their average connections
    top_compounds_info = [(connected_compounds[compound_id], degree) for compound_id, degree in top_compounds]

    return top_compounds_info

#########################################################################################################

top_compounds_for_PCNA = find_top_connected_compounds_for_gene(H, "PCNA")
if top_compounds_for_PCNA:
    print("Top 5 connected compounds to Gene PCNA and their degrees:")
    for compound, degree in top_compounds_for_PCNA:
        print(f"{compound}: Total Connections = {degree}")

#########################################################################################################

# Subgraph for PCNA and connected compounds
#extract_and_visualize_subgraph(H, "PCNA", "Gene", "Compound", relationship='predecessors')

# Subgraph for Bortezomib and connected side effects
#extract_and_visualize_subgraph(H, "Bortezomib", "Compound", "Side Effect", relationship='successors')

# Subgraph for Breast Cancer and its connected genes
#extract_and_visualize_subgraph(H, "breast cancer", "Disease", "Gene", relationship='successors')

#########################################################################################################

def visualize_all_paths_together(G):
    # Defining the specific nodes and their connections for visualization
    paths = [
        ("Edema", "breast cancer", "PCNA"),  # Path 1: Edema to Breast Cancer to PCNA
        ("Bortezomib", "PCNA"),              # Path 2: Bortezomib to PCNA
        ("Bortezomib", "Nausea")             # Path 3: Bortezomib to Nausea
    ]
    
    # Collecting nodes from all paths
    all_nodes = []
    for path in paths:
        node_ids = []
        for node_name in path:
            node_id = next((node for node, attrs in G.nodes(data=True) if attrs.get('name') == node_name), None)
            if not node_id:
                print(f"Node '{node_name}' not found.")
                break
            node_ids.append(node_id)
        if len(node_ids) == len(path):
            all_nodes.extend(node_ids)

    # Removes duplicates and creates a subgraph
    unique_nodes = list(set(all_nodes))
    subgraph = G.subgraph(unique_nodes)

    # Drawing the combined path
    draw_combined_paths(subgraph, paths)

def draw_combined_paths(subgraph, paths):
    # Drawing the subgraph for combined paths
    pos = nx.spring_layout(subgraph)  # Node positions
    plt.figure(figsize=(12, 10))
    nx.draw_networkx_nodes(subgraph, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_edges(subgraph, pos, edgelist=subgraph.edges(), edge_color='gray', arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_labels(subgraph, pos, labels={n: G.nodes[n]['name'] for n in subgraph.nodes()}, font_size=12)
    plt.title("Combined Paths Visualization")
    plt.show()

visualize_all_paths_together(H)
