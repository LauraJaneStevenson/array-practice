def jump_game(lst):
	"""Given an array of non-negative integers, you are initially positioned at the first index of the array.
	   Each element in the array represents your maximum jump length at that position."""

	i = 0

	while i < len(lst) and lst[i] != 0:

		if i == len(lst) - 1:
			return True

		i += lst[i]

	return False

print(jump_game([2,3,1,1,4]))
print(jump_game([3,2,1,0,4]))