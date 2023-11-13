#Ejercicio 4: Clasificación de Notas

#Escribe un programa que solicite al usuario ingresar una puntuación (de 0 a 100) y luego muestre una calificación de acuerdo con la siguiente escala:
#90-100: "A" (sobresaliente)
#80-89: "B" (bueno)
#70-79: "C" (satisfactorio)
#60-69: "D" (necesita mejorar)
#Menos de 60: "F" (reprobado)


puntuacion=int(input("ingrese puntuacion de 0 a 100"))
if puntuacion >= 90:
    print("A -Sobresaliente")
elif puntuacion >=80 and 89:
    print("B-Bueno")
elif puntuacion >=70 and   79:
    print("C-Satisfactorio")
elif puntuacion >=60 and  69:
    print("D-Necesita mejorar")
elif puntuacion < 60:
    print("F-Reprobado")
    


