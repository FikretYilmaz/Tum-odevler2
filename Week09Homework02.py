#ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve hepsini toplayip sonucu veren
# bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz.
#Write a function that multiplies the odd elements of a given list of numbers by two and returns all of them.
# Use map, filter and reduce.
from functools import reduce
lisst=[1,2,3,4,5,6,7,8,11,33,54]
#lisst= list(filter(lambda a:a%2 == 1,lisst))
#print(lisst)

#lisst=list(map(lambda a:a*2,(list(filter(lambda a:a%2 == 1,lisst)))))
#print(lisst)

#reduce(lambda b,c:b+c,(list(map(lambda a: a*2,(list(filter(lambda a:a%2 == 1,lisst)))))))

print(reduce(lambda b,c:b+c,(list(map(lambda a:a*2,(list(filter(lambda a:a%2==1,lisst))))))))