# ==============================================================================
# Nombre del estudiante: Felipe Murcia Marín
# Grupo: [213022_273]
# Programa: Ingeniería de Sistemas
# Código fuente: autoría propia / Asistido por IA (Depuración)
# ==============================================================================

# Diccionario inicial de ventas por mes
VENTAS_POR_MES = {"enero": 1500, "febrero": 2200, "marzo": 1800}
LIMITE_BONO = 5000

def solicitar_datos():
    """Solicita un nombre de vendedor y una cantidad de ventas válida para abril."""
    nombre_vendedor = input("Ingrese su nombre: ")
    try:
        cantidad_nueva = int(input("Ingrese las ventas de abril: "))
        if cantidad_nueva < 0:
            print("La cantidad no puede ser negativa, se asignará 0.")
            cantidad_nueva = 0
    except ValueError:
        print("Entrada inválida, se asignará 0 por defecto.")
        cantidad_nueva = 0
    return nombre_vendedor, cantidad_nueva

def agregar_ventas(datos_actuales, mes, monto):
    """Agrega un nuevo mes de ventas al diccionario y retorna la lista de valores."""
    datos_actuales[mes] = monto
    return list(datos_actuales.values())

def revisar_bono(ventas_totales, limite):
    """Verifica si el vendedor califica para un bono basado en el límite establecido."""
    if ventas_totales > limite:
        # Corrección lógica: el bono se calcula de forma proporcional o como incentivo fijo/porcentual
        monto_bono = ventas_totales * 0.10  
        print(f"¡Felicidades! Gana un bono de: ${monto_bono:,.2f}")
    else:
        print("Siga esforzándose para el bono.")

def menu_principal():
    print("--- SISTEMA DE GESTIÓN Y SEGUIMIENTO DE VENTAS ---")
    
    # Simulación de iteración de control de ventas
    contador = 1
    while contador <= 2:
        print(f"\n--- Iteración {contador} ---")
        vendedor, nuevas_ventas = solicitar_datos()
        
        # Agregamos las ventas de abril al diccionario copiando la estructura original
        ventas_actualizadas = agregar_ventas(VENTAS_POR_MES, "abril", nuevas_ventas)
        total_anual = sum(ventas_actualizadas)
        
        try:
            revisar_bono(total_anual, LIMITE_BONO)
            # Manejo seguro para evitar KeyError si se consulta un mes que no existe
            mes_extra = VENTAS_POR_MES.get("mayo", 0)
            print(f"Ventas de {vendedor}: ${total_anual:,}. Ventas registradas de mayo (referencia): ${mes_extra:,}")
        except Exception as e:
            print(f"Ocurrió un problema en el cálculo final: {e}")
            
        contador += 1

if __name__ == "__main__":
    menu_principal()
