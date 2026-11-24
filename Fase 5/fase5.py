# ==============================================================================
# Nombre del estudiante: Felipe Murcia Marín
# Grupo: [Tu número de grupo]
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación (213022) - Fase 5 POA
# Código fuente: autoría propia
# ==============================================================================

CATEGORIA_OBJETIVO = "Platos Fuertes"
UMBRAL_PRECIO = 25000.0
DESCUENTO_PROMO = 0.15


def obtener_menu_productos():
    """Retorna una matriz de 6 productos con formato: [Nombre, Categoría, Precio_Base]."""
    return [
        ["Bandeja Montañera", "Platos Fuertes", 32000.0],   # Aplica 15% (Categoría ok, > 25000)
        ["Sancocho de Gallina", "Platos Fuertes", 22000.0], # No aplica (No supera umbral)
        ["Limonada de Coco", "Bebidas", 9500.0],            # No aplica (Otra categoría)
        ["Lomo a la Pimienta", "Platos Fuertes", 38000.0],  # Aplica 15% (Categoría ok, > 25000)
        ["Torta de Chocolate", "Postres", 28000.0],         # No aplica (Otra categoría)
        ["Jugo Natural en Agua", "Bebidas", 7000.0]         # No aplica (Otra categoría)
    ]


def calcular_precio_final(precio_base, categoria, categoria_objetivo=CATEGORIA_OBJETIVO, umbral_precio=UMBRAL_PRECIO, descuento=DESCUENTO_PROMO):
    """Calcula el precio final aplicando el 15% de descuento si cumple la categoría y el umbral de precio."""
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        precio_final = precio_base * (1.0 - descuento)
    else:
        precio_final = precio_base
    return precio_final


def mostrar_reporte_promocion(menu, categoria_objetivo, umbral_precio):
    """Recorre la matriz de productos e imprime el nombre, precio base y precio final."""
    print("=" * 68)
    print(f"   PROMOCIÓN DEL 15% - CATEGORÍA: {categoria_objetivo.upper()} (PRECIO > ${umbral_precio:,.0f})")
    print("=" * 68)
    print(f"{'PRODUCTO':<24} {'PRECIO BASE':>14} {'PRECIO FINAL':>16}")
    print("-" * 68)

    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        precio_final = calcular_precio_final(precio_base, categoria, categoria_objetivo, umbral_precio, DESCUENTO_PROMO)
        print(f"{nombre:<24} ${precio_base:>13,.2f} ${precio_final:>15,.2f}")

    print("=" * 68)


def ejecutar_sistema_menu():
    """Función principal que coordina la lectura de la matriz y el despliegue del reporte."""
    menu = obtener_menu_productos()
    mostrar_reporte_promocion(menu, CATEGORIA_OBJETIVO, UMBRAL_PRECIO)


if __name__ == "__main__":
    ejecutar_sistema_menu()
