def validar_producto(sku, nombre, categoria, precio, stock, stock_minimo):
    if not sku or not str(sku).strip():
        return False, "SKU vacio o invalido"

    if not nombre or not str(nombre).strip():
        return False, "Nombre vacio"

    if not categoria or not str(categoria).strip():
        return False, "Categoria vacia"

    try:
        precio = float(precio)
        if precio < 0:
            return False, "Precio negativo"
    except:
        return False, "Precio invalido"

    try:
        stock = int(stock)
        if stock < 0:
            return False, "Stock negativo"
    except:
        return False, "Stock invalido"

    try:
        stock_minimo = int(stock_minimo)
        if stock_minimo < 0:
            return False, "Stock minimo negativo"
    except:
        return False, "Stock minimo invalido"

    return True, None     