#Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız.
# örnek: madam, taco cat, utrecht sonuç: True, True, False
def tersten_ayni(*letter):
    letter=input("Lutfen Herhangi bir kelime giriniz: ")
    letter=list(letter)
    for [i] in letter:
        for [k] in letter[-1]:
            if i != k:
                #print("Girdiginiz kelimenin tersten okunusu ayni degil")
                return False
        else:
            #print(letter,"kelimesinin terseten okunusu aynidir")
            return True

print(tersten_ayni())
#ey edip adanada pide ye ornek cikti.