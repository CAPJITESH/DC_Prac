"""
This program simulates a load balancing algorithm to manage processes across nodes in a distributed system.

1. Add a Process:
   - Identify the node with the least load (fewest assigned processes).
     Formula: `node = get_least_loaded_node(loads)`
   - Add a process to the node by increasing its load by 1.
     Formula: `loads[node] += 1`
   - This helps balance the load and avoid overloading any single node.

2. Remove a Process:
   - The user specifies the node ID from which a process should be removed.
   - If the node exists and has processes assigned, decrease the load by 1.
     Formula: `loads[node_id] -= 1`
   - If the node has no processes or does not exist, an error message is displayed.

3. Add a Node:
   - A new node is added with an ID that's one greater than the current highest node ID.
     Formula: `new_id = max(loads.keys()) + 1 if loads else 0`
   - Initialize the load of the new node to 0.
     Formula: `loads[new_id] = 0`
   - Redistribute processes across all nodes to maintain load balance:
     Formula: 
     - Calculate the total processes: `total_processes = sum(loads.values())`
     - Calculate the load per node: `load_per_node = total_processes // len(loads)`
     - Distribute remaining processes: `remaining = total_processes % len(loads)`
   - Redistributing ensures that the load is evenly spread across all nodes.

4. Remove a Node:
   - The user specifies the node ID to be removed.
   - If the node exists, remove its load and redistribute its processes across the remaining nodes.
     Formula:
     - If processes exist on the node, redistribute them: 
       `redistribute_processes(loads)`
   - If the node has no processes or there are no processes to redistribute, the system displays a message.

5. Exit:
   - This option allows the user to exit the simulation and terminate the program.
     Formula: `break`
   - Stops the menu loop and ends the load balancing simulation.

### Main Goal:
The main goal of this simulation is to manage and balance the load between different nodes, ensuring that no single node becomes overloaded. This is achieved through:
- Assigning processes to the node with the least load.
- Redistributing processes whenever nodes are added or removed to maintain a balanced load across all nodes.
- The formulas and methods used ensure optimal system efficiency and prevent any node from becoming a bottleneck.

"""

def display_menu():
    print("\n--- Load Balancer Menu ---")
    print("1. Add a Process")
    print("2. Remove a Process")
    print("3. Add a Node")
    print("4. Remove a Node")
    print("5. Exit")

def get_least_loaded_node(loads):
    return min(loads, key=loads.get)

def redistribute_processes(loads):
    total_processes = sum(loads.values())
    nodes_count = len(loads)
    avg_load = total_processes // nodes_count
    remaining_processes = total_processes % nodes_count

    # Distribute the processes evenly
    for node in loads:
        loads[node] = avg_load

    # Distribute remaining processes to the first few nodes
    nodes = list(loads.keys())
    for i in range(remaining_processes):
        loads[nodes[i]] += 1

# Initial configuration
loads = {0: 4, 1: 3, 2: 3}

while True:
    print("\nCurrent Load Distribution:", loads)
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        # Add a process to the least loaded node
        node = get_least_loaded_node(loads)
        loads[node] += 1
        print(f"Process added to Node {node}.")

    elif choice == '2':
        # Remove a process from a specified node
        try:
            node_id = int(input("Enter node ID to remove a process from: "))
            if node_id in loads and loads[node_id] > 0:
                loads[node_id] -= 1
                print(f"Process removed from Node {node_id}.")
            else:
                print("Invalid node or no process to remove.")
        except ValueError:
            print("Invalid input.")

    elif choice == '3':
        # Add a new node with 0 initial load
        new_id = max(loads.keys()) + 1 if loads else 0
        loads[new_id] = 0
        print(f"Node {new_id} added with 0 load.")
        
        # Redistribute the load across all nodes
        redistribute_processes(loads)
        print("Load has been redistributed across all nodes.")

    elif choice == '4':
        # Remove a node and redistribute its processes
        try:
            node_id = int(input("Enter node ID to remove: "))
            if node_id in loads:
                removed_load = loads.pop(node_id)
                if loads:
                    redistribute_processes(loads)
                    print(f"Node {node_id} removed. Its processes redistributed.")
                else:
                    print("All nodes removed. No redistribution possible.")
            else:
                print("Node ID not found.")
        except ValueError:
            print("Invalid input.")

    elif choice == '5':
        print("Exiting Load Balancer Simulation.")
        break

    else:
        print("Invalid choice. Please try again.")
