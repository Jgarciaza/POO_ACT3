import tkinter as tk
from tkinter import messagebox
from math import sqrt

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_soluciones(self):
        discriminante = self.b**2 - 4*self.a*self.c
        if discriminante > 0:
            x1 = (-self.b + sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - sqrt(discriminante)) / (2 * self.a)
            return x1, x2
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return x, None
        else:
            return None, None

class InterfazUsuario:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ecuación de Segundo Grado")

        tk.Label(self.ventana, text="Coeficiente A:").grid(row=0, column=0, padx=10, pady=5)
        self.campo_a = tk.Entry(self.ventana)
        self.campo_a.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Coeficiente B:").grid(row=1, column=0, padx=10, pady=5)
        self.campo_b = tk.Entry(self.ventana)
        self.campo_b.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Coeficiente C:").grid(row=2, column=0, padx=10, pady=5)
        self.campo_c = tk.Entry(self.ventana)
        self.campo_c.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).grid(row=3, column=0, columnspan=2, pady=10)

    def capturar_datos(self):
        try:
            a = float(self.campo_a.get())
            b = float(self.campo_b.get())
            c = float(self.campo_c.get())
            return a, b, c
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")
            return None, None, None

    def calcular(self):
        a, b, c = self.capturar_datos()
        if None not in (a, b, c):
            ecuacion = EcuacionSegundoGrado(a, b, c)
            x1, x2 = ecuacion.calcular_soluciones()

            if x1 is not None and x2 is not None:
                messagebox.showinfo("Resultados", f"Soluciones: x1 = {x1:.2f}, x2 = {x2:.2f}")
            elif x1 is not None:
                messagebox.showinfo("Resultados", f"Solución única: x = {x1:.2f}")
            else:
                messagebox.showinfo("Resultados", "No hay soluciones reales.")

    def ejecutar(self):
        self.ventana.mainloop()

class Cap3Ejercicio:
    @staticmethod
    def main():
        app = InterfazUsuario()
        app.ejecutar()

if __name__ == "__main__":
    Cap3Ejercicio.main()
