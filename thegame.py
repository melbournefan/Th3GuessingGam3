import random

rdmb = random.randint(1, 10)
gss = "P"
ext = "H"
input("Welcome to Tha3GuessingGam3. Press the 'P' key to start playing")
while gss == "P":
    ext = input("Type a number from 1 to 10, remember if you want to exit you can press the 'H' Key \n")
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




        ##DATA Dictonary
        ## import = import a library, this can be a 'code helper' that imports code to help with the code
        ## rdmb, gss, ext = dictonary functions, these define a word to then later put in the code later, in this case rdmb points to a function that points to the random library
        ## gss and ext point to a keyboard function
        ## print = this prints text to the screen when the program is first opened
        ## while = a while command then 