from functions import *

mailString = ""

# COLORS
green = '\u001b[92m'
red = '\u001b[31m'
underline = '\u001b[4m'
yellow = "\033[93m"
reset = "\033[0m"

# file creation
f = open("AddressList.txt", "a")
f.close()

while 1:
    print(green + "--- COMANDI ---", reset)
    print("-Richiedi stringa mail dei presenti ", yellow,  "[1]", reset)
    print("-Aggiungi mail ", yellow, "[2]" + reset)
    print("-Esci dal programma ", yellow + "[1]", reset, "\n")

    userRequest = input(yellow + "Inserisci comando: " + reset)

    match userRequest:
        case '3':
            print(red, "Chiudo il programma...\n", reset)
            break
        case '1':
            print(to_string())
        case '2':
            print(add_mail())
        case _:
            print(red, "Input inserito non valido", reset)

    print("\n")
