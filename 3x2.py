from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import random

def generar_cuentas_pdf(nombre_archivo, nombre_archivo_resultados, cantidad_cuentas):
    # Crear un lienzo para el PDF de las cuentas
    c_cuentas = canvas.Canvas(nombre_archivo, pagesize=A4)
    width, height = A4

    # Crear un lienzo para el PDF de los resultados
    c_resultados = canvas.Canvas(nombre_archivo_resultados, pagesize=A4)

    # Definir tamaño de fuente para los números
    tamano_fuente_numeros = 20

    # Definir coordenadas para las cuentas
    x_inicial = 50
    y_inicial = height - 100
    espacio_horizontal = 150
    espacio_vertical = 180  # Doble de espacio para el desarrollo manual

    # Escribir el título en el lienzo de las cuentas
    titulo = "Prácticas de multiplicación: 3 cifras por 2 cifras"
    titulo_width = c_cuentas.stringWidth(titulo, "Helvetica-Bold", 16)
    titulo_x = (width - titulo_width) / 2
    titulo_y = height - 50  # Cambiado para dejar espacio para el título
    c_cuentas.setFont("Helvetica-Bold", 16)
    c_cuentas.drawString(titulo_x, titulo_y, titulo)
    titulo_y -= 20  # Espacio adicional después del título

    # Generar las cuentas y los resultados
    resultados = []
    cuentas = []
    for i in range(cantidad_cuentas // 4):
        for j in range(4):
            # Generar números aleatorios
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 99)

            # Calcular resultado
            resultado = num1 * num2
            resultados.append(resultado)

            # Ajustar tamaño de fuente
            c_cuentas.setFont("Helvetica", tamano_fuente_numeros)

            # Escribir la cuenta en el lienzo de las cuentas
            x_actual = x_inicial + j * espacio_horizontal
            y_actual = y_inicial - (i * espacio_vertical)
            c_cuentas.drawString(x_actual + 5, y_actual, str(num1))  # Desplazar el número de arriba hacia la derecha
            c_cuentas.drawString(x_actual, y_actual - 20, "x " + str(num2))  # El "x" está en la misma línea que el segundo número
            c_cuentas.line(x_actual, y_actual - 30, x_actual + 50, y_actual - 30)  # La línea horizontal es la mitad de larga

            # Espacios para desarrollo manual en el lienzo de las cuentas
            for k in range(8):  # Doble de líneas
                c_cuentas.drawString(x_actual, y_actual - 50 - (k * 20), "")

            # Guardar las cuentas
            cuentas.append((num1, num2))

    # Guardar el PDF de las cuentas
    c_cuentas.save()

    # Escribir los resultados en el lienzo de los resultados
    y_resultados = height - 50  # Posición vertical inicial para los resultados
    for i, resultado in enumerate(resultados, start=1):
        num1, num2 = cuentas[i-1]
        c_resultados.drawString(50, y_resultados - i * 20, f"Resultado {i}: {num1} x {num2} = {resultado}")

    # Guardar el PDF de los resultados
    c_resultados.save()

# Generar los archivos PDF con 16 cuentas y los resultados
generar_cuentas_pdf("multiplicar_3x2.pdf", "resultados_multiplicar_3x2.pdf", 16)
