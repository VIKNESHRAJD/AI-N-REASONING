def depth_first_search(graph, initial_state, goal_state):
    initial_node = {
        "state": initial_state,
        "path": [initial_state],
        "path_cost": 0
    }

    if initial_state == goal_state:
        return initial_node["path"]

    frontier = [initial_node]
    explored = set()

    while frontier:

        node = frontier.pop()
        current_state = node["state"]
        current_path = node["path"]
        current_cost = node["path_cost"]

        if current_state in explored:
            continue

        print(f"\n Expanding node: {current_state}")
        print(f"Current path: {current_path}")

        if current_state == goal_state:
            print(f"\nGoal State {goal_state} found!")
            return current_path

        explored.add(current_state)

        frontier_state = {
            frontier_node["state"]
            for frontier_node in frontier
        }

        for child_state in graph.get(current_state, []):
            if (
                child_state not in explored
                and child_state not in frontier_state
            ):
                child_node = {
                    "state": child_state,
                    "path": current_path + [child_state],
                    "path_cost": current_cost + 1
                }

                print(f"Generated child : {child_state}")
                frontier.append(child_node)
                frontier_state.add(child_state)

        print(
            "Frontier:",
            [frontier_node["state"] for frontier_node in frontier]
        )

        print("Explored:", explored)

    return None


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H", "I"],
    "F": ["C", "I"],
    "G": ["C", "I"],
    "H": ["E"],
    "I": ["G"]
}

initial_state = "A"
goal_state = "I"

solution = depth_first_search(graph, initial_state, goal_state)

if solution is not None:
    print("\nSolution path:")
    print(" -> ".join(solution))
    print("Path cost:", len(solution) - 1)
  
else:
    print("\nFailure: No path exists.")



######OUTPUT

 '''
 Expanding node: A
Current path: ['A']
Generated child : B
Generated child : C
Frontier: ['B', 'C']
Explored: {'A'}

 Expanding node: C
Current path: ['A', 'C']
Generated child : F
Generated child : G
Frontier: ['B', 'F', 'G']
Explored: {'A', 'C'}

 Expanding node: G
Current path: ['A', 'C', 'G']
Generated child : I
Frontier: ['B', 'F', 'I']
Explored: {'A', 'C', 'G'}

 Expanding node: I
Current path: ['A', 'C', 'G', 'I']

Goal State I found!

Solution path:
A -> C -> G -> I
Path cost: 3
PS C:\Users\DSL-189\Videos\VIKNESHRAJ  AI> 
'''
