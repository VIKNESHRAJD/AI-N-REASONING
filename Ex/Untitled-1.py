
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3), ('E', 5)],
    'C': [('A', 4), ('F', 2), ('G', 4)],
    'D': [('B', 3)],
    'E': [('B', 5), ('H', 3)],
    'F': [('C', 2)],
    'G': [('C', 4), ('I', 2)],
    'H': [('E', 3)],
    'I': [('G', 2)]
}

h = {
    'A': 6, 'B': 5, 'C': 4, 'D': 7,
    'E': 4, 'F': 4, 'G': 2, 'H': 3, 'I': 0
}

start = 'A'
goal = 'I'

queue = [(h[start], 0, [start])]
visited = []

while queue:
    queue.sort()
    f, g, path = queue.pop(0)
    node = path[-1]

    if node not in visited:
        print("\nExpanding Node:", node)
        print("Current Path:", path)
        print("G Cost:", g)
        print("H Cost:", h[node])
        print("F Cost:", f)

        visited.append(node)

        if node == goal:
            print("Frontier:", queue)
            print("Explored:", visited)
            print("Goal Found!")
            print("Path:", path)
            print("Path Cost:", g)
            break

        for child, cost in graph[node]:
            if child not in visited:
                new_g = g + cost
                new_f = new_g + h[child]
                queue.append((new_f, new_g, path + [child]))

        print("Frontier:", queue)
        print("Explored:", visited)

else:
    print("No path exists")
