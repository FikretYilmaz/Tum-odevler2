#Asal sayi olup olmadigini kontrol eden fonksiyon yazınız.
#Write a function that checks whether the entered number is a prime number.

def prime_number(prime):
    for i in range(2,prime):
        if prime % i == 0:
            return print(prime,"Is not a prime number")
    else:
        return print(prime,"Is  a prime number.")

prime=int(input("Please enter a number: "))
prime_number(prime)
