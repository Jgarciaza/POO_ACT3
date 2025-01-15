import tkinter as tk
from tkinter import messagebox





def calcular_salario():
    try:
        # Obtener valores de los campos
        codigo = entry_codigo.get()
        nombres = entry_nombres.get()
        horas_trabajadas = float(entry_horas.get())
        valor_hora = float(entry_valor_hora.get())
        retencion = float(entry_retencion.get()) / 100

        # Calcular salarios
        salario_bruto = horas_trabajadas * valor_hora
        salario_neto = salario_bruto * (1 - retencion)

        # Mostrar resultados
        messagebox.showinfo("Resultados", f"Código: {codigo}\nNombre: {nombres}\nSalario Bruto: ${salario_bruto:.2f}\nSalario Neto: ${salario_neto:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Salario")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Código del Empleado:").grid(row=0, column=0, padx=10, pady=5)
entry_codigo = tk.Entry(ventana)
entry_codigo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
entry_nombres = tk.Entry(ventana)
entry_nombres.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Horas Trabajadas al Mes:").grid(row=2, column=0, padx=10, pady=5)
entry_horas = tk.Entry(ventana)
entry_horas.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Valor por Hora Trabajada:").grid(row=3, column=0, padx=10, pady=5)
entry_valor_hora = tk.Entry(ventana)
entry_valor_hora.grid(row=3, column=1, padx=10, pady=5)

tk.Label(ventana, text="Porcentaje de Retención (%):").grid(row=4, column=0, padx=10, pady=5)
entry_retencion = tk.Entry(ventana)
entry_retencion.grid(row=4, column=1, padx=10, pady=5)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_salario)
boton_calcular.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar aplicación
ventana.mainloop()