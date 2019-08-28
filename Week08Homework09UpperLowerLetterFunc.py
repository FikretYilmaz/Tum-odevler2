#Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf sayılarının veren bir fonksiyon yazınız
def upper_lower_letter(letter):
     upper_letter=0
     lower_letter=0
     for i in letter:
         if i.isupper()==True:
             upper_letter +=1
         elif i.islower()== True:
             lower_letter +=1
     lisst=[upper_letter,lower_letter]
     print("The number of upper letters:", upper_letter)
     print("The number of lower letters::", lower_letter)

letter=input("Please type anything:")
upper_lower_letter(letter)
