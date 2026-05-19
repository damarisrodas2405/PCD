import math

def validar_producto(sku, nombre, categoria, precio, stock, stock_minimo):
    if not sku or not str(sku).strip():
        return False, "SKU vacio o invalido"

    if not nombre or not str(nombre).strip():
        return False, "Nombre vacio"

    if not categoria or not str(categoria).strip():
        return False, "Categoria vacia"

    # Validar precio
    if precio is None or str(precio).strip() == "":
        return False, "Precio ausente"
    try:
        precio_float = float(precio)
        if not math.isfinite(precio_float):
            return False, "Precio no finito"
        if precio_float < 0:
            return False, "Precio negativo"
    except ValueError:
        return False, "Precio invalido"

    # Validar stock
    if stock is None or str(stock).strip() == "":
        return False, "Stock vacio"
    try:
        stock_int = int(stock)
        if stock_int < 0:
            return False, "Stock negativo"
    except ValueError:
        return False, "Stock invalido"

    # Validar stock mínimo
    if stock_minimo is None or str(stock_minimo).strip() == "":
        return False, "Stock minimo vacio"
    try:
        stock_min_int = int(stock_minimo)
        if stock_min_int < 0:
            return False, "Stock minimo negativo"
    except ValueError:
        return False, "Stock minimo invalido"

    return True, None