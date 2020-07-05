
def ispalindrome(outputnum):
    return outputnum == outputnum[::-1]


print("Welcome! Find the largest paindrome number made from the product of two numbers with same number of digits")

numberofdigits = 0
palindromenumber = 0

while numberofdigits < 2 or numberofdigits > 4:
    numberofdigits = int(input("Please enter the number of digits for your two numbers (upto 4 digits): "))

seed = 0

while len(str(seed)) < numberofdigits:
    seed = seed + 1


while len(str(seed)) < numberofdigits + 1:
    secondnumber = seed
    while len(str(secondnumber)) < numberofdigits + 1:
        multiple = seed * secondnumber
        if ispalindrome(str(multiple)):
            palindromenumber = multiple
            numberone = seed
            numbertwo = secondnumber
        secondnumber = secondnumber + 1
    seed = seed + 1


print(f"The largest palindrome number for {numberofdigits} digits is {palindromenumber}")
print(f"The two numbers are {numberone} and {numbertwo}")



