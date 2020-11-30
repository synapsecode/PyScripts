"""
@author: Manas Hejmadi
Finding the Square Root of a number using the Division method.
method: sqrt(576)
>>>
    Q: 24  //Quotient
    ___________
  2 |   5   76  //Number gets split ['00']
    | - 4       //the nearest square is subtracted
    |__________
 44 |   176        //Quotient is Doubled, and when joined with a digit, and multiplied by                
    |  -176          the same digit, should return a number smaller than or equal to it.
    |__________
    .....0.....   >/ loop runs till it is zero. if the vector runs out of numbers it
                     means that the number is not a perfect square and a pair of zeros are added.
>>>
    Therefore Square Root of 576 is 24.

Custom Accuracy is Allowed
This class tries to replicate the following.
"""

class DivisionRoot:
    # class constructor
    def __init__(self):
        # Lambda expression to check if the calculated square root is valid.
        self.__checkifSqrt = lambda n, sq: n**(1/2) == float(sq)
        # Gradient to act as a dividend for the next iteration
        self.__gradient = ""
        # Quotient
        self.__Quotient = ""
        # Remainder
        self.__Remainder = 0
        # Boolean: Number is a perfectSquare or not
        self.__isPerfectSquare = True
        # Accuracy Value for the number of decimal places
        self.__accuracy = 12
        # Point Quotient
        self.__Q = ""

# ---------------------------------------------------------------------------------------------------
    # Driver Callable function
    def sqrt(self, n, accuracy=12):

        #Handle Accuracy
        self.__accuracy = accuracy

        # Input number
        self.__n = n
        # Stores the actual number and trailing zeros to perform calculations
        self.__vector = self.__split(str(self.__n))
        # Calls the Traversing function
        self.__propagate()  # Most of the work is completed here!

        #proves that the number is a perfect square
        if(self.__Remainder == 0):
            if(self.__checkifSqrt(self.__n, self.__Quotient)):
                return float(self.__Quotient)
        else:
            return float(self.__Q)


# -------------------------------------------------------------------------------------------------------------

    # handles the case when a zero is found in the program
    def __HandleZero(self, num, update=False):
        if(not update):
            self.__Quotient += str(int(num[0]))  # Adds a zero to the quotient
        else:
            self.__Q += str(int(num[0]))

    # Traverses down the operation tree to find the next operation.
    def __propagate(self):
        self.__isPerfectSquare = True
        self.__Quotient = ""
        self.__gradient = ""
        for batch in self.__vector:
            # iterates through each digit pair in the vector
            self.__gradient += batch
            # First time, find the pure square lesser than the number
            if(batch == self.__vector[0]):
                # multiple lesser than the number
                multiple = self.__findmultiple(int(self.__gradient))
                self.__Remainder = int(self.__gradient) - \
                multiple*multiple  # remainder
                self.__Quotient += str(multiple)  # Adding to the quotient
            # Every attempt except first needs to double the quotient (call: __next)
            else:
                if(self.__Remainder == 0 and batch == '00'):  # if the remainder is 0 and batch value is 0
                    # calls the zero handler function
                    self.__HandleZero(batch)
                else:
                    # computes the next multiple
                    multiple = self.__next(self.__Quotient, self.__gradient)
                    # computes the remainder
                    self.__Remainder = int(self.__gradient) - multiple
       
            # Updating the gradient
            self.__gradient = str(self.__Remainder) # gradient = remainder at that iteration.
        if(int(self.__gradient) != 0):  # The number is not a perfect square
            self.__alpha()  # calls the function to process the non perfect squares

    def __alpha(self):
        self.__isPerfectSquare = False  # setting the perfect square boolean to false
        # adding a decimal point to the auxiliary quotient
        self.__Q = self.__Quotient + "."
        self.__vector = []  # clear the vector as any of the previous values wont be used
        # loop as many times as the specified decimal accuracy.
        for _ in range(self.__accuracy):
            # Add a pair of zeros as per the division algorithm.
            self.__vector += ['00']
        for batch in self.__vector:  # iterates over the new zero list.
            # concatenates the batch and the gradient.
            self.__gradient += batch
            # Optimization and Decimal Tresholding
            if(self.__Remainder != 0):
                multiple = self.__next(
                    self.__Quotient, self.__gradient, update=True)
                self.__Remainder = int(self.__gradient) - multiple
            else:
                self.__HandleZero(batch, update=True)
            self.__gradient = str(self.__Remainder)

    # Function to generate the next Dividend
    def __next(self, quotient, n, update=False):
        temp = ""  # temporary placeholder
        temp += str(int(quotient)*2)  # doubles the quotient
        Q = ""  # Temporary quotient
        x = []  # Empty List
        # loop through digits 0-9 paired with the temp to get next dividend.
        for i in range(0, 10):
            number = int(temp + str(i))  # create the number
            if((number*i) <= int(n)):  # check condition
                x.append(number*i)  # append the multiple
                Q = str(i)  # update temporary quotient
            else:  # if the condition fails once it will never satisfy it again
                break  # terminates the loop
        self.__Quotient += Q  # updates the global quotient
        if(update):
            self.__Q += Q
        return int(x[-1])  # returns the next Dividend

    # Private Function to split the number into pairs of 2 from the ones place.
    def __split(self, s):
        if(len(s) % 2 == 0):  # if string is even length split into even pairs
            o = []  # declaring empty list
            while s:  # iterate until len(s) == 0 i.e (s exists)
                o.append(s[:2])  # append the last 2 elements
                s = s[2:]  # remove 2 elements
            return o  # return new vector
        # if string is not of even length, split into 1 lone pair + even pairs.
        else:
            x = s[0]
            s = s[1:]  # storing the first value of the string and deleting it.
            split = self.__split(s)  # holding the current vector: Recursion
            o = [x]  # Adding the stored value
            for i in split:  # iterating over the new vector
                o.append(i)
            return o  # returning new vector

    # Private: Finds the smallest number whose square is smaller than the dividend.
    def __findmultiple(self, n):
        x = []  # Empty list to store all the values
        for i in range(0, n + 1):  # Loops through all the numbers below it
            if((i*i) <= n):  # If the square of i is lesser than or equal to
                x.append(i)  # Adds the value of i to the list
            else:  # once the condition is false it isnt necessary to check other iterations
                break  # exits loop
        return int(x[-1])  # returns the last element in the list.



def newton_root(n):
    a = 0.000000000000001
    x = n
    count = 0
    while(True):
        count +=1 
        root = 0.5 * (x + (n / x))
        if (abs(root - x) < a) : 
            break 
        x = root
    return x

def babylonian_root(n):
    x = n
    y = 1
    e = 0.000000000000001
    while(x - y > e):
        x = (x + y)/2
        y = n/x
    return x

# --------------------------------------Driver Code-------------------------------------------------
if(__name__ == "__main__"):
    dqrt = DivisionRoot()
    n = int(input("Enter the number: "))
    import timeit
    import math

    t1 = timeit.timeit()
    gt = math.sqrt(n)
    t2 = timeit.timeit()

    t3 = timeit.timeit()
    dr = dqrt.sqrt(n, accuracy=16)
    t4 = timeit.timeit()

    t5 = timeit.timeit()
    nr = newton_root(n)
    t6 = timeit.timeit()

    t7 = timeit.timeit()
    br = babylonian_root(n)
    t8 = timeit.timeit()

    gd = t2-t1
    dd = t4-t3
    nd = t6-t5
    bd = t8-t7

    # print(f"Ground Truth: {gt} T[{gd}]")
    # print(f"Division Root: {dr} T[{dd}]")
    # print("Newton Root:", nr, f"T[{nd}]")

    from prettytable import PrettyTable
    table = PrettyTable(['Algorithm', 'N', 'Result', 'Time'])
    L = [
        ["Math SQRT", n, gt, abs(gd)],
        ["Division Root", n, dr, abs(dd)],
        ["Newton Root", n, nr, abs(nd)],
        ["Babylonian Root", n, br, abs(bd)],
    ]

    for rec in L:
        table.add_row(rec)

    print(table)