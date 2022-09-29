import random
for i in range(5):
    number = random.randint(1,10)
    user = eval(input("Guess the number: "))
    if user == number:
        print("hurray")
        print("you guessed right it's ",number)
        break
    else:
        print("INCORRECT the number is ",number)
print("Thanks for playing!!..")