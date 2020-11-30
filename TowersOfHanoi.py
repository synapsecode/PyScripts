#Towers Of Hanoi

c = 0
def TOH(n, F, T, A):
	"""
	n -> Number of Disks
	F -> From Rod
	T -> To Rod
	A -> Auxiliary Rod
	"""
	if(n==1):
		print("Move disk 1 from rod",F,"to rod",T)
		return
	TOH(n-1, F, A, T)
	print("Move disk", n ,"from rod", F , "to rod", T)
	TOH(n-1, A, T, F) 

n = int(input("Enter number of disks: "))
TOH(n, "A", "B", "C")
print("Number of Steps: ",  2**n - 1)