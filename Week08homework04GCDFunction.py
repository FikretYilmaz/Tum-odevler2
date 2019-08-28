def greatest_common_divisor(number1, number2):
    i = 1
    gcd = 1
    while (i <= number1 and i <= number2):
        if (number1 % i == 0) and (number2 % i == 0):
            gcd = i
        i += 1
    return gcd

number1 = int(input("Please enter number-1: "))
number2 = int(input("Please enter number-2: "))
print("Greatest common divisor:", greatest_common_divisor(number1,number2))