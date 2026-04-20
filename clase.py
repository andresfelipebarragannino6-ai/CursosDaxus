# Proyecto
# Comando `print()` para imprimir información

print("Semana de Python en la práctica")
print('Juancho el profe de Python')


# Recibir datos del usuario 
# Comando `input()` para recibir datos del usuario

# input("Escriba la clave: ") 
# input("Cual es el mejor lenguaje de programación: ")

# Almacenando variables 

proyecto = "Mi primer proyecto con Python"
numero = 10
# 3saludo = Esto esta mal porque no se pueden iniciar con números la declaración de variables

print(proyecto)
print(numero)
# print(Proyecto) Se salta un error por la declaración de la variable ya que son diferentes

# Mezclar todos los conceptos

proyecto = input("Escriba la descripción del proyecto: ")
horas_estimadas = input("Escriba las horas estimadas para este proyecto: ")
valor_por_hora = input("Cual es el valor de la hora trabajada: ")
plazo_estimado = input("Escriba cuanto tiempo se estima que tomara el proyecto: ")

# print(proyecto)
# print(horas_estimadas)
# print(valor_por_hora)
# print(plazo_estimado)

# Calculos con Python

# print(10+4)
# print(123-23)
# print(12*3)
# print(10/2)

valor_total = int(horas_estimadas) * int(valor_por_hora)

# print(valor_total)

# Generador de PDFs 

# 1. Crear un PDF
# 2. Defina un tipo de letra
# 3. Llenar los datos
# 4. Guardar el PDF con un nombre específico

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("Template.png", 0, 0)

pdf.text(115,145, proyecto)
pdf.text(115,160, horas_estimadas)
pdf.text(115,175, valor_por_hora)
pdf.text(115,190, plazo_estimado)
pdf.text(115,205, str(valor_total))

pdf.output("Presupuesto.pdf")

print("Presupuesto generado con éxito")