import csv

def leer_inventario(ruta_archivo):
    productos_raw = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            # DictReader usa la primera línea automáticamente como las llaves del diccionario
            lector = csv.DictReader(archivo)
            for fila in lector:
                productos_raw.append(fila)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta_archivo}")
    return productos_raw


def escribir_reporte(productos, ruta_archivo):
    encabezados = [
        "sku",
        "nombre",
        "categoria",
        "stock_actual",
        "stock_minimo",
        "unidades_faltantes",
        "valor_inventario"
    ]

    with open(ruta_archivo, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezados)

        for p in productos:
            escritor.writerow([
                p.sku,
                p.nombre,
                p.categoria,
                p.stock,
                p.stock_minimo,
                p.unidades_faltantes(),
                f"{p.valor_inventario():.2f}"
            ])