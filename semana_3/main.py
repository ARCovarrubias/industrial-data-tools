# ==========================================
# Script: Conversor de Temperaturas Científico
# Autor: Axel (Futuro Industrial Data Scientist)
# Descripción: Toma una lista de temperaturas en Celsius y las
#              convierte a Kelvin y Fahrenheit para análisis.
# ==========================================

def celsius_a_kelvin(celcius):
    """Concierte grados Celsius a Kelvin.
    Formula: K = °C + 273.15
    """
    kelvin = celcius + 273.15
    return kelvin

def celsius_a_fahrenheit(celcius):
    """Convierte grados Celsius a Fahrenheit.
    Formula: °F = (°C * 9/5) + 32
    """
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def procesar_datos_temperatura():
    """
    Funcion principal que orquesta el proceso.
    1. Define los datos de entrada
    2. Itera sobre los datos.
    3. Llama a las funciones de conversion.
    4. Imprime un reporte ordenado
    """
    print("---INICIO DEL REPORTE DE TEMPERATURAS---")

    # Datos de entrada
    lecturas_celsius = [0, 20, 37, 100, -40, 25.5]

    print(f"Procesando {len(lecturas_celsius)} lecturas.../n")
    print(f"{'Celsius (°C)':<15} | {'Kelvin (K)':<15} | {'Fahrenheit (°F)':<15}")
    print("-" * 55) # Línea separadora

    # Bucle para procesar cada lectura
    for temp_c in lecturas_celsius:
        # Llamamos a las funciones
        temp_k = celsius_a_kelvin(temp_c)
        temp_f = celsius_a_fahrenheit(temp_c)

        # Imprimimos usando f-strings con formato de ancho fijo (.2f = 2 decimales)
        print(f"{temp_c:<15.2f} | {temp_k:<15.2f} | {temp_f:<15.2f}")

    print("\n--- FIN DEL REPORTE ---")

# ==========================================
# Punto de Entrada Principal
# ==========================================
# Esta condición es una "buena práctica" crucial.
# Asegura que el script solo corra si se ejecuta directamente,
# no si se importa como una librería en otro código.

if __name__ == "__main__":
    procesar_datos_temperatura()