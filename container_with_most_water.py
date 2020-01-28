# for every bar, 
# if the bar we are compairing it to is lower, multiply the heigh 
# of the lower bar by the distance away it is from the current bar 
# if bar we are compating it to is higher, multiple the height of
# current bar by distance from lower
# store in variable 
# if variable is greater than existing var replace it

# return existing var 

def most_water(lst):

	most = 0

	for i in range(len(lst)):

		for j in range(i + 1,len(lst)):

			if lst[i] > lst[j]:

				lowest = lst[j]

			elif lst[i] < lst[j]:

				lowest = lst[i]

			# if bars we are compairing are same height
			else:

				lowest = lst[i]

			distance = j - i

			if most < (lowest * distance):

				most = (lowest * distance)


	return most




print(most_water([1,8,6,2,5,4,8,3,7]))