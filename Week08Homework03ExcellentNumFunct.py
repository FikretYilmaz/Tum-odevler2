#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup
# olmadığını dönen bir tane fonksiyon yazın. Bir sayının, kendisi haric pozitif tam bolenleri toplami o sayiya esit ise
# mukemmel sayidir. Örnek olarak 28 mükemmel bir sayıdır (1+2+4+7+14=28).
def excellent_number(excellent):
    divide = 0
    for i in range(1,excellent):
        if excellent % i == 0:
            divide += i
    if divide == excellent:
        print(excellent,"is excelent")
        return True
    else:
        print(excellent,"is not excellent")
        return False

excellent_number2= []
for i in range(1, 1000):
    if excellent_number(i):
        excellent_number2.append(i)
print("The perfect numbers are:",excellent_number2)