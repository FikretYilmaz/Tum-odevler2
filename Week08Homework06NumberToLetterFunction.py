#Kullanıcıdan 2 basamaklı one sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın. Örnek: 97 ---------> Doksan Yedi
def numberto_letter(number):
    onesDigit={
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        0:""
    }
    tensDigit={
        1:"ten",
        2:"twenty",
        3:"thirty",
        4:"fourt",
        5:"fifty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety",
        0:""
    }
    specialones={
        1: "eleven",
        2: "twelwe",
        3: "thirteen",
        4: "fourteen",
        5: "fiveteen",
        6: "sixteen",
        7: "seventeen",
        8: "eighteen",
        9: "nineteen",
        0: ""
    }
    specialtens={
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        0: ""
    }
    if "11" in number or "12" in number or "13" in number or "14" in number or "15" in number or "16" in number or "17" in number or "18" in number or "19" in number:
        print(specialtens[int(number[0])] + " " + specialones[int(number[1])])
    else:
       print(tensDigit[int(number[0])] + " " + onesDigit[int(number[1])])
number=(input("Please enter a number: "))
numberto_letter(number)