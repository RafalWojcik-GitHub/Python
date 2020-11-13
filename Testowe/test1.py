import sys

try:
    if len(sys.argv) > 2 and sys.argv[1] == 'dodaj':
        a = int (sys.argv[2])
        b = int(sys.argv[3])
        c = a+b
        print("Wykonuje")
        print("Suma:", c)
    else:
        print("Uzycie ./test1 dodaj 1 2")
except:
    print("Nieprawidlowe parametry to musza byc liczby")
