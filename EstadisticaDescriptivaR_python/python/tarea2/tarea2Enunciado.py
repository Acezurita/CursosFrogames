# Tarea 2 : Adrian de la Cruz Espinosa Zurita
import math
''' Pregunta 1
Escribe una secuencia de instrucciones que permitan leer un
número real por pantalla y que muestre si el
número es positivo o no. '''

def suSigno() :
    try:
        x=(float(input( "Ingrese un número real :" )))
        if x==0:
            print("El número ", x ," no tiene signo")
        elif x>0:
            print("El número ",x," es positivo")
        elif x<0:
            print("El número ",x," es negativo")
    except TypeError:
        print("No ingreso un argumento válido")
    except ValueError:
        print("No ingreso un argumento válido")    
        
'''
Pregunta 2
Escribe una secuencia de instrucciones que permitan leer un
número real por pantalla y que muestre si el
número está en el rango entre −5 y 5, ambos incluidos.
'''
def entreCincos() :
    try:
        x=(float(input( "Ingrese un número real :" )))
        if x <=5 and x >=-5 :
            print("El número ", x ," esta en el rango -5 a 5")
        else :
            print("El número ",x," no esta en el rango -5 a 5")
    except TypeError:
        print("No ingreso un argumento válido")
    except ValueError:
        print("No ingreso un argumento válido")   
        
'''
Pregunta 3
Escribe una secuencia de instrucciones que permitan leer 
las coordenadas de un punto (x, y) e indique en
cuál de los cuatro cuadrantes se encuentra dicho punto.
Si x = 0, deberás indicar que el punto se encuentra sobre 
el eje vertical.
Si y = 0, deberás indicar que el punto se encuentra 
sobre el eje horizontal.
Si tanto x = 0 como y = 0, entonces deberás indicar
que el punto se trata del origen de coordenadas.
'''
def cuadrante() :
    try:
        print("Ingrese los valores de la cordenada ")
        x=(float(input( "Ingrese el valor del eje X :" )))
        y=(float(input( "Ingrese el valor del eje Y :" )))
        if x ==0 and y ==0 :
            print("El punto se encuentra en el origen")
        elif x==0:
            print("El punto está en el eje Vertical")
        elif y==0:
            print("El punto está en el eje horizontal")
        elif x>0 and y>0:
            print("El punto está en el primer Cuadrante")
        elif x<0 and y>0:
            print("El punto está en el segundo Cuadrante")
        elif x<0 and y<0:
            print("El punto está en el tercer cuadrante")
        elif x>0 and y<0:
            print("El punto está en el cuarto Cuadrante")
    except TypeError:
        print("No ingreso argumentos válidos")
    except ValueError:
        print("No ingreso argumentos válidos") 
        
'''
Pregunta 4
Escribe una secuencia de instrucciones que permitan 
leer dos números enteros y muestre el cociente de la
división entera y el resto de la división entera.
'''
def suCociente() :
    try:
        x=(int(input( "Ingrese el primer número entero :" )))
        y=(int(input( "Ingrese el segundo número entero :" )))
        cociente = x/y
        resto = x%y
        print("La division de ",x," entre ",y,''' da un cociente
               de : ''',cociente," con un resto de :",resto)
    except TypeError:
        print("No ingreso un número entero")
    except ValueError:
        print("No ingreso un número entero")  
        
'''
Pregunta 5
Escribe una secuencia de instrucciones que permitan leer un número
entero y determinar si es cuadrado perfecto o no 
(piensa la mejor forma de hacerlo con lo que has aprendido 
ahora).
'''
def esCuadrado() :
    try:
        x=(int(input( "Ingrese un número entero :" )))
        y=math.sqrt(x)
        if(y-math.floor(y))==0:
            print("Es un cuadrado perfecto")
        else:
            print("No es un cuadrado perfecto")
    except TypeError:
        print("No ingreso un número entero")
    except ValueError:
        print("No ingres un número entero") 
        
'''
Pregunta 6
Escribe una expresión que permita determinar si un número entero
positivo puede corresponder a un año bisiesto o no.
Se consideran años bisiestos aquellos cuyo número es divisible 
por cuatro excepto los años que son múltiplos de 100, a no ser
que lo sean de 400 (por ejemplo el año 2000 fue bisiesto 
pero el 2100 no lo será). '''
def esBisiesto() :
    try:
        x=(int(input( "Ingrese un número entero :" )))
        if(x>=0):
            if x%4 == 0 and x%100 != 0:
                print("El número ", x ," es un año bisiesto")
            elif x%400 == 0:
                print("El número ",x," es un año bisiesto")
            else:
                print("El número ",x," no es un año bisiesto")
        else: 
            print("El número no es positivo")
    except TypeError:
        print("No ingreso un argumento válido")
    except ValueError:
        print("No ingreso un argumento válido") 
        
''' Pregunta 7
Busca la imagen de un tablero de ajedrez en Google y fíjate 
en la nomenclatura de las casillas. Escribe una secuencia 
que lea una letra y un número de teclado correspondiente 
a una casilla de un tablero de ajedrez y que indique si esta
casilla es negra o blanca. '''
def suCasilla() :
    try:
        let=(input( "Ingrese la letra de la posición : " )).lower
        num=(int(input( "Ingrese el número de la posición: " )))
        if(num>0 and num <9):
            if let == 'a' or let =='c' or let =='e' or let=='g':  
                if num%2 != 0:
                    print("Casilla Negra:Posicion ",let,"-",num)
                else:
                    print("Casilla Blanca:Posicion ",let,"-",num)
            elif let == 'b' or let =='d' or let =='f' or let=='h':  
                if num%2 != 0:
                    print("Casilla Blanca:Posicion ",let,"-",num)
                else:
                    print("Casilla Negra:Posicion ",let,"-",num)
    except TypeError:
        print("No ingreso un número entero")
    except ValueError:
        print("No ingreso un número entero") 