import tkinter as tk
from tkinter import messagebox
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

class InterfazFiguras:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Figuras Geometricas")

        tk.Button(self.ventana, text="Círculo", command=self.abrir_circulo).grid(row=0, column=0, padx=20, pady=20)
        tk.Button(self.ventana, text="Rectángulo", command=self.abrir_rectangulo).grid(row=0, column=1, padx=20, pady=20)
        tk.Button(self.ventana, text="Cuadrado", command=self.abrir_cuadrado).grid(row=1, column=0, padx=20, pady=20)
        tk.Button(self.ventana, text="Triángulo", command=self.abrir_triangulo).grid(row=1, column=1, padx=20, pady=20)
        tk.Button(self.ventana, text="Salir", command=self.ventana.quit).grid(row=2, column=0, columnspan=2, pady=20)

    def abrir_circulo(self):
        VentanaCirculo()

    def abrir_rectangulo(self):
        VentanaRectangulo()

    def abrir_cuadrado(self):
        VentanaCuadrado()

    def abrir_triangulo(self):
        VentanaTriangulo()

    def ejecutar(self):
        self.ventana.mainloop()

class VentanaCirculo:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Círculo")

        tk.Label(self.ventana, text="Radio:").grid(row=0, column=0, padx=10, pady=5)
        self.radio = tk.Entry(self.ventana)
        self.radio.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Área:").grid(row=1, column=0, padx=10, pady=5)
        self.area = tk.Entry(self.ventana, state='readonly')
        self.area.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Perímetro:").grid(row=2, column=0, padx=10, pady=5)
        self.perimetro = tk.Entry(self.ventana, state='readonly')
        self.perimetro.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).grid(row=3, column=0, pady=10)
        tk.Button(self.ventana, text="Limpiar", command=self.limpiar).grid(row=3, column=1, pady=10)
        tk.Button(self.ventana, text="Salir", command=self.ventana.destroy).grid(row=4, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            radio = float(self.radio.get())
            circulo = Circulo(radio)
            self.area.config(state='normal')
            self.area.delete(0, tk.END)
            self.area.insert(0, f"{circulo.calcular_area():.2f}")
            self.area.config(state='readonly')

            self.perimetro.config(state='normal')
            self.perimetro.delete(0, tk.END)
            self.perimetro.insert(0, f"{circulo.calcular_perimetro():.2f}")
            self.perimetro.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para el radio.")

    def limpiar(self):
        self.radio.delete(0, tk.END)
        self.area.config(state='normal')
        self.area.delete(0, tk.END)
        self.area.config(state='readonly')
        self.perimetro.config(state='normal')
        self.perimetro.delete(0, tk.END)
        self.perimetro.config(state='readonly')

class VentanaRectangulo:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Rectángulo")

        tk.Label(self.ventana, text="Base:").grid(row=0, column=0, padx=10, pady=5)
        self.base = tk.Entry(self.ventana)
        self.base.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Altura:").grid(row=1, column=0, padx=10, pady=5)
        self.altura = tk.Entry(self.ventana)
        self.altura.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Área:").grid(row=2, column=0, padx=10, pady=5)
        self.area = tk.Entry(self.ventana, state='readonly')
        self.area.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Perímetro:").grid(row=3, column=0, padx=10, pady=5)
        self.perimetro = tk.Entry(self.ventana, state='readonly')
        self.perimetro.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).grid(row=4, column=0, pady=10)
        tk.Button(self.ventana, text="Limpiar", command=self.limpiar).grid(row=4, column=1, pady=10)
        tk.Button(self.ventana, text="Salir", command=self.ventana.destroy).grid(row=5, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            base = float(self.base.get())
            altura = float(self.altura.get())
            rectangulo = Rectangulo(base, altura)
            self.area.config(state='normal')
            self.area.delete(0, tk.END)
            self.area.insert(0, f"{rectangulo.calcular_area():.2f}")
            self.area.config(state='readonly')

            self.perimetro.config(state='normal')
            self.perimetro.delete(0, tk.END)
            self.perimetro.insert(0, f"{rectangulo.calcular_perimetro():.2f}")
            self.perimetro.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para base y altura.")

    def limpiar(self):
        self.base.delete(0, tk.END)
        self.altura.delete(0, tk.END)
        self.area.config(state='normal')
        self.area.delete(0, tk.END)
        self.area.config(state='readonly')
        self.perimetro.config(state='normal')
        self.perimetro.delete(0, tk.END)
        self.perimetro.config(state='readonly')

class VentanaCuadrado:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Cuadrado")

        tk.Label(self.ventana, text="Lado:").grid(row=0, column=0, padx=10, pady=5)
        self.lado = tk.Entry(self.ventana)
        self.lado.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Área:").grid(row=1, column=0, padx=10, pady=5)
        self.area = tk.Entry(self.ventana, state='readonly')
        self.area.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Perímetro:").grid(row=2, column=0, padx=10, pady=5)
        self.perimetro = tk.Entry(self.ventana, state='readonly')
        self.perimetro.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).grid(row=3, column=0, pady=10)
        tk.Button(self.ventana, text="Limpiar", command=self.limpiar).grid(row=3, column=1, pady=10)
        tk.Button(self.ventana, text="Salir", command=self.ventana.destroy).grid(row=4, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            lado = float(self.lado.get())
            cuadrado = Cuadrado(lado)
            self.area.config(state='normal')
            self.area.delete(0, tk.END)
            self.area.insert(0, f"{cuadrado.calcular_area():.2f}")
            self.area.config(state='readonly')

            self.perimetro.config(state='normal')
            self.perimetro.delete(0, tk.END)
            self.perimetro.insert(0, f"{cuadrado.calcular_perimetro():.2f}")
            self.perimetro.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para el lado.")

    def limpiar(self):
        self.lado.delete(0, tk.END)
        self.area.config(state='normal')
        self.area.delete(0, tk.END)
        self.area.config(state='readonly')
        self.perimetro.config(state='normal')
        self.perimetro.delete(0, tk.END)
        self.perimetro.config(state='readonly')

class VentanaTriangulo:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Triángulo")

        tk.Label(self.ventana, text="Base:").grid(row=0, column=0, padx=10, pady=5)
        self.base = tk.Entry(self.ventana)
        self.base.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Altura:").grid(row=1, column=0, padx=10, pady=5)
        self.altura = tk.Entry(self.ventana)
        self.altura.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Área:").grid(row=2, column=0, padx=10, pady=5)
        self.area = tk.Entry(self.ventana, state='readonly')
        self.area.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Perímetro:").grid(row=3, column=0, padx=10, pady=5)
        self.perimetro = tk.Entry(self.ventana, state='readonly')
        self.perimetro.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Hipotenusa:").grid(row=4, column=0, padx=10, pady=5)
        self.hipotenusa = tk.Entry(self.ventana, state='readonly')
        self.hipotenusa.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).grid(row=5, column=0, pady=10)
        tk.Button(self.ventana, text="Limpiar", command=self.limpiar).grid(row=5, column=1, pady=10)
        tk.Button(self.ventana, text="Salir", command=self.ventana.destroy).grid(row=6, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            base = float(self.base.get())
            altura = float(self.altura.get())
            triangulo = TrianguloRectangulo(base, altura)
            self.area.config(state='normal')
            self.area.delete(0, tk.END)
            self.area.insert(0, f"{triangulo.calcular_area():.2f}")
            self.area.config(state='readonly')

            self.perimetro.config(state='normal')
            self.perimetro.delete(0, tk.END)
            self.perimetro.insert(0, f"{triangulo.calcular_perimetro():.2f}")
            self.perimetro.config(state='readonly')

            self.hipotenusa.config(state='normal')
            self.hipotenusa.delete(0, tk.END)
            self.hipotenusa.insert(0, f"{triangulo.calcular_hipotenusa():.2f}")
            self.hipotenusa.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para base y altura.")

    def limpiar(self):
        self.base.delete(0, tk.END)
        self.altura.delete(0, tk.END)
        self.area.config(state='normal')
        self.area.delete(0, tk.END)
        self.area.config(state='readonly')
        self.perimetro.config(state='normal')
        self.perimetro.delete(0, tk.END)
        self.perimetro.config(state='readonly')
        self.hipotenusa.config(state='normal')
        self.hipotenusa.delete(0, tk.END)
        self.hipotenusa.config(state='readonly')

if __name__ == "__main__":
    interfaz = InterfazFiguras()
    interfaz.ejecutar()
