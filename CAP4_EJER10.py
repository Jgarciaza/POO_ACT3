import tkinter as tk
from tkinter import messagebox

class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_pago_matricula(self):
        valor_constante = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            return valor_constante + (self.patrimonio * 0.03)
        return valor_constante

class InterfazUsuario:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cálculo de Matrícula")

        tk.Label(self.ventana, text="Número de Inscripción:").grid(row=0, column=0, padx=10, pady=5)
        self.campo_numero_inscripcion = tk.Entry(self.ventana)
        self.campo_numero_inscripcion.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
        self.campo_nombres = tk.Entry(self.ventana)
        self.campo_nombres.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=5)
        self.campo_patrimonio = tk.Entry(self.ventana)
        self.campo_patrimonio.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Estrato Social:").grid(row=3, column=0, padx=10, pady=5)
        self.campo_estrato = tk.Entry(self.ventana)
        self.campo_estrato.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).grid(row=4, column=0, columnspan=2, pady=10)

    def capturar_datos(self):
        try:
            numero_inscripcion = self.campo_numero_inscripcion.get()
            nombres = self.campo_nombres.get()
            patrimonio = float(self.campo_patrimonio.get())
            estrato = int(self.campo_estrato.get())
            return numero_inscripcion, nombres, patrimonio, estrato
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")
            return None, None, None, None

    def calcular(self):
        numero_inscripcion, nombres, patrimonio, estrato = self.capturar_datos()
        if None not in (numero_inscripcion, nombres, patrimonio, estrato):
            estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)
            pago_matricula = estudiante.calcular_pago_matricula()
            messagebox.showinfo(
                "Resultados", 
                f"Número de Inscripción: {numero_inscripcion}\nNombres: {nombres}\nPago de Matrícula: ${pago_matricula:.2f}"
            )

    def ejecutar(self):
        self.ventana.mainloop()

class Cap3Ejercicio:
    @staticmethod
    def main():
        app = InterfazUsuario()
        app.ejecutar()

if __name__ == "__main__":
    Cap3Ejercicio.main()
