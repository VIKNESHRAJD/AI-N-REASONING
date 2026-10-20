
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

start = 'A'
goal = 'I'

queue = [[start]]
visited = []

while queue:
    path = queue.pop(0)
    node = path[-1]

    if node not in visited:
        print("\nExpanding Node:", node)
        print("Current Path:", path)

        visited.append(node)

        if node == goal:
            print("Frontier:", [p for p in queue])
            print("Explored:", visited)
            print("Goal Found!")
            print("Path:", path)
            print("Cost:", len(path) - 1)
            break

        for child in graph[node]:
            if child not in visited:
                queue.append(path + [child])

        print("Frontier:", queue)
        print("Explored:", visited)

else:
    
    print("No path exists")
