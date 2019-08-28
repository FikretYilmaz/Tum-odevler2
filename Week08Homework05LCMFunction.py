def least_common_multiple (number1, number2):
    i = 1
    lcm = 1
    while (i <= number1 and i <= number2):
        if (number1 % i == 0) and (number2 % i == 0):
            lcm = i
        i += 1
    return (number1*number2) / lcm

number1 = int(input("Please enter number-1: "))
number2 = int(input("Please enter number-2: "))
print("Least common multiple :",(least_common_multiple(number1,number2)))

