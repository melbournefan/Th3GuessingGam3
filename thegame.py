import random

rdmb = random.randint(1, 20)
answr = "S"
while answr == "S":
    gss = input("Welcome to Tha3GuessingGam3. Type a number from 1 to 20, remember if you want to exit you can press the 'H' Key \n")
    if gss == 'H':
        break

    elif int(guess) > num:
        print("Worng, please input a LOWER number")