from math import floor

def binary_search(lst,start,end,sought):
	print(lst[start:end])
	if abs(end-start) == 1 and lst[start] != sought:
		return "not in list"

	mid = floor((start + end)/2)


	if lst[mid] == sought:
		return mid

	if sought < lst[mid]:
		return binary_search(lst,start,mid,sought)
	if sought > lst[mid]:
		return binary_search(lst,mid,end,sought)

l = [0,1,2,3,4,5,6,7,8]
print(binary_search(l,0,len(l),90))



