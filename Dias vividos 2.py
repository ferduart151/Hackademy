from datetime import datetime

def dias_vividos(fecha_nacimiento):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Calcular la diferencia de días
    diferencia = fecha_actual - fecha_nacimiento

    # Obtener el número de días en la diferencia
    dias_vividos = diferencia.days

    return dias_vividos

# Ingresar la fecha de nacimiento del usuario
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (formato YYYY-MM-DD): ")

# Convertir la cadena a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")

# Calcular y mostrar los días vividos
dias_totales = dias_vividos(fecha_nacimiento)
print(f"Hasta hoy, has vivido aproximadamente {dias_totales} días.")
