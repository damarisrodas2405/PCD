import argparse
import csv


def es_valor_nulo(valor):
    if valor is None:
        return True
    if isinstance(valor, str) and valor.strip() == "":
        return True
    return False


def es_numerico(valor):
    try:
        float(str(valor).replace(",", "").strip())
        return True
    except:
        return False


def es_fecha(valor):
    v = str(valor).strip()
    if len(v) >= 10:
        try:
            partes = v[:10].split("-")
            if len(partes) == 3:
                int(partes[0])
                int(partes[1])
                int(partes[2])
                return True
        except:
            return False
    return False


def es_booleano(valor):
    v = str(valor).strip().lower()
    return v in ["true", "false", "yes", "no", "si", "1", "0"]


def inferir_tipo(valores):
    no_nulos = [v for v in valores if not es_valor_nulo(v)]

    if not no_nulos:
        return "texto"

    total = len(no_nulos)

    num = sum(1 for v in no_nulos if es_numerico(v))
    fecha = sum(1 for v in no_nulos if es_fecha(v))
    booleano = sum(1 for v in no_nulos if es_booleano(v))

    if num / total > 0.8:
        return "numerico"
    if fecha / total > 0.8:
        return "fecha"
    if booleano / total > 0.8:
        return "booleano"

    return "texto"


def calcular_porcentaje(parte, total):
    if total == 0:
        return 0.00
    return round((parte / total) * 100, 2)


def perfilar_columna(nombre, valores):
    total = len(valores)
    nulos = sum(1 for v in valores if es_valor_nulo(v))

    no_nulos = [v for v in valores if not es_valor_nulo(v)]

    tipo = inferir_tipo(valores)
    unicos = len(set(no_nulos))
    ejemplo = no_nulos[0] if no_nulos else ""

    return {
        "nombre_columna": nombre,
        "tipo_inferido": tipo,
        "total_registros": total,
        "valores_nulos": nulos,
        "porcentaje_nulos": calcular_porcentaje(nulos, total),
        "valores_unicos": unicos,
        "porcentaje_unicos": calcular_porcentaje(unicos, total),
        "ejemplo_valor": ejemplo
    }


def leer_csv(ruta):
    with open(ruta, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        columnas = reader.fieldnames
        datos = {col: [] for col in columnas}

        for fila in reader:
            for col in columnas:
                datos[col].append(fila[col])

    return datos


def escribir_csv(ruta, perfiles):
    columnas = [
        "nombre_columna",
        "tipo_inferido",
        "total_registros",
        "valores_nulos",
        "porcentaje_nulos",
        "valores_unicos",
        "porcentaje_unicos",
        "ejemplo_valor"
    ]

    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(perfiles)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)

    args = parser.parse_args()

    datos = leer_csv(args.input)

    perfiles = []
    for col, valores in datos.items():
        perfil = perfilar_columna(col, valores)
        perfiles.append(perfil)

    escribir_csv(args.output, perfiles)


if __name__ == "__main__":
    main()
