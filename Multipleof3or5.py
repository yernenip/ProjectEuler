
try:
    input_value = int(input("Enter the number to which you want to get sum: "))
    output_sum = 0

    for num in range(1, input_value):
        if num%3 == 0 or num%5 == 0:
            output_sum = output_sum + num

    print(f"The sum of multiples of 3 and 5 under {input_value} is: {output_sum}")
except ValueError:
    print("Please enter a valid natural number")
except:
    print("This needs to be investigated")
else:
    print("Nice job!")


