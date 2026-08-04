import heapq

def uniform_cost_search(graph, initial_state, goal_state):

    initial_node = {
        "state": initial_state,
        "path": [initial_state],
        "path_cost": 0
    }

    if initial_state == goal_state:
        return initial_node["path"], initial_node["path_cost"]

    frontier = []
    heapq.heappush(frontier, (0, initial_node))

    explored = set()

    while frontier:

        current_cost, node = heapq.heappop(frontier)

        current_state = node["state"]
        current_path = node["path"]

        if current_state in explored:
            continue

        print(f"\nExpanding node: {current_state}")
        print(f"Current path: {current_path}")
        print(f"Current cost: {current_cost}")

        if current_state == goal_state:
            print(f"\nGoal State {goal_state} found!")
            return current_path, current_cost

        explored.add(current_state)

        frontier_state = {
            frontier_node["state"]
            for _, frontier_node in frontier
        }

        for child_state, cost in graph.get(current_state, []):

            if (
                child_state not in explored
                and child_state not in frontier_state
            ):

                child_node = {
                    "state": child_state,
                    "path": current_path + [child_state],
                    "path_cost": current_cost + cost
                }

                print(f"Generated child : {child_state} (Cost = {cost})")

                heapq.heappush(
                    frontier,
                    (current_cost + cost, child_node)
                )

                frontier_state.add(child_state)

        print(
            "Frontier:",
            [
                (frontier_node["state"], cost)
                for cost, frontier_node in frontier
            ]
        )

        print("Explored:", explored)

    return None, None


graph = {
    "A": [("B", 2), ("C", 4)],
    "B": [("D", 3), ("E", 5)],
    "C": [("F", 2), ("G", 3)],
    "D": [],
    "E": [("H", 2)],
    "F": [],
    "G": [("I", 4)],
    "H": [],
    "I": []
}

initial_state = "A"
goal_state = "I"

solution, cost = uniform_cost_search(
    graph,
    initial_state,
    goal_state
)

if solution is not None:
    print("\nSolution path:")
    print(" -> ".join(solution))
    print("Path cost:", cost)

else:
    print("\nFailure: No path exists.")
