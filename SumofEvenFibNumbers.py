try:
    input_value = int(input("Enter the not to exceed fibonnaci number: "))
    output_sum = 0
    fib_prev_num = 0
    fib_num = 1

    while(fib_num < input_value):
        if(fib_num%2 == 0):
            output_sum = output_sum + fib_num
        temp_num = fib_num
        fib_num = fib_num + fib_prev_num
        fib_prev_num = temp_num
    
    print(f"The sum of even fibonacci numbers is: {output_sum}")
except ValueError:
    print("Please enter a valid natural number")
except:
    print("This needs to be investigated")
else:
    print("Nice job!")