# Reto semana 06 - Validador de Códigos

## Descripción

Este proyecto corresponde al desarrollo de un validador de códigos que procesa registros desde la entrada estándar (`stdin`), identifica el tipo de código, valida su formato y genera la salida en formato CSV.

El programa reconoce automáticamente los siguientes tipos:

- Producto
- Envío
- Empleado
- Factura

Y determina si cada código es:

- valido
- invalido

---

# Estructura del proyecto

semana_06/
├── README.md           
├── main.py             
├── .gitignore          
└── tests/              
    ├── codigos.txt
    └── salida_esperada.txt



# Ejecución

Desde terminal ejecutar:

```bash
python main.py < tests/codigos.txt > test/salida_generada.txt
```



# Formato de entrada

El archivo de entrada debe venir en formato CSV con una sola columna:

```csv
TEC-0001-MX
ALI-9999-US
ROB-1234-CA
tec-0001-MX
TEC-001-MX
TECH-0001-MX
ENV-2024-03-15-001234
ENV-2025-12-01-999999
ENV-2019-03-15-001234
ENV-2024-13-15-001234
ENV-2024-03-32-001234
EMP-VEN-1234
EMP-TEC-9999
EMP-ADM-1000
EMP-VEN-0123
EMP-XXX-1234
EMP-VEN-123
FAC-A-123456
FAC-E-000001
FAC-B-999999
FAC-F-123456
FAC-A-12345
FAC-a-123456
XXX-1234
RANDOM-CODE
```


# Formato de salida

La salida se genera también como CSV:

```csv
codigo,tipo,valido
TEC-0001-MX,producto,valido
ALI-9999-US,producto,valido
ROB-1234-CA,producto,valido
tec-0001-MX,desconocido,invalido
TEC-001-MX,desconocido,invalido
TECH-0001-MX,desconocido,invalido
ENV-2024-03-15-001234,envio,invalido
ENV-2025-12-01-999999,envio,invalido
ENV-2019-03-15-001234,envio,invalido
ENV-2024-13-15-001234,envio,invalido
ENV-2024-03-32-001234,envio,invalido
EMP-VEN-1234,empleado,valido
EMP-TEC-9999,empleado,valido
EMP-ADM-1000,empleado,valido
EMP-VEN-0123,empleado,invalido
EMP-XXX-1234,empleado,invalido
EMP-VEN-123,empleado,invalido
FAC-A-123456,factura,valido
FAC-E-000001,factura,valido
FAC-B-999999,factura,valido
FAC-F-123456,factura,invalido
FAC-A-12345,factura,invalido
FAC-a-123456,factura,invalido
XXX-1234,desconocido,invalido
RANDOM-CODE,desconocido,invalido

```

Si no cumple las reglas:

```csv
codigo,tipo,valido
FAC-a-123456,factura,invalido
XXX-1234,desconocido,invalido
```

---

# Reglas de validación

## 1. Producto

Formato:

```text
AAA-1234-AA
```

Reglas:

- 3 letras mayúsculas
- guion `-`
- 4 números
- guion `-`
- 2 letras mayúsculas

---

## 2. Envío

Formato:

```text
ENV-YYYY-MM-DD-XXXXXX
```

Reglas:

- debe iniciar con `ENV`
- fecha válida
- año entre 2020 y 2023
- secuencial numérico de 6 dígitos

---

## 3. Empleado

Formato:

```text
EMP-DEP-1234
```
Reglas:

- debe iniciar con `EMP`
- departamento permitido
- número de 4 dígitos

---

## 4. Factura

Formato:

```text
FAC-S-123456
```

Series válidas:

- A
- B
- C
- D
- E

Reglas:

- debe iniciar con `FAC`
- serie válida
- número de 6 dígitos

---

# Funcionamiento general

El programa:

1. Lee los códigos desde `stdin`
3. Detecta automáticamente el tipo
4. Ejecuta su validación correspondiente
5. Genera la salida en formato CSV con:

- código ingresado
- tipo detectado
- resultado (`valido` o `invalido`)

---

# Autor
Rodas Sánchez Damaris Pamela.