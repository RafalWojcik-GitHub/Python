import sys


if len(sys.argv) > 2 and sys.argv[1] == 'add':
    print("Wykonuje")
    a = int (sys.argv[2])
    b = int(sys.argv[3])
    c = a+b
    print("Suma:", c)
else:
    print("Uzycie ./test1 add 1 2")
