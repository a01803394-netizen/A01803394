EJERCICIO 1
donas=input("¿Cuantas donas tienes?")
docenas=donas//12
print(donas, "//12=", docenas)

EJERCICIO 2
num1=input("escribe un número")
num2=input("escribe otro número")
residuo= num1 % num2
print(num1, "%", num2, "=", residuo)

EJERCICIO 3
segundos=input("escribe una cantidad de segundos")
horas= segundos // 3600
minutos= (segundos % 3600) // 60
segundosrestantes= segundos % 60
print(segundos, "=", horas, "* 3600 +", minutos, "* 60 *", segundos restantes)
