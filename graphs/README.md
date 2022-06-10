# Graphs
<!-- Short summary or background information -->
- Graph is a non linear data structure.
- Graph consist of nodes that connected to each other by edges.

## Challenge
<!-- Description of the challenge -->
### Features
- Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- **add node**
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph

- **add edge**
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph

- **get nodes**
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)

- **get neighbors**
  - Arguments: node
  - Returns a collection of edges connected to the given node
    - Include the weight of the connection in the returned collection
- **size**
  - Arguments: none
  - Returns the total number of nodes in the graph

### Testing
Write tests to prove the following functionality:

  - Node can be successfully added to the graph
  - An edge can be successfully added to the graph
  - A collection of all nodes can be properly retrieved from the graph
  - All appropriate neighbors can be retrieved from the graph
  - Neighbors are returned with the weight between nodes included
  - The proper size is returned, representing the number of nodes in the graph
  - A graph with only one node and edge can be properly returned
  - An empty graph properly returns null

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Time BigO(n)
- Space BigO(n)

## API
<!-- Description of each method publicly available in your Graph -->
  - **Add node**: Create a new node object and add it to the adjacency list, and return it.
  - **Add Edge**: Connects two nodes and add weight to the edge (optionally).
  - **Get nodes**: Return all nodes in the adjacency list.
  - **Get neighbors**: Return all nodes that connect to specific node.
  - **Size** : Return how many nodes the graph contains.