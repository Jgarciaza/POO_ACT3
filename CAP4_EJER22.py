import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, salario_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_hora = salario_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_hora * self.horas_trabajadas

class InterfazUsuario:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cálculo de Salario Mensual")

        tk.Label(self.ventana, text="Nombre del Empleado:").grid(row=0, column=0, padx=10, pady=5)
        self.campo_nombre = tk.Entry(self.ventana)
        self.campo_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Salario por Hora:").grid(row=1, column=0, padx=10, pady=5)
        self.campo_salario_hora = tk.Entry(self.ventana)
        self.campo_salario_hora.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Horas Trabajadas en el Mes:").grid(row=2, column=0, padx=10, pady=5)
        self.campo_horas_trabajadas = tk.Entry(self.ventana)
        self.campo_horas_trabajadas.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).grid(row=3, column=0, columnspan=2, pady=10)

    def capturar_datos(self):
        try:
            nombre = self.campo_nombre.get()
            salario_hora = float(self.campo_salario_hora.get())
            horas_trabajadas = float(self.campo_horas_trabajadas.get())
            return nombre, salario_hora, horas_trabajadas
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")
            return None, None, None

    def calcular(self):
        nombre, salario_hora, horas_trabajadas = self.capturar_datos()
        if None not in (nombre, salario_hora, horas_trabajadas):
            empleado = Empleado(nombre, salario_hora, horas_trabajadas)
            salario_mensual = empleado.calcular_salario_mensual()

            if salario_mensual > 450000:
                messagebox.showinfo(
                    "Resultados", 
                    f"Nombre: {nombre}\nSalario Mensual: ${salario_mensual:.2f}"
                )
            else:
                messagebox.showinfo("Resultados", f"Nombre: {nombre}")

    def ejecutar(self):
        self.ventana.mainloop()

class Cap3Ejercicio:
    @staticmethod
    def main():
        app = InterfazUsuario()
        app.ejecutar()

if __name__ == "__main__":
    Cap3Ejercicio.main()
