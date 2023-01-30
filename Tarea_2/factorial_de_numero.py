# 
num =int(input("Igresar un numero entero:"))
if num >= 0:
    control_value=1
    iter_value=1
    while control_value <= num:
        iter_value = iter_value * control_value
        control_value += 1
        result=iter_value
    print("Factorial de " ,num,"es: ",result)
else:
    print("ERROR")