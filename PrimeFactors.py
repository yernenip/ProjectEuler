try:
    unfactored_number = int(input("Enter the number you wish to factorize: "))
    divisor = 2
    prime_numbers = []

    while prime_numbers.count(int(unfactored_number)) == 0:
        if unfactored_number < divisor:
            break
        elif unfactored_number%divisor == 0:
            unfactored_number = unfactored_number/divisor
            prime_numbers.append(int(divisor))
        else:
            divisor = divisor + 1
        
    print(f"The prime factors are {prime_numbers}")
    print(f"The largest prime number is {prime_numbers[-1]}")


except ValueError:
    print("Please enter a valid natural number")
except:
    print("This needs to be investigated")
else:
    print("All done!")