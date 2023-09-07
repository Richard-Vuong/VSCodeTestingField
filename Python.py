#Learning about print arguments (sep and end)
def arrow():
    print("    *", "   * *", "  *   *"," *     *", "***   ***","  *   *","  *   *", "  *****", sep = "\n", end = "")

#learning about literals 

#this is an octal number with a decmial value equal to 83
def octal83():
    print("\n",0o123, sep="")

#0x123 is a hexadecimal number with a decimal = 291
def hd291():
    print(0x123)

#can use E for exponent, e.g. 3E4 = 3 * 10^4, SIMILARLY, 3E-4 = 3 * 10^-4
def threeem4():
    print(3E-4)

# threeem4()

#guess the output of the print from bidmas()
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
    x = x/y
    y /=x
    print(y)
# main()

# a = 1//2

# print (a*3)


#Collatz's Hypothesis

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

    while c0 !=1:
        if c0%2 == 0:
            c0 = c0/2
            print(c0)
        else:
            c0 = 3*c0+1
            print (c0)

    print("end of loop")



def  stars():
    i = 0
    while i <=5:
        i +=1
        if i %2 == 0:
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
    t = [[3-i for i in range (3)] for j in range (3)]
    s = 0
    for i in range(3):
        s+=t[i][i]
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
