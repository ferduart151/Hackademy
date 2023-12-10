# Instrucciones al usuario
dato = input ('Para calcular el volumen de una esfera, introduce el radio o el diametro')
#Convertir string a float
dat = float (dato)
#Solicitar si es diametro o radio
var = input ('¿Es radio o diámetro? ').lower()
if var == 'radio':
   volrad = (4 / 3) * 3.1416 * (dat ** 3) 
   print (volrad)
elif var == 'diametro':
   voldiam = (4 / 3) * 3.1416 * ((dat / 2) ** 3) 
   print (voldiam)



