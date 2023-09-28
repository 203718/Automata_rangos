import tkinter as tk

class Automata:
    def __init__(self):
        self.estado_actual = "q0"
        self.transiciones = {
            "q0": {"567": "q1"},
            "q1": {"-": "q2"},
            "q2": {"W": "q3", "X": "q4"},
            "q3": {"Z": "q5"},
            "q5": {"-": "q7"},
            "q7": {"0": "q8", "123456789": "q9"},
            "q8": {"123456789": "q10"},
            "q10": {"DEFG": "aceptacion"},
            "q4": {"ABCDEFGHIJKLMNOPQRSTUVWX": "q6"},
            "q6": {"-": "q7"},
            "q9": {"0123456789": "q11"},
            "q11": {"DEFG": "aceptacion"}
        }

    def transicion(self, simbolo):
        for categoria, estado_siguiente in self.transiciones.get(self.estado_actual, {}).items():
            if simbolo in categoria:
                self.estado_actual = estado_siguiente
                return
        self.estado_actual = "rechazo"

    def validar_cadena(self, cadena):
        for simbolo in cadena:
            self.transicion(simbolo)
        return self.estado_actual == "aceptacion"

class AutomataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automata de Transiciones")

        self.automata = Automata()

        self.label = tk.Label(root, text="Ingrese la cadena a validar:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.validate_button = tk.Button(root, text="Validar", command=self.validar_cadena)
        self.validate_button.pack()

        self.transitions_label = tk.Label(root, text="Transiciones:")
        self.transitions_label.pack()

        self.transitions_text = tk.Text(root, height=10, width=50)
        self.transitions_text.pack()

    def validar_cadena(self):
        cadena = self.entry.get()
        self.transitions_text.delete("1.0", tk.END)
        self.transitions_text.insert(tk.END, f"Estado inicial: {self.automata.estado_actual}\n")
        for simbolo in cadena:
            self.automata.transicion(simbolo)
            self.transitions_text.insert(tk.END, f"Simbolo: {simbolo} - Estado: {self.automata.estado_actual}\n")
        self.transitions_text.insert(tk.END, f"Estado final: {self.automata.estado_actual}\n")
        self.transitions_text.insert(tk.END, f"Cadena {'valida' if self.automata.estado_actual == 'aceptacion' else 'invalida'}\n")

        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomataApp(root)
    root.mainloop()
