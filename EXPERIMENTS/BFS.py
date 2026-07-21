from collections import deque

def breadth_first_search(graph, initial_state, goal_state):

    # Each node stores the current state and the path used to reach it.
    initial_node = {
        "state": initial_state,
        "path": [initial_state],
        "path_cost": 0
    }

    # Check whether the initial state itself is the goal.
    if initial_state == goal_state:
        return initial_node["path"]

    # FIFO queue contains nodes waiting to be explored.
    frontier = deque([initial_node])

    # States already explored.
    explored = set()

    while frontier:
        # Remove the shallowest node.
        node = frontier.popleft()
        current_state = node["state"]
        current_path = node["path"]
        current_cost = node["path_cost"]

        print(f"Exploring state: {current_state}")
        print(f"Current path: {current_path}")

        # Mark the current state as explored.
        explored.add(current_state)

        # States currently in the frontier
        frontier_states = {
            frontier_node["state"] for frontier_node in frontier
        }

        # Generate all the children of the current state.
        for child_state in graph.get(current_state, []):

            # Process the child only if it is neither explored nor in the frontier.
            if (
                child_state not in explored
                and child_state not in frontier_states
            ):
                child_node = {
                    "state": child_state,
                    "path": current_path + [child_state],
                    "path_cost": current_cost + 1
                }

                print(f"Generated child: {child_state}")

                # Goal Test
                if child_state == goal_state:
                    print(f"Goal state {goal_state} found!")
                    return child_node["path"]

                # Insert the child at the end of the FIFO queue.
                frontier.append(child_node)

        print("Frontier:",
              [node["state"] for node in frontier])

    # Frontier is empty, so no solution exists.
    return None


# ----------------
# DUMMY GRAPH
# ----------------

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H"],
    "F": ["C"],
    "G": ["C", "I"],
    "H": ["E"],
    "I": ["G"]
}

initial_state = "A"
goal_state = "I"

# Run BFS
solution = breadth_first_search(
    graph,
    initial_state,
    goal_state
)

# Display the Result
if solution is not None:
    print("\nSolution path:")
    print(" -> ".join(solution))
    print("Path cost:", len(solution) - 1)
else:
    print("\nFailure: No path exists.")
