#Bir sayinin tam bolenlerini bulan fonksiyon yazınız.
#Type a function that finds the exact dividigns of the number.
def divide_number():
    #divide_list=[]
    prime = int(input("Please enter a number: "))
    divide=2
    divide_list0=[]
    count=0
    total=2
    for i in range(1,prime+1):
        if prime % i == 0:
            print(i, "are the dividing numbers")
            if i not in divide_list0:
                divide_list0.append(i)
                count+=1
        total= count*2
    else:
        divide+=1
    print("Total divide list consist of:",divide_list0, "and there are",count,"positif dividings in total and,",total,"total dividings in total.")


divide_number()
