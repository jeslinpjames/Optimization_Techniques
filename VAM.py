"""
Algorithm:
1. Initialize Variables:
    - Initialize the grid with the given values.
    - Initialize supply and demand arrays.
    - Define a constant, INF, representing infinity.
    - Determine the dimensions of the grid.
    - Initialize ans (total cost) to 0.

2. Define Helper Function:
    - Define a function, findDiff(grid), to find row and column differences:
        - Initialize empty arrays rowDiff and colDiff.
        - Iterate over each row to find row differences and append to rowDiff.
        - Iterate over each column to find column differences and append to colDiff.
        - Return rowDiff and colDiff.

3. Main Loop:
    - Iterate until either supply or demand is exhausted (max(supply) == 0 or max(demand) == 0):
        - Find row and column differences using findDiff function.
        - Determine the maximum element in row and column differences.
        - If row difference max is greater than or equal to column difference max:
            - Iterate over rows:
                - Find the minimum element in the row.
                - Find the corresponding column index with the minimum element.
                - Calculate the quantity to allocate (min of supply and demand).
                - Update ans by adding quantity * minimum element.
                - Update supply and demand by subtracting the allocated quantity.
                - If demand becomes 0, mark the entire column as INF.
                - If supply becomes 0, mark the entire row as INF.
        - If column difference max is greater than row difference max:
            - Iterate over columns:
                - Find the minimum element in the column.
                - Find the corresponding row index with the minimum element.
                - Calculate the quantity to allocate (min of supply and demand).
                - Update ans by adding quantity * minimum element.
                - Update supply and demand by subtracting the allocated quantity.
                - If demand becomes 0, mark the entire column as INF.
                - If supply becomes 0, mark the entire row as INF.

4. Print the Result:
    - Print the total cost, ans.
"""
grid = [
	[3, 1, 7, 4],
    [2, 6, 5, 9],
    [8,3, 3, 2]
]
supply = [300, 400, 500] # supply
demand = [250, 350, 400, 200] # demand
INF = 10**3
n = len(grid)
m = len(grid[0])
ans = 0

# hepler function for finding the row difference and the column difference
def findDiff(grid):
	rowDiff = []
	colDiff = []
	for i in range(len(grid)):
		arr = grid[i][:]
		arr.sort()
		rowDiff.append(arr[1]-arr[0])
	col = 0
	while col < len(grid[0]):
		arr = []
		for i in range(len(grid)):
			arr.append(grid[i][col])
		arr.sort()
		col += 1
		colDiff.append(arr[1]-arr[0])
	return rowDiff, colDiff


# loop runs until both the demand and the supply is exhausted
while max(supply) != 0 or max(demand) != 0:
	# finding the row and col difference
	row, col = findDiff(grid)
	# finding the maxiumum element in row difference array
	maxi1 = max(row)
	# finding the maxiumum element in col difference array
	maxi2 = max(col)

	# if the row diff max element is greater than or equal to col diff max element
	if(maxi1 >= maxi2):
		for ind, val in enumerate(row):
			if(val == maxi1):
				# finding the minimum element in grid index where the maximum was found in the row difference
				mini1 = min(grid[ind])
				for ind2, val2 in enumerate(grid[ind]):
					if(val2 == mini1):
						# calculating the min of supply and demand in that row and col
						mini2 = min(supply[ind], demand[ind2])
						ans += mini2 * mini1
						# subtracting the min from the supply and demand
						supply[ind] -= mini2
						demand[ind2] -= mini2
						# if demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
						if(demand[ind2] == 0):
							for r in range(n):
								grid[r][ind2] = INF
						# if supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
						else:
							grid[ind] = [INF for i in range(m)]
						break
				break
	# if the row diff max element is greater than col diff max element
	else:
		for ind, val in enumerate(col):
			if(val == maxi2):
				# finding the minimum element in grid index where the maximum was found in the col difference
				mini1 = INF
				for j in range(n):
					mini1 = min(mini1, grid[j][ind])

				for ind2 in range(n):
					val2 = grid[ind2][ind]
					if val2 == mini1:
						# calculating the min of supply and demand in that row and col
						mini2 = min(supply[ind2], demand[ind])
						ans += mini2 * mini1
						# subtracting the min from the supply and demand
						supply[ind2] -= mini2
						demand[ind] -= mini2
						# if demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
						if(demand[ind] == 0):
							for r in range(n):
								grid[r][ind] = INF
						# if supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
						else:
							grid[ind2] = [INF for i in range(m)]
						break
				break

print("The basic feasible solution is ", ans)
