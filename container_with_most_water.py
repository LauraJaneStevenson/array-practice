 
def most_water(lst):
	"""Given n non-negative integers a1, a2, ..., an , w
	here each represents a point at coordinate (i, ai). n vertical 
	lines are drawn such that the two endpoints of line i is 
	at (i, ai) and (i, 0). Find two lines, which together with 
	x-axis forms a container, such that the container 
	contains the most water.

	Note: You may not slant the container and n is at least 2."""

	most = 0

	# nested loop to compair each bar to all other bars
	for i in range(len(lst)):

		for j in range(i + 1,len(lst)):

			# find which bar is lower
			if lst[i] > lst[j]:

				lowest = lst[j]

			elif lst[i] < lst[j]:

				lowest = lst[i]

			else:

				lowest = lst[i]

			distance = j - i

			# find amount of water
			if most < (lowest * distance):

				most = (lowest * distance)


	return most




print(most_water([1,8,6,2,5,4,8,3,7]))