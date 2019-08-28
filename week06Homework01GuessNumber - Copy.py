import random
enter=""" 
Welcome To The Guess Number Game! The Computer is Waiting You To Guess Number in Your Mind!!
Please Pick a Number Between 1-100.
If the Guessing is Bigger Than Your Number Please Enter "-"
If the Guessing is Smaller Than Your Number Please Enter "+"
If the Guess is True Please Enter "y"
"""
print(enter)

try:
    key = None
    while key != "y" and key != "Y":
        key=input("Did you Pick The Number Y/N:")
    correct=False
    minNum = 1
    maxNum = 100
    step = 0
    while not correct:
        step+=1
        guess = random.randint(minNum, maxNum)
        print("Is Your Number", guess, "Y/N:")
        answer=input("")
        answer=answer.upper()
        if answer=="Y":
            correct=True
        else:
            answer=input("If Your Number is Bigger Than Guess Please Enter (+) or (-)")
            if answer == "+":
                minNum = guess
            elif answer == "-":
                maxNum = guess
    print("You Won At Your",step,"Try")
except ValueError:
    print("Please Enter Only Number")
