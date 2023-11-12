
#Ejercicio 2: Clasificación de Edades

#Crea un programa que pida al usuario su edad y, según la edad proporcionada, muestre uno de los siguientes mensajes:
#Si la edad es menor de 18 años: "Eres menor de edad."
#Si la edad está entre 18 y 65 años (incluidos): "Eres un adulto."
#Si la edad es mayor de 65 años: "Eres un adulto mayor."


edad=int(input("ingrese la edad"))
if edad <18:
    print("eres menor de edad")
    if edad >18 and 65:
        print("eres un adulto")
    else:
        if edad >65:
            print("eres un adulto mayor")
            
