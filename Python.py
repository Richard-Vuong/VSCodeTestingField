# Learning about print arguments (sep and end)
def arrow():
    print("    *", "   * *", "  *   *", " *     *", "***   ***", "  *   *", "  *   *", "  *****", sep="\n", end="")


# learning about literals

# this is an octal number with a decmial value equal to 83
def octal83():
    print("\n", 0o123, sep="")


# 0x123 is a hexadecimal number with a decimal = 291
def hd291():
    print(0x123)


# can use E for exponent, e.g. 3E4 = 3 * 10^4, SIMILARLY, 3E-4 = 3 * 10^-4
def threeem4():
    print(3E-4)


# threeem4()

# guess the output of the print from bidmas()
def bidmas():
    print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)


# print ("Hi " + "Lol")
'''
this is a multi line comment
lol
'''


def main():
    x = int(2)
    y = int(4)
    x = x / y
    y /= x
    print(y)


# main()

# a = 1//2

# print (a*3)


# Collatz's Hypothesis

'''Scenario
In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.

Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.


Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

Test your code using the data we've provided.'''


def Collatz():
    c0 = int(input("Enter a non-negative, non-zero integer: "))

    while c0 <= 0:
        c0 = int(input("Enter a non-negative, non-zero integer: "))

    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
            print(c0)
        else:
            c0 = 3 * c0 + 1
            print(c0)

    print("end of loop")


def stars():
    i = 0
    while i <= 5:
        i += 1
        if i % 2 == 0:
            continue
        print("*")


''' why does this code return [1,1,1,1,2,3]
list1 = [1,2,3]
for v in range (3):
    list1.insert(1,list1[v])
print(list1)

'''


# l1,l2 = [1,2,3], []

# for v in l1:
#     l2.insert(0,v)

# print(l2)


def list1():
    t = [[3 - i for i in range(3)] for j in range(3)]
    s = 0
    for i in range(3):
        s += t[i][i]
    print(s)


# list1()

'''

l1 = [[0,1,2,3,4] for i in range(2)]
print (l1[1]) #list within a list


# l1 = [[0,1,2,3] for i in range(2)]
# print (l1[2][0]) #this code results in an error as there is no l1[2], only l1[0] or l1[1]


'''

'''
for i in range(1):
    print("#")
else:
    print("#")
'''

'''

l1 = [i for i in range(-1,2)]
print(l1)

'''

'''
make a function that creates a leap year.

Leap years are years that are divisible by 4, unless they are century years,to which they must be divisible by 400. E.G. the year 2000 is a leap year (divisible by 400)
where as 1900 is not a leap year as 1900/4 results in a decimal remainder.
'''
'''

def is_year_leap(year):
#

    if (year % 4 ==0 and year % 100 !=0) or year % 400 == 0:
        return True
        
    else:
        return False



#

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

'''

'''def days_in_month(year, month):
    # List of days in each month (assuming non-leap year)
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if the provided year and month are valid
    if year < 1 or month < 1 or month > 12:
        return None
    
    # Adjust February for leap years
    if is_leap_year(year) and month == 2:
        return 29
    
    # Return the number of days for the given month
    return days_per_month[month - 1]'''

''' PRIME NUMBERS!!
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    if number == 2:
        return True  # 2 is prime
    
    if number % 2 == 0:
        return False  # Even numbers greater than 2 are not prime

    max_divisor = int(number**0.5) + 1
    for divisor in range(3, max_divisor, 2):
        if number % divisor == 0:
            return False  # Found a divisor, not prime
    
    return True  # No divisors found, prime

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
'''

'''


Using the keyword "global" to have a variable propogate outside a function


a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()
print(a)





result outputs 2 then 2 again.
'''

''' FACTORIAL FUNCTION

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # testing
    print(n, factorial_function(n))


'''

''' fibonacci /

def fib(n):
    n1,n2 = 1,1
    if n < 1:
        return None
    if n <3:
        return 1
    for x in range(3, n+1):
        n3 = n1+ n2
        n1, n2 = n2, n3
    
    return n3
    
    
for n in range(1, 10):  # testing
    print(n, "->", fib(n))
 
'''

''' fibonacci using recursion 
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


'''

'''

tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

6 is printed out, as the tuples elements are "unpacked" into the a,b,c variables.

'''

'''

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)


'''

'''
updating dictionaries

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

'''

'''converting tuples to dictionaries


colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary) 


'''

# dictionary.clear() removes all the items in the dictionary without having to delete the 
# dictionary variable itself.


'''
very VERY interesting code block with dictionaries

dictionary = {'one':'two', 'three':'one', 'two':'three'}

v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)

'''

'''
my = ['mary','had','a','little','lamb']

def my_list(my_list):
    del my_list[3]
    my_list[3]='ram'

print(my_list(my))

'''
#


'''lst = [[x for x in range(3)] for y in range(3)]
    
for r in range(3):
        for c in range(3):
            if lst[r][c] %2 !=0:
                print("#")'''

'''list = [1,2]

for v in range(2):
    list.insert(-1,list[v])

print(list)

'''


# Packages are a bunch of modules, modules are a bunch of functions
# therefore package > module > function

# import sys
#
# for p in sys.path:
#     print(p)
#
# sys.path.append('...\\modules')
#
# for p in sys.path:
#     print(p)

# # Demonstrating the rfind() method:
# print("tau tau tau".rfind("ta"))
# print("tau tau tau".rfind("ta", 9))
# print("tau tau    tau".rfind("ta", 3, 9))
#

# #%%
# # Demonstrating the rstrip() method:
# print("[" + " upsilon ".rstrip() + "]")
# print("cisco.com".rstrip(".com"))

# %%

# print(sorted(['3','1','2','3']))
# %%

# %%

# # %%
# class A:
#     def __str__(self):
#         return 'a'
#
#
# class B:
#     def __str__(self):
#         return 'b'
#
#
# class C(A, B):
#     pass
#
#
# o = C()
# print(o)


class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


class C(A, B):
    def c(self):
        self.a()


o = C()
o.c()
