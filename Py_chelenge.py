"""#----------------------------------------#
Qestion 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""
#
#
#def generator(start, stop):
#    for i in range(start, stop):
#        if (i % 7 == 0) and (i % 5 != 0):
#            print(i, ',', end=' ')
#
#
"""#----------------------------------------#
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""
#
#
#def factorial(n):
#    total = 1
#    for i in range(2, n+1):
#        total *= i
#    return total
#
#
"""#----------------------------------------#
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""
#
#
#def dic_generator(x):
#    dic = {}
#    for i in range(1, x + 1):
#        dic[i] = i*i
#    return dic
#
#
"""#----------------------------------------#
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""
#
#
#def spliter(abc=str(input("Give coma saparated values: "))):
#    li = abc.split(',')
#    tu = tuple(li)
#    print(li)
#    print(tu)
#
#
"""#----------------------------------------#
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""


#class String5:
#
#    def __init__(self):
#        self.text = ""
#
#    def getstring(self):
#        self.text = input("Give new text: ")
#
#    def printstring(self):
#        print(self.text.upper())


"""
#----------------------------------------#
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

#def calc(d_input = input("Put coma sapareted values: ")):
#    c = 50
#    h = 30
#    result = []
#    d_input_list = d_input.split(',')
#    for d in d_input_list:
#        q = ((2 * c * float(d)) / h)**0.5
#        result.append(q)
#    return result


"""
#----------------------------------------#
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1,...,X-1; j=0,1,...,Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]"""

#def array(x, y):
#    l = []
#    for i in range(0, x):
#        l.append([])
#        for j in range(0, y):
#            l[i].append(i*j)
#    return l

"""
#----------------------------------------#
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""
values = str.split('5,10,8,1', ',')
values_listed = [int(x) for x in values]
sorted_values = sorted(values_listed)
sv2 = [str(x) for x in sorted_values]
sv3 = str.join(sv2)


print(values)
print(values_listed)
print(sorted_values)
print(sv2)
print(sv3)
