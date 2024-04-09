import numpy as np

def least_cost_method(cost_matrix, supply, demand):
    num_rows = len(supply)
    num_cols = len(demand)
    allocation = np.zeros((num_rows, num_cols))

    while True:
        min_cost = float('inf')
        min_row = -1
        min_col = -1

        # Find the cell with the lowest transportation cost
        for i in range(num_rows):
            for j in range(num_cols):
                if cost_matrix[i][j] < min_cost and supply[i] > 0 and demand[j] > 0:
                    min_cost = cost_matrix[i][j]
                    min_row = i
                    min_col = j

        # If no cell can be allocated, break
        if min_row == -1:
            break

        # Allocate as much as possible from the cell
        allocation_amount = min(supply[min_row], demand[min_col])
        allocation[min_row][min_col] = allocation_amount

        # Update supply and demand
        supply[min_row] -= allocation_amount
        demand[min_col] -= allocation_amount

        # Remove row or column if allocation is complete
        # if supply[min_row] == 0:
        #     supply[min_row] = 10**9  # Replace with a very large integer
        # if demand[min_col] == 0:
        #     demand[min_col] = 10**9  # Replace with a very large integer

    return allocation

# Example usage:
cost_matrix = np.array([
    [3, 1, 7,4],
    [2, 6, 5,9],
    [8, 3, 3,2]
])

supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400,200])

allocation = least_cost_method(cost_matrix, supply, demand)
print("Allocation Matrix:")
print(allocation)