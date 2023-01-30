def intercalar_strings (string1, string2):
    #Validacion largo de strings.
    if len(string1) != len(string2):
        print ("Los strings deben tener el mismo largo")
        return
    #Nueva variable vacia.
    new_string = " "
    #Intercalar los strings.
    for i in range(len(string1)):
        new_string += string1[i]
        new_string += string2[i]
    print(new_string)
#Definir variables strings       
string1=input("Ingresar la primera string: ") 
string2=input("Ingresar la segunda string: ") 
intercalar_strings(string1,string2)   
