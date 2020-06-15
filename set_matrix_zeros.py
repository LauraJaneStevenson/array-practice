def set_matrix_zeros(grid):

	indices = []
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:

				indices.append((i,j))

	for index in indices:

		for i in range(len(grid)):
			for j in range(len(grid[0])): 

				if i == index[0] or j == index[1]:

					grid[i][j] = 0

	return grid

grid = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

print(set_matrix_zeros(grid))
