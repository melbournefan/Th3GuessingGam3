import random

rdmb = random.randint(1, 10)
gss = "P"
ext = "H"
print("Welcome to Tha3GuessingGam3. Press the 'P' key to start playing")
while gss == "P":
    input("Type a number from 1 to 10, remember if you want to exit you can press the 'H' Key \n")
    if ext == "H":
        print("Thanks 4 playing, goodbai")
        break
    elif int(gss) > rdmb:
        print("Worng, please input a LOWER number")

    elif int(gss) < rdmb:
        print("Worng, please input a HIGHER number")

    elif int(gss) == rdmb:
        print("WINNER. You won the JackPOT LMAO")
    else:
        print("test")