"""
ODEV 3: pzt = [ { isim: 'Fonksiyonlara calis', sure: 180, }, { isim: 'ornek coz', sure: 120, }, { isim: 'odev kontrol', sure: 20, }, { isim: 'bayramlasma', sure: 200, } ]

sali = [ { isim: 'gelecek haftaya hazirlik', sure: 240, }, { isim: 'ornek cozumlerine devam et', sure: 180, }, { isim: 'kahve molasi', sure: 10, }, { isim: 'kitap oku', sure: 200, }, { isim: 'spor yap', sure: 40, } ]

Not: Sureler dakika cinsindendir!

Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan neticesinde kac puan kazanilacagini hesaplayan bir program yaziniz.

•	Map ile sureleri saat cinsine donusturun.
•	Iki saatin altindaki tum rutinleri filter ile eleyin.
•	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin.
•	Kusurlu degerleri .round() ile yuvarlayin.
•	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
•	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin.
"""
from functools import reduce
pzt = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180, }, { 'isim': 'ornek coz', 'sure': 120, },
        { 'isim': 'odev kontrol','sure': 20, }, { 'isim': 'bayramlasma', 'sure': 200, }, ]
sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240, }, { 'isim': 'ornek cozumlerine devam et', 'sure': 180, },
         { 'isim': 'kahve molasi', 'sure': 10, }, { 'isim': 'kitap oku', 'sure': 200, }, { 'isim': 'spor yap', 'sure': 40, }, ]

list_share=[]

for i in range(len(pzt)):
   list_share.append(pzt[i]['sure'])
for i in range(len(sali)):
   list_share.append(sali[i]['sure'])
#print(list_share)
#print(list(map(lambda x:round(x/60,1),list_share)))
#print(list(filter(lambda t: t >= 2,list(map(lambda x:round(x/60,1),list_share)))))
#print(list(map(lambda a:a*20 ,list(filter(lambda t: t >= 2,list(map(lambda x:round(x/60,1),list_share)))))))
#print(list(map(lambda k:round(k),list(map(lambda a:a*20 ,list(filter(lambda t: t >= 2,list(map(lambda x:round(x/60,1),list_share)))))))))
print("The total points is:",reduce(lambda b,r:b+r,(list(map(lambda k:round(k),list(map(lambda a:a*20 ,list(filter(lambda t: t >= 2,list(map(lambda x:round(x/60,1),list_share)))))))))))
