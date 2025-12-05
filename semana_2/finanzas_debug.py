from tabulate import tabulate

# --- VARIABLE GLOBAL ---

saldo_cuenta = 1000.0

def procesar_transaccion(tipo, monto):
    """
    Calcula el nuevo saldo basado en una transacción local.
    No modifica la global directamente, retorna el resultado.
    """
    comision = 5.00

    saldo_temporal = 0.0

    if tipo == "retiro":
        saldo_temporal = saldo_cuenta - monto - comision
    elif tipo == "deposito":
        saldo_temporal = saldo_cuenta + monto - comision

    return saldo_temporal

def mostrar_resumen():
    # Muestra de datos en tabla visual

    datos = [
        ["Saldo Inicial (Global)", f"${saldo_cuenta:.2f}"],
        ["Intento de Retiro", "$200.00"],
        ["Comisión (Local)", "$5.00"],
        ["Saldo Simulado", "Calculando..."]
    ]

    # Simulacion de trasaccion
    nuevo_saldo = procesar_transaccion("retiro", 200)

    # Actualizamos la tabla
    datos[3][1] = f"${nuevo_saldo:.2f}"

    print("\n--- REPORTE DE TRANSACCIÓN ---")
    print(tabulate(datos, headers=["Concepto", "Monto"], tablefmt="fancy_grid"))

# Punto de entrada del script
if __name__ == "__main__":
    mostrar_resumen()