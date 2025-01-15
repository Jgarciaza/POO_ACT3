import tkinter as tk
from tkinter import messagebox
from math import sqrt

class Triangulo:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (self.lado * sqrt(3)) / 2

    def calcular_area(self):
        return (self.lado ** 2 * sqrt(3)) / 4

class InterfazUsuario:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Triángulo Equilátero")

        tk.Label(self.ventana, text="Lado del triángulo:").grid(row=0, column=0, padx=10, pady=5)
        self.campo_lado = tk.Entry(self.ventana)
        self.campo_lado.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).grid(row=1, column=0, columnspan=2, pady=10)

    def capturar_datos(self):
        try:
            lado = float(self.campo_lado.get())
            return lado
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para el lado.")
            return None

    def calcular(self):
        lado = self.capturar_datos()
        if lado is not None:
            triangulo = Triangulo(lado)
            perimetro = triangulo.calcular_perimetro()
            altura = triangulo.calcular_altura()
            area = triangulo.calcular_area()

            messagebox.showinfo("Resultados", f"Perímetro: {perimetro:.2f}\nAltura: {altura:.2f}\nÁrea: {area:.2f}")

    def ejecutar(self):
        self.ventana.mainloop()

class Cap4ej19:
    @staticmethod
    def main():
        app = InterfazUsuario()
        app.ejecutar()

if __name__ == "__main__":
    Cap4ej19.main()
