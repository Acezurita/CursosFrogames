# UTILIZANDO R COMO CALCULADORA: EJERCICIOS
# Alumno: Adri�n de la Cruz Espinosa Zurita
# Pregunta 1
# Si hubi�ramos empezado a contar segundos a partir de las 12 campanadas que marcan el inicio de 2018, �a
# qu� hora de qu� d�a de qu� a�o llegar�amos a los 250 millones de segundos? �Cuidado con los a�os bisiestos!
# A�os bisiestos 2020, 2024, 2028, 2032
# Equivalencias 1 hora = 3600 segundos 1 dia = 86400 segundos
250000000%/%86400 #2893
250000000%%86400  #44800
44800%/%3600      # 12 Horas
2893%/%365        # 7 a�os
2893%%365         # 338 dias 
# Respuesta
# Son 7 a�os, 338 dias y 12 horas . 2018 m�s 7 a�os da 2025, el d�a 338 de ese a�o es el jueves 4 de Diciembre,
# pero teniendo en cuenta los biciestos, se restan 2 d�as y ser�a el 2 de Diciembre
# Fecha Final: 12 horas del 2 de Diciembre del 2025

# Pregunta 2
# Crea una funci�n en R que resuelva una ecuaci�n de primer grado (de la forma Ax + B = 0). Es decir, los
# par�metros deben ser los coeficientes (en orden) y la funci�n tiene que devolver la soluci�n. Por ejemplo, si
# la ecuaci�n es 2x + 4 = 0, la funci�n tendr�a que devolver -2.
# Una vez creada la funci�n, util�zala para resolver las siguientes ecuaciones de primer grado:
#  . 5x + 3 = 0
#  . 7x + 4 = 18
#  . x + 1 = 1
ecuacion <- function(a,b,c){
  (-b+c)/a
}
ecuacion(2,4,0) # -2
ecuacion(5,3,0) # -3/5  # -0.6
ecuacion(7,4,18)# 2
ecuacion(1,1,1) # 0

# Da una expresi�n para calcular 3e???pi con R y a continuaci�n, da el resultado obtenido redondeado a 3 cifras
# decimales.
round(3^-pi,3) # 0.032

# Da una expresi�n para calcular el m�dulo del n�mero complejo (2 + 3i)2
#                                                              (5 + 8i) 
# y, a continuaci�n, da el resultado obtenido redondeado a 3 cifras decimales.
round(Mod(((2+3i)^2)/(5+8i)),3) #1.378

#Demostraci�n matem�tica : La divisi�n da 71/89 + 100/89i y la f�rmula del m�dulo es ra�z de la suma de sus 
# cuadrados

