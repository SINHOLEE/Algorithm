
def merge(left, right):
	temp = []
	while left and right:
		if(left[0]<= right[0]):
			temp.append(left.pop(0))
		else:
			temp.append(right.pop(0))
	temp= temp+left
	temp = temp+right
	return temp



def divide_and_conquer(lis):
	if(len(lis)==1):
		return lis
	m = len(lis) // 2
	left = divide_and_counquer(lis[:m])
	right = divide_and_counquer(lis[m:])
	return  merge(left,right)

def merge_sort(lis):
	return divide(lis)

print(merge_sort([56,3,2,1,54,454,2,34,3,2,2,1]))