#Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
# Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]
ornek_liste = [1,2,3,3,3,3,4,5,5]
def unigues():
    liste=input("Listenin elemanlarini arasinda bosluk birakarak yaziniz giriniz: ")
    liste=list(liste.split(" "))
    liste2=[]
    for i in liste:
        if i not in liste2:
            liste2.append(i)
    return liste2
print(unigues())