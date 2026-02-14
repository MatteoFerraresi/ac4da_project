# Biomedical Graph Analysis — Hetionet Knowledge Network

## Overview
This project analyzes a biomedical knowledge graph (Hetionet) to explore relationships between entities such as diseases and symptoms.

The focus is on graph construction, similarity computation, and structural analysis using NetworkX.

---

## Dataset
- `hetionet-v1.0-nodes.tsv` — node metadata
- `hetionet-v1.0-edges.sif` — graph edges and relationships

---

## Objectives
- Load and construct a heterogeneous knowledge graph
- Explore graph composition and connectivity
- Compute similarity measures between entities
- Analyze relational proximity within biomedical networks

---

## Methods

### Graph Construction
- Parsed nodes and edges from TSV/SIF files
- Built NetworkX graph structure

### Similarity Analysis
- Jaccard similarity between nodes
- SimRank similarity for structural comparison

### Graph Exploration
- Neighborhood inspection
- Entity-level structural comparisons
- Basic connectivity analysis

---

## Technologies Used
- Python, pandas, numpy, networkx, matplotlib, collections

---

## Key Takeaways
- Built and analyzed a heterogeneous biomedical knowledge graph
- Applied similarity metrics to quantify entity relationships
- Demonstrated structural analysis on real-world scientific data
