import heapq

def uniform_cost_search(graph, initial_state, goal_state):

    initial_node = {
        "state": initial_state,
        "path": [initial_state],
        "path_cost": 0
    }
    frontier = []
    insertion_number = 0
    heapq.heappush(frontier, (initial_node["path_cost"], insertion_number, initial_node))
    explored = set()
    frontier_cost = {initial_state: 0}

    while frontier:

        current_cost, _, node = heapq.heappop(frontier)
        current_state = node["state"]
        current_path = node["path"]

        if current_state in explored:
            continue
        if current_cost != frontier_cost.get(current_state, float('inf')):
            continue

        del frontier_cost[current_state]
        print(f"\nExpanding node: {current_state}")
        print(f"Current path: {current_path}")
        print(f"Current cost: {current_cost}")

        if current_state == goal_state:
            print(f"\nGoal State found!")
            return current_path, current_cost
        explored.add(current_state)

        for child_state, step_cost in graph.get(current_state, []):

            if child_state not in explored:
                new_cost = current_cost + step_cost
                child_node = {
                    "state": child_state,
                    "path": current_path + [child_state],
                    "path_cost": new_cost
                }

                if child_state not in frontier_cost:
                    insertion_number += 1
                    heapq.heappush(frontier, (new_cost, insertion_number, child_node))
                    frontier_cost[child_state] = new_cost
                    print(f"Added : {child_state} with cost {new_cost}")

                elif new_cost < frontier_cost[child_state]:
                    insertion_number += 1
                    heapq.heappush(frontier, (new_cost, insertion_number, child_node))
                    frontier_cost[child_state] = new_cost
                    print(f"Replaced Path to {child_state} with new cost {new_cost}")

    return None


graph = {"A": [("B", 8), ("C", 13),("D", 9)],
         "B": [("A", 8), ("H", 11)],
         "C": [("A", 13), ("G", 11),("H", 14)],
         "D": [("A", 9), ("E", 9)],
         "E": [("D", 9), ("F", 3),("G", 2)],
         "F": [("E", 3)],
         "G": [("C", 11), ("E", 2), ("H", 12)],
         "H": [("B", 11),("C", 14),("G", 12)]
         }

initial_state = "A"
goal_state = "G"

result = uniform_cost_search(graph, initial_state, goal_state)

if result is not None:
    solution_path, total_cost = result
    print("\nSolution Path:")
    print(" -> ".join(solution_path))
    print(f"Total Cost: {total_cost}")
else:
    print("\n Failure: No path exists.")



'''OUTPUT:


Expanding node: H
Current path: ['A', 'B', 'H']
Current cost: 19

Expanding node: G
Current path: ['A', 'D', 'E', 'G']
Current cost: 20

Goal State found!

Solution Path:
A -> D -> E -> G
Total Cost: 20
PS C:\Users\DSL-189\Videos\VIKNESHRAJ  AI> '''
