import sys
import re
from typing import List, Dict
from datetime import datetime


DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RHH']
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']


# PARTE 1
def validar_producto(codigo: str) -> Dict:
    resultado = {"valido": False, "categoria": None, "numero": None, "pais": None}
    patron = r'^([A-Z]{3})-(\d{4})-([A-Z]{2})$'
    m = re.match(patron, codigo)

    if m:
        resultado.update({
            "valido": True,
            "categoria": m.group(1),
            "numero": m.group(2),
            "pais": m.group(3)
        })

    return resultado


def validar_envio(codigo: str) -> Dict:
    resultado = {"valido": False, "fecha": None, "secuencial": None}
    patron = r'^ENV-(\d{4})-(\d{2})-(\d{2})-(\d{6})$'
    m = re.match(patron, codigo)

    if m:
        año, mes, dia, sec = m.groups()

        try:
            fecha = datetime(int(año), int(mes), int(dia))

            if 2020 <= fecha.year <= 2023:
                resultado.update({
                    "valido": True,
                    "fecha": fecha.strftime("%Y-%m-%d"),
                    "secuencial": sec
                })

        except ValueError:
            pass

    return resultado


def validar_empleado(codigo: str) -> Dict:
    resultado = {"valido": False, "departamento": None, "numero": None}
    patron = r'^EMP-([A-Z]{3})-(\d{4})$'
    m = re.match(patron, codigo)

    if m:
        dept, num = m.groups()

        if dept in DEPARTAMENTOS_VALIDOS and not num.startswith('0'):
            resultado.update({
                "valido": True,
                "departamento": dept,
                "numero": num
            })

    return resultado


def validar_factura(codigo: str) -> Dict:
    resultado = {"valido": False, "serie": None, "numero": None}
    patron = r'^FAC-([A-Z])-([0-9]{6})$'
    m = re.match(patron, codigo)

    if m:
        serie, numero = m.groups()

        if serie in SERIES_VALIDAS:
            resultado.update({
                "valido": True,
                "serie": serie,
                "numero": numero
            })

    return resultado


# PARTE 2
def validar_codigo(codigo: str) -> Dict:
    resultado = {
        "codigo": codigo,
        "tipo": "desconocido",
        "valido": False,
        "detalles": {}
    }

    if re.match(r'^[A-Z]{3}-\d{4}-[A-Z]{2}$', codigo):
        resultado["tipo"] = "producto"
        resultado["detalles"] = validar_producto(codigo)

    elif codigo.startswith('ENV-'):
        resultado["tipo"] = "envio"
        resultado["detalles"] = validar_envio(codigo)

    elif codigo.startswith('EMP-'):
        resultado["tipo"] = "empleado"
        resultado["detalles"] = validar_empleado(codigo)

    elif codigo.startswith('FAC-'):
        resultado["tipo"] = "factura"
        resultado["detalles"] = validar_factura(codigo)

    resultado["valido"] = resultado["detalles"].get("valido", False)

    return resultado


# PARTE 3
def procesar_lote(lineas: List[str]) -> Dict:
    resultado = {
        "total": 0,
        "validos": 0,
        "invalidos": 0,
        "por_tipo": {
            "producto": {"total": 0, "validos": 0},
            "envio": {"total": 0, "validos": 0},
            "empleado": {"total": 0, "validos": 0},
            "factura": {"total": 0, "validos": 0},
            "desconocido": {"total": 0, "validos": 0}
        },
        "detalle": []
    }

    for cod in lineas:
        res = validar_codigo(cod)

        resultado["total"] += 1

        if res["valido"]:
            resultado["validos"] += 1
        else:
            resultado["invalidos"] += 1

        tipo = res["tipo"]

        resultado["por_tipo"][tipo]["total"] += 1

        if res["valido"]:
            resultado["por_tipo"][tipo]["validos"] += 1

        resultado["detalle"].append(res)

    return resultado


def main():
    lineas = []

    for linea in sys.stdin:
        linea = linea.strip()

        if not linea:
            continue

        if linea.lower().startswith("codigo"):
            continue

        lineas.append(linea)

    resultado = procesar_lote(lineas)

    print("codigo,tipo,valido")

    for item in resultado["detalle"]:
        print(
            f'{item["codigo"]},'
            f'{item["tipo"]},'
            f'{"valido" if item["valido"] else "invalido"}'
        )


if __name__ == "__main__":
    main()