
# This python code determines the largest palindrome number as a result of 2,3 or 4 digit numbers.
# For example for a 2 digit number the largest palindrome is 9009 and the digits are 91 and 99
# The first part of the code accepts the number of digits you would want to check with.
# The second part then iterates over that many number of digits starting from lowest value to highest
# It uses a nested loop so complexity is O(n^2)


#function to check if a given number is a palindrome
def ispalindrome(outputnum):
    return outputnum == outputnum[::-1]


print("Welcome! Find the largest paindrome number made from the product of two numbers with same number of digits")

numberofdigits = 0
palindromenumber = 0

try:
    # Accepts numbers greater than 2 digits and less than 4 digits. Any digits beyond 4 will cause performance.
    while numberofdigits < 2 or numberofdigits > 4:
        numberofdigits = int(input("Please enter the number of digits for your two numbers (upto 4 digits): "))

    seed = 0

    # set the starting value for the number of digits
    while len(str(seed)) < numberofdigits:
        seed = seed + 1

    #Setting the first number to seed as this will increment.
    firstnumber = seed

    # Loop through the numbers, incrementing the second number and multiplying with first.
    # I guess we do not need to loop through all the numbers. Might be better to start somewhere in the middle?
    while len(str(firstnumber)) < numberofdigits + 1:
        secondnumber = seed
        while len(str(secondnumber)) < numberofdigits + 1:
            multiple = firstnumber * secondnumber
            if ispalindrome(str(multiple)):
                if multiple > palindromenumber:
                    palindromenumber = multiple
                    numberone = firstnumber
                    numbertwo = secondnumber
            secondnumber = secondnumber + 1
        firstnumber = firstnumber + 1


    print(f"The largest palindrome number for {numberofdigits} digits is {palindromenumber}")
    print(f"The two numbers are {numberone} and {numbertwo}")

except ValueError:
    print("Please enter a valid natural number between 2 and 4")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Thank you for trying this code.")



