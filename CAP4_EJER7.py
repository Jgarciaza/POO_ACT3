import tkinter as tk
from tkinter import messagebox

class Comparador:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comparar(self):
        if self.a > self.b:
            return "A es mayor que B"
        elif self.a < self.b:
            return "A es menor que B"
        else:
            return "A es igual a B"

class InterfazUsuario:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Comparador de Números")

        tk.Label(self.ventana, text="Valor de A:").grid(row=0, column=0, padx=10, pady=5)
        self.campo_a = tk.Entry(self.ventana)
        self.campo_a.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Valor de B:").grid(row=1, column=0, padx=10, pady=5)
        self.campo_b = tk.Entry(self.ventana)
        self.campo_b.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Comparar", command=self.comparar).grid(row=2, column=0, columnspan=2, pady=10)

    def capturar_datos(self):
        try:
            a = float(self.campo_a.get())
            b = float(self.campo_b.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
            return None, None

    def comparar(self):
        a, b = self.capturar_datos()
        if a is not None and b is not None:
            comparador = Comparador(a, b)
            resultado = comparador.comparar()
            messagebox.showinfo("Resultado", resultado)

    def ejecutar(self):
        self.ventana.mainloop()

class Cap3Ejercicio:
    @staticmethod
    def main():
        app = InterfazUsuario()
        app.ejecutar()

if __name__ == "__main__":
    Cap3Ejercicio.main()