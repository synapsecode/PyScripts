"""
Python Patters using Loops


To get: 

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
def numberpattern1(n):
	for i in range(1, n + 1):
		for k in range(1, n - (n - i) + 1):
			print(k, end=" ")
		print()
	print()

"""
To get: 

     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5 
 """
def numberpattern2(n):
	for i in range(1, n + 1):

		for j in range(1, (n - i) + 1):
			print(end=" ")

		for k in range(1, i + 1):
			print(k, end=" ")
		print()
	print()

"""
To get:

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
def numberpattern3(n):
	for i in range(1, 5 + 1):
		for j in range(1, ((n + 1) - i) + 1):
			print(j, end=" ")
		print()
	print()

"""
To get:

1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
"""
def numberpattern4(n):
	for i in range(1, 5 + 1):
		for k in range(1, n - (n - i)):
			print(end=" ")

		for j in range(1, ((n + 1) - i) + 1):
			print(j, end=" ")
		print()
	print()
"""
To get:

 1
  1 2
   1 2 3
    1 2 3 4
     1 2 3 4 5
"""
def numberpattern5(n):
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print(end=" ")
		for k in range(1, i + 1):
			print(k, end=" ")
		print()
	print()

"""
To get:

/ / / / /
\ \ \ \ \
/ / / / /
\ \ \ \ \
"""
def slashpattern():
	for i in range(1, 5):
		if(i == 2 or i == 4):
			print("\\ \\ \\ \\ \\")
		else:
		 print("/ / / / /")
	print()
	


if __name__ == "__main__":
	numberpattern1(5)
	numberpattern2(5)
	numberpattern3(5)
	numberpattern4(5)
	numberpattern5(5)
	slashpattern()