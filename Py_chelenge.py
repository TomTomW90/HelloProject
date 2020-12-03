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

# values = str.split('without,hello,bag,world', ',')
# values_listed = sorted(values)
# values_sorted = ','.join(values_listed)
#
# items=[x for x in raw_input().split(',')]
# items.sort()
# print ','.join(items)

"""
#----------------------------------------#
Question 9
Level 2

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

# lines = []
# while True:
#     s = raw_input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
#
# for sentence in lines:
#     print sentence

"""
#----------------------------------------#
Question 10
Level 2

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

# values = "hello world and practice makes perfect and hello world again"
# values_list = [word for word in values.split()]
# print(" ".join(sorted(set(values_list))))

"""
#----------------------------------------#
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""

"""
#----------------------------------------#
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

# values = [num for num in range(1000, 3001)]
# values_new = [num for num in range(1000, 3001)]
# for number in values:
#     for digit in str(number):
#         if int(digit) % 2 != 0:
#             try: values_new.remove(int(number))
#             except ValueError:
#                 pass
# values_new_as_str = [str(num) for num in values_new]
# print(','.join(values_new_as_str))

"""
#----------------------------------------#
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
# sentence = "hello world! 123"
# total_letters = 0
# total_digits = 0
#
# for mark in sentence:
#     if mark.isalpha():
#         total_letters += 1
#     elif mark.isdigit():
#         total_digits += 1
#
# print("LETTERS: {}\nDIGITS: {}".format(total_letters, total_digits))

"""
#----------------------------------------#
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

# sentence = "Hello world!"
# d = {'UPPER CASE': 0,
#      'LOWER CASE': 0}
#
# for mark in sentence:
#     if mark.isupper():
#         d['UPPER CASE'] += 1
#     elif mark.islower():
#         d['LOWER CASE'] += 1
#     else:
#         pass
#
# print("Upper case: {}\nLower case: {}".format(d['UPPER CASE'], d['LOWER CASE']))

"""
#----------------------------------------#
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""
# d = 9
#
# def compute(digit):
#     total = digit + digit*11 + digit*111 + digit*1111
#     return total
#
# print(compute(d))

"""
#----------------------------------------#
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""
# sequance = "1,2,3,4,5,6,7,8,9"
# values = [int(num)**2 for num in sequance.split(',') if int(num) % 2 != 0]

"""
#----------------------------------------#
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""
