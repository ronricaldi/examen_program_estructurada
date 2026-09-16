
n = int(input("Ingrese un numero: "))

while n <= 0:
    print("Debe ingresar un numero mayor a 0")
    n = int(input("Ingrese un numero entero positivo: "))

a = 0
b = 1
contador = 0

print(f"Los primeros {n} terminos son:")


while contador < n:
    
    if contador < n - 1:
        print(a, end=" ")
    else:
        print(a)
    
    c = a + b
    a = b
    b = c
    contador = contador + 1 