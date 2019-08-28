#Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.
def factorial(number):
    factor=1
    for i in range(1,number+1):
        factor *=i
    return factor
number=int(input("please enter a number: "))
print("The factorial of the",number,"is:",factorial(number))