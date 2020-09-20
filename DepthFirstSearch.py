def depthFirstSearch(visited, inGraph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in inGraph[node]:
            depthFirstSearch(visited, inGraph, neighbour)

if __name__ == '__main__':
    visited = set() 
    graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['G','H'],
    'E' : ['F'],
    'F' : [],
    'G' : [],
    'H' : []
    }    
    depthFirstSearch(visited, graph, 'A')