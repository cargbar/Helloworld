# Solicitar variable de  entrada
num =int(input("Igresar un numero entero: "))
# Validacion
if num>0:
# Funcion triangulo numerico    
    for i in range(1,num+1):
        for j in range (1,i+1):
            print(j,end=" ")
        print(" ")    
else:
    print("ERROR")