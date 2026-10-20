
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1)],
    'C': [('A', 5), ('B', 1)]
}

start = 'A'
goal = 'C'

queue = [(0, [start])]
visited = []

while queue:
    queue.sort()
    cost, path = queue.pop(0)
    node = path[-1]

    if node not in visited:
        print("\nExpanding Node:", node)
        print("Current Path:", path)
        print("Current Cost:", cost)

        visited.append(node)

        if node == goal:
            print("Frontier:", queue)
            print("Explored:", visited)
            print("Goal Found!")
            print("Path:", path)
            print("Path Cost:", cost)
            break

        for child, weight in graph[node]:
            if child not in visited:
                queue.append((cost + weight, path + [child]))

        print("Frontier:", queue)
        print("Explored:", visited)

else:
    print("No path exists")
