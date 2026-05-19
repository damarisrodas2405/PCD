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
python3 main.py < tests/entrada1.txt

Para guardar la salida en el archivo salida1.txt:
python3 main.py < test/entrada1.txt > tests/salida1.txt

## Ejemplo de entrada

Archivo: `entrada1.txt`

```csv
fecha,producto,cantidad,precio_unitario
2026-03-29,Notebook_HyperX,12,7650.81
2026-03-02
2026-03-30,Barra_Sonido,16,1831.59
2026-02-19,Teclado_HP,10,533.84
2026-02-19,Mousepad,6,126.52
2026-01-26,RAM_HyperX,10,644.70
2026-01-04,SSD_BenQ,13,2512.47
2026-02-14,Touchpad_LG,6,693.86
2026-04-02
2026-01-09,NAS_HP,2,8822.85,N/A,vacio
2026-04-06,Impresora_Laser,2,10256.89
2026-04-03,Mouse_Ergonomico_Kingston,10,514.07
2026-01-20,Docking_Station,15,4959.66
2026-04-10,USB_Corsair,5,61.92
2026-01-06,SSD_SanDisk,3,4175.98
2026-03-05,Audifonos_Gaming_Gigabyte,5,2578.92
2026-02-13,Laptop_Samsung,1,25096.35
2026-02-05
2026-03-20,MicroSD_Asus,INVALIDO,504.11
2026-03-23,Monitor_Curvo_Epson,9,14420.90
2026-02-18,Bocina_Xiaomi,17,1859.17
2026-03-17,Bocina_LG,10,vacio
2026-02-24,Teclado_Mecanico_HyperX,1,2634.83
2026-01-18,Microfono_USB_Lenovo,13,553.10
2026-03-09,Tarjeta_Video,2,10304.82
2026-01-08
2026-02-01,Bocina_Canon,19,555.68
2026-01-12,SSD_LG,7,2663.38
2026-02-20,USB_Acer,7,66.21
2026-01-10,Ultrabook_Anker,3,16915.26
2026-04-09,Tarjeta_Video_Lenovo,5,23441.00
2026-01-03,Licencia_Adobe,18,3842.08,1e999
2026-04-09,Teclado_Razer,3,1864.90
2026-02-06,Audifonos_Bluetooth_Sony,18,1387.64
2026-01-18,HDD_LG,2,3181.39
2026-02-19,Chromebook_SanDisk,15,12220.31
2026-03-08,Microfono_Razer,8,1454.00
2026-01-27,USB_Asus,11,166.63
2026-04-01,SSD_Razer,8,3575.15
2026-03-22,Monitor_Curvo_Acer,14,8529.06
2026-03-31,Mouse_Ergonomico_Sony,10,962.22
2026-04-09,Chromebook_WD,2,5305.81
2026-03-17,HDD_WD,1,626.59
2026-04-07,Stylus_MSI,6,1310.55
2026-02-16,Teclado_Mecanico_Kingston,1,2308.81
2026-02-05,Laptop_Logitech,12,12517.56
2026-01-18,Audifonos_Gigabyte,19,493.44
2026-01-05,RAM_Dell,20,2335.82
2026-01-07,Barra_Sonido_WD,2
2026-01-20,Laptop_MSI,19,13816.22
2026-04-10,SSD_Kingston,1,2272.13,sin_dato,xx,vacio
2026-03-28,NAS_Asus,5
2026-02-25,HDD_Externo_HyperX,4,2729.25
2026-03-04,Laptop_Asus,3,16786.68
2026-03-25,Barra_Sonido_Samsung,14,6133.51
2026-04-05,Ultrabook_Gigabyte,20,25353.83
2026-03-18,Pantalla_Portatil_Kingston,19,3814.26
2026-01-31,Mouse_Gaming_Canon,11,1672.83
2026-03-15,Monitor_Curvo_Acer,7,5972.60
2026-02-16,Placa_Base,9,4165.44
2026-03-13,Barra_Sonido_Logitech,3,5057.60
2026-01-01,Audifonos_Gaming_Acer,15,1e999
2026-03-14,Audifonos_Gaming_HyperX,5,1870.89
2026-02-26,Audifonos_Gaming_WD,9,1579.41
2026-03-16,Teclado_Seagate,3,1253.31
2026-03-12,Stylus_Anker,8,1540.34
2026-01-28,Audifonos_Bluetooth_Epson,17,1920.31
2026-02-01,Tarjeta_Video_TP_Link,18,2960.11
2026-04-07,Stylus_Xiaomi,12,1903.51
2026-03-31,HDD_Externo_Logitech,1,2519.71
2026-01-11,MicroSD_Lenovo,17,199.37
2026-03-07,Chromebook_Razer,1,12225.89, ,TBD,muchos
2026-01-07,Pantalla_Portatil_Asus,1e999,5221.25
2026-03-23,Mouse_Gaming_Acer,-,648.24
2026-01-18,SSD_Seagate,15,2220.47
2026-02-04,Audifonos_Gaming_Logitech,16,999.58,,$100
2026-03-08,Pantalla_Portatil_Sony,17,3233.72
2026-01-29,Monitor_Gaming_SanDisk,15,14356.89
2026-02-07,Microfono_USB_Corsair,5,2225.60
2026-02-12,Mouse_Gaming_TP_Link,13,error
2026-03-15,Audifonos_Gaming_Acer,5,1562.96
2026-01-22,RAM_Epson,8,2660.69
2026-03-31,Monitor_Gaming_SanDisk,5,14266.68
2026-03-20,Teclado_Gaming_Epson,14,1987.24
2026-01-09,Teclado_Gaming_Canon
2026-04-01,MacBook_Anker,3,50598.32
2026-03-27,Teclado_Mecanico_Dell,10,1419.31
2026-04-09,MacBook_Asus,1,48342.77
2026-03-25,Teclado_Acer,5,804.55
2026-01-21,Teclado_Dell,7,1096.74
2026-04-04,Chromebook_Dell,4,9930.19,NaN,abc
2026-01-03,Barra_Sonido,9,1771.97
2026-04-07,HDD_Logitech,5,2343.97
2026-02-17,Monitor_Gaming_SanDisk,8,9788.02
2026-01-16,Notebook_Lenovo,sin_dato,15056.38
2026-01-15,Mousepad,12,330.92
2026-02-08,MicroSD_Samsung,20,12..5
2026-01-28,NAS_Dell,15,15363.42
2026-02-06,Microfono_HP,18,728.60
2026-01-16,Monitor_Gigabyte,18,10042.30

```

---

## Ejemplo de salida

```csv
producto,unidades_vendidas,ingreso_total,precio_promedio
Ultrabook_Gigabyte,20,507076.60,25353.83
Monitor_Gaming_SanDisk,28,364990.91,13035.39
Laptop_MSI,19,262508.18,13816.22
NAS_Dell,15,230451.30,15363.42
Chromebook_SanDisk,15,183304.65,12220.31
Monitor_Gigabyte,18,180761.40,10042.30
Monitor_Curvo_Acer,21,161215.04,7676.91
MacBook_Anker,3,151794.96,50598.32
Laptop_Logitech,12,150210.72,12517.56
Monitor_Curvo_Epson,9,129788.10,14420.90
Tarjeta_Video_Lenovo,5,117205.00,23441.00
Notebook_HyperX,12,91809.72,7650.81
Barra_Sonido_Samsung,14,85869.14,6133.51
Docking_Station,15,74394.90,4959.66
Pantalla_Portatil_Kingston,19,72470.94,3814.26
Pantalla_Portatil_Sony,17,54973.24,3233.72
Tarjeta_Video_TP_Link,18,53281.98,2960.11
Ultrabook_Anker,3,50745.78,16915.26
Laptop_Asus,3,50360.04,16786.68
MacBook_Asus,1,48342.77,48342.77
RAM_Dell,20,46716.40,2335.82
Barra_Sonido,25,45253.17,1810.13
Placa_Base,9,37488.96,4165.44
SSD_Seagate,15,33307.05,2220.47
SSD_BenQ,13,32662.11,2512.47
Audifonos_Bluetooth_Epson,17,32645.27,1920.31
Bocina_Xiaomi,17,31605.89,1859.17
SSD_Razer,8,28601.20,3575.15
Teclado_Gaming_Epson,14,27821.36,1987.24
Laptop_Samsung,1,25096.35,25096.35
Audifonos_Bluetooth_Sony,18,24977.52,1387.64
Stylus_Xiaomi,12,22842.12,1903.51
RAM_Epson,8,21285.52,2660.69
Tarjeta_Video,2,20609.64,10304.82
Impresora_Laser,2,20513.78,10256.89
SSD_LG,7,18643.66,2663.38
Mouse_Gaming_Canon,11,18401.13,1672.83
Barra_Sonido_Logitech,3,15172.80,5057.60
Audifonos_Gaming_WD,9,14214.69,1579.41
Teclado_Mecanico_Dell,10,14193.10,1419.31
Microfono_HP,18,13114.80,728.60
Audifonos_Gaming_Gigabyte,5,12894.60,2578.92
SSD_SanDisk,3,12527.94,4175.98
Stylus_Anker,8,12322.72,1540.34
HDD_Logitech,5,11719.85,2343.97
Microfono_Razer,8,11632.00,1454.00
Microfono_USB_Corsair,5,11128.00,2225.60
HDD_Externo_HyperX,4,10917.00,2729.25
Chromebook_WD,2,10611.62,5305.81
Bocina_Canon,19,10557.92,555.68
Mouse_Ergonomico_Sony,10,9622.20,962.22
Audifonos_Gigabyte,19,9375.36,493.44
Audifonos_Gaming_HyperX,5,9354.45,1870.89
Stylus_MSI,6,7863.30,1310.55
Audifonos_Gaming_Acer,5,7814.80,1562.96
Teclado_Dell,7,7677.18,1096.74
Microfono_USB_Lenovo,13,7190.30,553.10
RAM_HyperX,10,6447.00,644.70
HDD_LG,2,6362.78,3181.39
Teclado_Razer,3,5594.70,1864.90
Teclado_HP,10,5338.40,533.84
Mouse_Ergonomico_Kingston,10,5140.70,514.07
Mousepad,18,4730.16,262.79
Touchpad_LG,6,4163.16,693.86
Teclado_Acer,5,4022.75,804.55
Teclado_Seagate,3,3759.93,1253.31
MicroSD_Lenovo,17,3389.29,199.37
Teclado_Mecanico_HyperX,1,2634.83,2634.83
HDD_Externo_Logitech,1,2519.71,2519.71
Teclado_Mecanico_Kingston,1,2308.81,2308.81
USB_Asus,11,1832.93,166.63
HDD_WD,1,626.59,626.59
USB_Acer,7,463.47,66.21
USB_Corsair,5,309.60,61.92

```


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
