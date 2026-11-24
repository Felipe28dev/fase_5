# ==============================================================================
# Nombre del estudiante: Felipe Murcia Marín
# Grupo: 213022A_2204
# Programa: Ingeniería de Sistemas
# Código fuente: autoría propia
# ==============================================================================

def evaluar_temperatura(temp: int) -> str:
    """Evalúa la temperatura ingresada y retorna la alerta correspondiente."""
    if temp > 200:
        return "Alerta: enfriamiento"
    elif temp < 180:
        return "Alerta: calentamiento"
    else:
        return "Temperatura óptima"

def monitoreo_temperatura():
    print("--- SISTEMA DE MONITOREO DE TEMPERATURA INDUSTRIAL ---")
    
    continuar = 1
    
    while continuar == 1:
        try:
            temperatura = int(input("\nIngrese la temperatura actual del horno (°C): "))
            
            # Evaluación e impresión de resultado
            resultado = evaluar_temperatura(temperatura)
            print(f"-> {resultado}")
                
            # Control de continuación
            continuar = int(input("\n¿Desea continuar? (1: sí, 0: no): "))
            while continuar not in [0, 1]:
                print("Opción inválida. Ingrese 1 para continuar o 0 para finalizar.")
                continuar = int(input("¿Desea continuar? (1: sí, 0: no): "))
                
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")

    print("\n[!] Monitoreo finalizado correctamente.")

if __name__ == "__main__":
    monitoreo_temperatura()
