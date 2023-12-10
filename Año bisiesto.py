#Definir la funcion de bisiesto
def es_bisiesto(año):
#Definir condiciones para saber si un año es bisiesto    
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        return True
    else: 
        return False
#Solicitar al usuario que ingrese un año 
año_usuario = int (input ('Para saber si un año es bisiesto ingresa un año en formato aaaa:'))
if es_bisiesto (año_usuario):
    print ('El año', año_usuario, ' es bisiesto')
else: 
    print ('El año', año_usuario, ' no es bisiesto')