# UTILIZANDO R COMO CALCULADORA: EJERCICIOS
# Alumno: Adrián de la Cruz Espinosa Zurita
# Pregunta 1
# Si hubiéramos empezado a contar segundos a partir de las 12 campanadas que marcan el inicio de 2018, ¿a
# qué hora de qué día de qué año llegaríamos a los 250 millones de segundos? ¡Cuidado con los años bisiestos!
# Años bisiestos 2020, 2024, 2028, 2032
# Equivalencias 1 hora = 3600 segundos 1 dia = 86400 segundos
250000000%/%86400 #2893
250000000%%86400  #44800
44800%/%3600      # 12 Horas
2893%/%365        # 7 años
2893%%365         # 338 dias 
# Respuesta
# Son 7 años, 338 dias y 12 horas . 2018 más 7 años da 2025, el día 338 de ese año es el jueves 4 de Diciembre,
# pero teniendo en cuenta los biciestos, se restan 2 días y sería el 2 de Diciembre
# Fecha Final: 12 horas del 2 de Diciembre del 2025

# Pregunta 2
# Crea una función en R que resuelva una ecuación de primer grado (de la forma Ax + B = 0). Es decir, los
# parámetros deben ser los coeficientes (en orden) y la función tiene que devolver la solución. Por ejemplo, si
# la ecuación es 2x + 4 = 0, la función tendría que devolver -2.
# Una vez creada la función, utilízala para resolver las siguientes ecuaciones de primer grado:
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

# Da una expresión para calcular 3e???pi con R y a continuación, da el resultado obtenido redondeado a 3 cifras
# decimales.
round(3^-pi,3) # 0.032

# Da una expresión para calcular el módulo del número complejo (2 + 3i)2
#                                                              (5 + 8i) 
# y, a continuación, da el resultado obtenido redondeado a 3 cifras decimales.
round(Mod(((2+3i)^2)/(5+8i)),3) #1.378

#Demostración matemática : La división da 71/89 + 100/89i y la fórmula del módulo es raíz de la suma de sus 
# cuadrados

