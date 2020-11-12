import sys # przekazanie argumentow


names = []
if len(sys.argv) > 2 and sys.argv[1] == 'add':
    names = sys.argv[2:]
    print("Wykonuje")
    a = int (sys.argv[2])
    b = int(sys.argv[3])
    c = a+b
    print("Suma:", c)
else:
    print("Uzycie ./pythonARGV add 1 2")




'''    
for n in names:
    print (n, 'Powodzenie')
'''


'''
add = 0.0
  
n = len(sys.argv) 
  
for i in range(1, n): 
    add += str(sys.argv[i]) 
  
print ("the sum is :", add) 
'''
