#EJERCICIO1
edad = int(input("Ingresa tu edad:"))
if edad <18:
  print("Eres adulto")
else:
  print("No eres adulto")

#EJERCICIO2
edad = int(input("Ingresa tu edad"))

if 13 < edad < 19:
  print("Eres adolescente")
else:
  print("No eres adolescente")

#EJERCICIO3
añoNacimiento = int(input("Ingresa tu año de nacimiento"))
añoActual = 2025
edad = añoActual - añoNacimiento
print("Tienes", edad, "años.")
