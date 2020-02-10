

def product_except_self(nums):

	output = []
	

	for i in range(len(nums)):
		product = 1

		for j in range(len(nums)):

			if i != j:

				product = product * nums[j]

		output.append(product)

	return output


print(product_except_self([1,2,3,4]))