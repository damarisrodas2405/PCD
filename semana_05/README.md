# Perfilador de Datasets CSV

Este programa analiza un archivo CSV y genera un reporte con estadísticas por columna.

## ¿Qué hace?

Para cada columna calcula:

* Nombre de la columna
* Tipo de dato inferido (numérico, texto, fecha, booleano)
* Total de registros
* Valores nulos
* Porcentaje de nulos
* Valores únicos
* Porcentaje de valores únicos
* Ejemplo de valor

---

## Estructura del proyecto

```
semana_05/
│
├── main.py                 
├── requirements.txt        
├── README.md               
├── .gitignore              
│
├── data/                   
│   ├── ventas.csv
│   ├── empleados.csv
│   └── sensores.csv
│
└── outputs/                
    └── (se generan al ejecutar)
```

---

## Cómo ejecutar

```
Para ejecutar:
python3 main.py --input data/empleados.csv --output outputs/perfil_empleados.csv
python3 main.py --input data/sensores.csv --output outputs/perfil_sensores.csv

Para revisar los resultados se registraron
ls outputs

Para ver los resultados:
cat outputs/perfil_empleados.csv
cat outputs/perfil_sensores.csv
```

---

## Ejemplo de entrada

```
fecha,producto,cantidad,precio
2026-01-01,Laptop,2,15000
2026-01-02,Mouse,10,250
2026-01-03,Teclado,5,800
2026-01-04,Laptop,1,14500
```

---

## Ejemplo de salida

```
nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
id,numerico,7,0,0.0,7,100.0,1
nombre,texto,7,1,14.29,6,85.71,Juan
edad,numerico,7,1,14.29,6,85.71,30
salario,numerico,7,1,14.29,6,85.71,15000
activo,booleano,7,0,0.0,2,28.57,si
fecha_ingreso,fecha,7,1,14.29,6,85.71,2020-01-15
```

---

## Autor

Rodas Sánchez Damaris Pamela
