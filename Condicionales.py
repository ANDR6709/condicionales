
#Ejercicio 3: Calculadora de Descuento

#Pide al usuario que ingrese el precio de un producto y su edad. Si el usuario tiene menos de 18 
#años, aplica un 10% de descuento al precio del producto. Si el usuario tiene 65 años o más, aplica 
#un 15% de descuento. En otros casos, no se aplica ningún descuento. Muestra el precio final 
#después del descuento.


precio=int(input("ingrese el precio"))
edad=int(input("ingrese la edad"))
if edad < 18:
    total_a_pagar=precio *0.9
    print("se aplica descuento",total_a_pagar)
elif edad >=65:
    total_a_pagar= precio*0.85
    print("se aplica descuento",total_a_pagar)
else:
    print("no aplica descuento",precio)
    
    