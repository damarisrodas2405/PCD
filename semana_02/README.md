# Reto Semana 02 - Clasificador de Temperaturas

## Descripción

Este programa en Python lee datos en formato CSV desde la entrada estándar (`stdin`).
Cada línea contiene el nombre de una ciudad, una temperatura y su unidad (`C` o `F`).

El programa realiza los siguiente:

* Convierte todas las temperaturas a grados Celsius
* Clasifica cada temperatura en una categoría climática
* Imprime los resultados en formato CSV



## Clasificación de temperaturas

Las temperaturas en Celsius se clasifican de la siguiente manera:

* Menor a 0 → Congelante
* 0 a 15 → Frío
* 16 a 25 → Templado
* 26 a 35 → Cálido
* Mayor a 35 → Extremo


## Cómo ejecutar

* Desde la terminal, ubicado en la carpeta del proyecto, ejecutar: python3 main.py < tests/entrada1.txt

* También se puede guardar la salida en el archivo salida:esperada1.txt: python3 main.py < tests/entrada1.txt > tests/salida_esperada1.txt


## Ejemplo de entrada
ciudad,temperatura,unidad
Oslo,-2,C
Helsinki,-10,C
Estocolmo,41,F
Paris,68,F
Roma,20,C
Atenas,95,F
Budapest,30,C
Varsovia,14,F
Lisboa,25,C
Sydney,77,F
Melbourne,18,C
Auckland,59,F
Honolulu,88,F
Phoenix,110,F
Denver,5,C
Seattle,50,F
Boston,45,F
Chicago,20,C
Houston,100,F
Arabia,70,F
ErrorA,abc,C
ErrorB,20,Z
ErrorC,,C

## Ejemplo de salida

ciudad,temperatura_celsius,clasificacion
Oslo,-2.0,Congelante
Helsinki,-10.0,Congelante
Estocolmo,5.0,Frio
Paris,20.0,Templado
Roma,20.0,Templado
Atenas,35.0,Calido
Budapest,30.0,Calido
Varsovia,-10.0,Congelante
Lisboa,25.0,Templado
Sydney,25.0,Templado
Melbourne,18.0,Templado
Auckland,15.0,Frio
Honolulu,31.1,Calido
Phoenix,43.3,Extremo
Denver,5.0,Frio
Seattle,10.0,Frio
Boston,7.2,Frio
Chicago,20.0,Templado
Houston,37.8,Extremo
Arabia,21.1,Templado


## Consideraciones

* Las temperaturas en Fahrenheit son convertidas a Celsius usando la fórmula:
  (F - 32) × 5 / 9

* Las líneas inválidas son ignoradas:

  * Temperaturas no numéricas
  * Unidades distintas de C o F
  * Líneas vacías o mal formateadas

* La salida siempre muestra un decimal


## Autor

Rodas Sánchez Damaris Pamela
