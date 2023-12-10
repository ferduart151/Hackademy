print('Este programa permite determinar si una frase o palabra es un palindromo.')
print('Un palindromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.')
#Convertir la frase a minusculas y eliminar espacios 
def es_palindromo(frase):
    frase = frase.replace(' ', '').lower() 
#Comparar la frase con su inversa
    return frase == frase[::-1]
#Pedir al usuario una frase
frase_usuario= input('Escribe una frase o palabra:')
if es_palindromo(frase_usuario):
    print('La frase es un palindromo')
else:
    print('La frase no es un palindromo.')

#frase.lower(): Convierte toda la frase a minúsculas. Esto es necesario para que la comparación no sea sensible a mayúsculas/minúsculas.
#.replace(" ", ""): Elimina todos los espacios en blanco de la frase. Esto es importante porque en un palíndromo, las letras deben coincidir incluso si hay espacios entre ellas.
#frase[::-1]: Obtiene la versión invertida de la frase utilizando la técnica de "slicing" en Python.
#frase == frase[::-1]: Compara la frase original con su versión invertida. Si son iguales, la función devuelve True, lo que significa que la frase es un palíndromo; de lo contrario, devuelve False.