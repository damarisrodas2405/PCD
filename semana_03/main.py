import sys

def main():
    productos = {}
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue

        # Saltar líneas vacías
        if not linea:
            continue

        # Separar columnas
        partes = linea.split(",")

        # Validar que tenga 4 columnas
        if len(partes) != 4:
            continue

        fecha = partes[0]
        producto = partes[1]

        # Convertir cantidad y precio
        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
        except ValueError:
            continue

        # Inicializar producto si no existe
        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        # Acumular datos
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    # Calcular precio promedio
    for producto in productos:
        unidades = productos[producto]["unidades"]
        ingreso = productos[producto]["ingreso"]
        productos[producto]["promedio"] = ingreso / unidades if unidades > 0 else 0

    # Ordenar por ingreso total descendente
    lista_ordenada = sorted(
        productos.items(),
        key=lambda x: x[1]["ingreso"],
        reverse=True
    )

    # Imprimir salida CSV
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for nombre, datos in lista_ordenada:
        print(f"{nombre},{datos['unidades']},{datos['ingreso']:.2f},{datos['promedio']:.2f}")

if __name__ == "__main__":
    main()