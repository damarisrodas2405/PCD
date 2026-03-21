import sys

#Limpiar valores
def limpiar_valor(valor):
    valor  = valor.strip()
    caracteres_validos = "0123456789.-"
    resultado = ""

    for char in valor:
        if char in caracteres_validos:
            resultado += char
    return resultado

#Procesar lineas
def procesar_linea(linea):
    linea = linea.strip()

    if linea == "":
        return 0
    
    valores = linea.split(",")
    suma = 0

    for valores in valores:
        valor_limpio = limpiar_valor()

        if valor_limpio == "":
            numero = 0
        else:
            try:
                numero = int(float(valor_limpio))
            except ValueError:
                numero = 0
        suma += numero
    return suma

def main():

    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()


#Programa para procesar lineas y sumar valores