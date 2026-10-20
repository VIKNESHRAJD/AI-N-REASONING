
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

stack = [['A']]
visited = []

while stack:
    path = stack.pop()
    node = path[-1]

    if node not in visited:
        print("\nExpanding Node:", node)
        print("Current Path:", path)

        visited.append(node)
        

        if node == 'I':
            print("Frontier:", stack)
            print("Explored:", visited)
            print("Goal Found!")
            print("Path:", path)
            print("Path Cost:", len(path) - 1)
            break

        for child in graph[node]:
            if child not in visited:
                stack.append(path + [child])

        print("Frontier:", stack)
        print("Explored:", visited)

else:
    print("No path exists")
