#Tek sayi kontrolu yapan fonksiyon
#Odd number check function
def single(number):
    if number % 2 == 1:
        return print("The number",number,"is odd")
single(5)

#Cift sayi kontrolu yapan fonksiyon
#Even number check function
def even_number(number):
    if number % 2 == 0:
        return print("The number",number,"is even")

even_number(8)

#Ucun Kati kontrolu yapan fonksiyon
#Tripple function

def tripple(number):
    if number % 3 == 0:
        return print("The number",number,"is tripple")

tripple(12)

#besin kati fonksiyonu
#Division To Five

def division_to_five(number):
    if number % 5 == 0:
        return print("The number",number,"is division to five")

division_to_five(25)

#-----------------Control Function------------------------
def control_funct(first, last):
    def single(i):
        if i % 2 == 1:
            return print("The number", i, "is odd")

    def even_number(i):
        if i % 2 == 0:
            return print("The number", i, "is even")

    def tripple(i):
        if i % 3 == 0:
            return print("The number", i, "is tripple")

    def division_to_five(i):
        if i % 5 == 0:
            return print("The number", i, "is division to five")

    for i in range(first, last):
        if single(i):
            print("The number", i, "is odd")
        if even_number(i):
            print("The number", i, "is even")
        if tripple(i):
            print("The number", i, "is tripple")
        if division_to_five(i):
            print("The number", i, "is division to five")


first = int(input("please enter first number: "))
last = int(input("please enter last number: "))
control_funct(first, last)
