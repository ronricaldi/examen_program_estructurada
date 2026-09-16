

n= int(input("Ingrese un numero: "))

for n in range (1, n+1):
    for tabla in range (1,13):
        resultado= n * tabla
        print (n,"x",tabla,"=",resultado)
        
        