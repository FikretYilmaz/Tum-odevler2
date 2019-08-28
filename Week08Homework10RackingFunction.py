#Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve sonrasında bu kelimeleri harf sırasına göre dizip tekrar tire ile ayırıp
# output olarak veren bir fonksiyon yazınız. örnek girdi: green-red-yellow-black-white örnek çıktı: black-green-red-white-yellow
def ranking():
    letter=input("Please type more than one word with a hyphen (-) between: ")
    dizi=[]
    dizi=letter.split("-")
    dizi.sort()
    return print(*dizi, sep="-")
ranking()