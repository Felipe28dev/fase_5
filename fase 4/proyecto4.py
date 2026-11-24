VENTAS_POR_MES = {"enero": 1500, "febrero": 2200, "marzo": 1800}
LIMITE_BONO = 5000


def solicitar_datos():
    """Solicita un nombre y una cantidad válida al usuario."""
    nombre_vendedor = input("Ingrese su nombre: ").strip()
    while not nombre_vendedor:
        print("El nombre no puede estar vacío.")
        nombre_vendedor = input("Ingrese su nombre: ").strip()

    while True:
        entrada = input("Ingrese las ventas de abril: ").strip()
        try:
            cantidad_nueva = int(entrada)
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
            continue

        if cantidad_nueva < 0:
            print("Las ventas no pueden ser negativas.")
            continue

        return nombre_vendedor, cantidad_nueva


def agregar_ventas(datos_actuales, mes, monto):
    """Acumula las ventas registradas para un mes."""
    datos_actuales[mes] = datos_actuales.get(mes, 0) + monto
    return list(datos_actuales.values())


def revisar_bono(ventas_totales, limite):
    """Verifica si las ventas totales superan el límite del bono."""
    if ventas_totales > limite:
        monto_bono = ventas_totales / limite
        print(f"¡Felicidades! Gana un bono de: {monto_bono}")
    else:
        print("Siga esforzándose para el bono.")


contador = 1
while contador < 3:
    print(f"\n--- Iteración {contador} ---")
    vendedor, nuevas_ventas = solicitar_datos()
    ventas_por_mes_nuevo = agregar_ventas(
        VENTAS_POR_MES, "abril", nuevas_ventas
    )
    total_anual = sum(ventas_por_mes_nuevo)

    revisar_bono(total_anual, LIMITE_BONO)
    print(
        f"Ventas de abril registradas para {vendedor}: {nuevas_ventas}. "
        f"Total acumulado de enero a abril: {total_anual}"
    )
    contador += 1
