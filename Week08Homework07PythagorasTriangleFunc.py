#1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
def pythagoras_triangle(*args):
    lisst=[]
    for a in range(1,101):
        for b in range(1,101):
            for c in range(1,101):
              if c**2==(a**2+b**2):
                sublist=[a,b,c]
                lisst.append(sublist)
    return lisst
print(pythagoras_triangle())

