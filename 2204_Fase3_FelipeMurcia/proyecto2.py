# ==============================================================================
# Nombre del estudiante: Felipe Murcia Marín
# Grupo: 213022A_2204
# Programa: Ingeniería de Sistemas
# Código fuente: autoría propia
# ==============================================================================

def control_compra_helados():
    print("--- CONTROL DE GASTOS: CUMPLEAÑOS DE PEPITO (#6) ---")
    
    # Arreglo estipulado en el problema: [2500, 2000, 3800, 4500, 1800]
    precios = [2500, 2000, 3800, 4500, 1800]
    
    # Matriz para almacenar los datos de los helados: [ID, Nombre, Precio, Cantidad Comprada]
    matriz_helados = [
        [1, "Vaso de helado", precios[0], 0],
        [2, "Choco cono",     precios[1], 0],
        [3, "Paleta Drácula", precios[2], 0],
        [4, "Polet",          precios[3], 0],
        [5, "Platillo",       precios[4], 0]
    ]
    
    # Lectura y validación del presupuesto inicial
    while True:
        try:
            dinero_disponible = float(input("\nIngrese el dinero disponible para helados ($): "))
            if dinero_disponible >= 0:
                break
            print("El dinero disponible debe ser mayor o igual a 0.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    presupuesto_inicial = dinero_disponible
    comprando = True

    while comprando:
        print("\n--- Catálogo de Helados ---")
        for fila in matriz_helados:
            print(f"{fila[0]}. {fila[1]} - ${fila[2]:,}")
            
        print(f"\nSaldo disponible: ${dinero_disponible:,.2f}")
        
        try:
            opcion = int(input("Seleccione el tipo de helado a comprar (1-5): "))
            if 1 <= opcion <= 5:
                idx = opcion - 1
                precio = matriz_helados[idx][2]
                
                # Evaluación de dinero suficiente
                if dinero_disponible >= precio:
                    dinero_disponible -= precio
                    matriz_helados[idx][3] += 1  # Incrementa cantidad en el arreglo
                    print(f"¡Compra exitosa de: {matriz_helados[idx][1]}!")
                else:
                    print("--> Saldo insuficiente para este helado.")
            else:
                print("Opción fuera de rango (debe ser de 1 a 5).")
        except ValueError:
            print("Error: Ingrese un número entero.")

        # Verificar si el saldo alcanza para el helado más barato
        precio_minimo = min(precios)
        if dinero_disponible < precio_minimo:
            print("\n[!] El saldo restante es inferior al costo del helado más económico. Finalizando compras...")
            break
            
        # Control de ciclo
        while True:
            try:
                resp = int(input("\n¿Desea comprar otro helado? (1: sí, 0: no): "))
                if resp in [0, 1]:
                    if resp == 0:
                        comprando = False
                    break
                print("Ingrese 1 para Sí o 0 para No.")
            except ValueError:
                print("Error: Ingrese 1 o 0.")

    # Cálculo de salidas finales
    total_helados = sum(fila[3] for fila in matriz_helados)
    total_gastado = presupuesto_inicial - dinero_disponible
    promedio_por_helado = (total_gastado / total_helados) if total_helados > 0 else 0.0

    print("\n" + "="*45)
    print("           RESUMEN FINAL DE LA COMPRA          ")
    print("="*45)
    print(f"• Cantidad total de helados comprados: {total_helados}")
    print("\n• Cantidad de helados por tipo:")
    for fila in matriz_helados:
        print(f"   - {fila[1]}: {fila[3]} unidad(es)")
        
    print(f"\n• Valor total gastado: ${total_gastado:,.2f}")
    print(f"• Valor promedio por helado: ${promedio_por_helado:,.2f}")
    print(f"• Dinero sobrante: ${dinero_disponible:,.2f}")
    print("="*45)

if __name__ == "__main__":
    control_compra_helados()
