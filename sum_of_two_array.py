
def main():
	n=4
	a = [1,2,3,4]
	b = [3,4,5,6]

	#solution 1
	# result = map(lambda x,y: x+y,a,b)

	#solution 2
	# result = [a for a in (x+y for x,y in zip(a,b))]
	result  = [a[i]+b[i] for i in range(n)]

	#solution 3
	# result = []
	# for i in range(n):
	# 	result.append(a[i]+b[i])

	print(result)

if __name__ == '__main__':
	main()