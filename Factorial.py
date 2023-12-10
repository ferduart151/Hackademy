#Permitir que el usuario ingrese un numero aleatorio
fact = int (input('Ingresa el numero para obtener su factorial'))
#Recursividad
def factorial(n):
    if n==0 or n==1:
     return 1
    else: 
     return n * factorial (n-1)
    
resultado = factorial (fact)

print ('El factorial del numero ingresado es:', resultado)
