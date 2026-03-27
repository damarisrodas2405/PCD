# Analizador de Ventas 

## Descripcion

Este programa lee un archivo CSV con registros de ventas y genera un resumen por producto.

Para cada producto calcula:

* Total de unidades vendidas
* Ingreso total generado
* Precio promedio de venta

Finalmente, muestra los resultados ordenados de mayor a menor según el ingreso total.

---

## ¿Cómo ejecutarlo?

Desde la terminal, ejecuta:
python3 main.py < entrada1.txt

Para guardar la salida en el archivo salida1.txt:
python3 main.py < entrada1.txt > salida1.txt

## Ejemplo de entrada

Archivo: `entrada1.txt`

```csv
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
```

---

## Ejemplo de salida

producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
Teclado,5,4000.00,800.00


El programa maneja errores automáticamente:

* Ignora líneas vacías
* Ignora líneas con formato incorrecto
* Ignora valores no numéricos (ej: `"abc"`, `"invalid"`)
* No se detiene si encuentra errores

---

## ¿Cómo se calculan los datos?

* **Ingreso total** = cantidad × precio_unitario
* **Precio promedio** = ingreso_total / unidades_vendidas

---

## 📊 Orden de resultados

Los productos se ordenan de:

➡️ Mayor ingreso
➡️ A menor ingreso


## Autor
Rodas Sánchez Damaris Pamela

Ejercicio realizado para el reto de programación de la semana 03.
