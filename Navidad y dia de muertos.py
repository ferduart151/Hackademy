#Importar modulo datetime (funcion para trabajar con fechas y horas)
from datetime import datetime
#Definir la función 'dias_hasta_eventos'
def dias_hasta_eventos (fecha_actual):
    #Definir la variable 'dia_muertos' con la fecha del evento
    dia_muertos = datetime (year=fecha_actual.year + 1, month=11, day=2)
    navidad = datetime (year=fecha_actual.year, month=12, day=25)
    #Se crean objetos datetime para representar las fechas del dia de muertos y nadidad, se establece en el mismo año que la fecha actual
    #Se calcula la diferencia entre la fecha actual y navidad, dia de muertos
    dias_hasta_muertos = (dia_muertos - fecha_actual).days
    dias_hasta_navidad = (navidad - fecha_actual).days
    #Retorno de resultados
    return dias_hasta_muertos, dias_hasta_navidad
#La propiedad days en el contexto del objeto datetime en Python es utilizada para obtener la diferencia en días entre dos objetos datetime. La diferencia entre dos objetos datetime produce un objeto timedelta, y la propiedad days de ese objeto timedelta representa la diferencia en días.
#Cuando restas dos objetos datetime, obtienes un objeto timedelta que representa la duración entre esas dos fechas. La propiedad days de este objeto timedelta te da el número de días en esa duración.
#Obtencion de la fecha actual
fecha_actual = datetime.now()
#Llamada a la función
dias_hasta_muertos, dias_hasta_navidad = dias_hasta_eventos (fecha_actual)
print ('Faltan', dias_hasta_muertos, 'dias para el dia de muertos')
print ('Faltan', dias_hasta_navidad, 'dias para navidad')

