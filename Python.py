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

print ("Hi " + "Lol")
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
main()

a = 1//2

print (a*3)