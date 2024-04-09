import numpy as np

def least_cost_method(supply, demand, costs):
    m, n = supply.size, demand.size
    allocation = np.zeros((m, n), dtype=int)
    total_cost = 0

    while np.sum(supply) > 0 and np.sum(demand) > 0:
        min_cost = np.inf
        min_i, min_j = None, None

        for i in range(m):
            for j in range(n):
                if supply[i] > 0 and demand[j] > 0 and costs[i, j] < min_cost:
                    min_cost = costs[i, j]
                    min_i, min_j = i, j

        allocation[min_i, min_j] = min(supply[min_i], demand[min_j])
        total_cost += min_cost * allocation[min_i, min_j]
        supply[min_i] -= allocation[min_i, min_j]
        demand[min_j] -= allocation[min_i, min_j]

    return allocation, total_cost

# Define the cost matrix
costs = np.array([[3, 1, 7, 4],
        [2, 6, 5, 9],
        [8, 3, 3, 2]])

# Define the supply and demand
supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

result, total_cost = least_cost_method(supply, demand, costs)
print("Allocation Matrix:")
print(result)
print(f"Total Cost: {total_cost}")