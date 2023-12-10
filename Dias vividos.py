from datetime import datetime

def es_bisiesto(ano):
    # Función para determinar si un año es bisiesto
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dias_vividos(fecha_nacimiento):
    # Obtener la fecha y hora actuales
    fecha_actual = datetime.now()

    # Calcular la diferencia de años
    diferencia_anos = fecha_actual.year - fecha_nacimiento.year

    # Ajustar la fecha de nacimiento para tener en cuenta años bisiestos
    fecha_nacimiento_ajustada = fecha_nacimiento.replace(year=fecha_nacimiento.year + diferencia_anos)

    # Calcular la diferencia total de días
    diferencia_total = fecha_actual - fecha_nacimiento_ajustada

    # Obtener el número total de días en la diferencia
    dias_vividos = diferencia_total.days

    return dias_vividos

# Ingresar la fecha de nacimiento por el usuario
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (formato YYYY-MM-DD): ")

# Convertir la cadena a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")

# Calcular y mostrar los días vividos
dias_totales = dias_vividos(fecha_nacimiento)
print(f"Hasta hoy, has vivido aproximadamente {dias_totales} días.")
