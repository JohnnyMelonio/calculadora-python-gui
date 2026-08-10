import tkinter as tk
from tkinter import messagebox


class CalculadoraApp:
    """Calculadora simples com interface gráfica usando Tkinter."""

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("360x520")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._configure_style()
        self._create_widgets()
        self._bind_keyboard()

    def _configure_style(self):
        self.bg = "#1e1e1e"
        self.display_bg = "#252526"
        self.button_bg = "#333333"
        self.operator_bg = "#0078d4"
        self.text = "#ffffff"

        self.root.configure(bg=self.bg)

    def _create_widgets(self):
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Segoe UI", 28),
            justify="right",
            bg=self.display_bg,
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            state="readonly",
        )
        display.pack(fill="x", padx=20, pady=(25, 20), ipady=18)

        frame = tk.Frame(self.root, bg=self.bg)
        frame.pack(expand=True, fill="both", padx=15, pady=10)

        buttons = [
            ("C", 0, 0, 1, self.clear, self.button_bg),
            ("⌫", 0, 1, 1, self.backspace, self.button_bg),
            ("%", 0, 2, 1, lambda: self.add("%"), self.button_bg),
            ("/", 0, 3, 1, lambda: self.add("/"), self.operator_bg),
            ("7", 1, 0, 1, lambda: self.add("7"), self.button_bg),
            ("8", 1, 1, 1, lambda: self.add("8"), self.button_bg),
            ("9", 1, 2, 1, lambda: self.add("9"), self.button_bg),
            ("*", 1, 3, 1, lambda: self.add("*"), self.operator_bg),
            ("4", 2, 0, 1, lambda: self.add("4"), self.button_bg),
            ("5", 2, 1, 1, lambda: self.add("5"), self.button_bg),
            ("6", 2, 2, 1, lambda: self.add("6"), self.button_bg),
            ("-", 2, 3, 1, lambda: self.add("-"), self.operator_bg),
            ("1", 3, 0, 1, lambda: self.add("1"), self.button_bg),
            ("2", 3, 1, 1, lambda: self.add("2"), self.button_bg),
            ("3", 3, 2, 1, lambda: self.add("3"), self.button_bg),
            ("+", 3, 3, 1, lambda: self.add("+"), self.operator_bg),
            ("0", 4, 0, 2, lambda: self.add("0"), self.button_bg),
            (".", 4, 2, 1, lambda: self.add("."), self.button_bg),
            ("=", 4, 3, 1, self.calculate, self.operator_bg),
        ]

        for text, row, column, colspan, command, bg in buttons:
            button = tk.Button(
                frame,
                text=text,
                command=command,
                font=("Segoe UI", 16, "bold"),
                bg=bg,
                fg=self.text,
                activebackground="#555555",
                activeforeground=self.text,
                relief="flat",
                bd=0,
                cursor="hand2",
            )
            button.grid(
                row=row,
                column=column,
                columnspan=colspan,
                sticky="nsew",
                padx=5,
                pady=5,
                ipady=12,
            )

        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for i in range(4):
            frame.columnconfigure(i, weight=1)

        footer = tk.Label(
            self.root,
            text="Projeto de portfólio • Python + Tkinter",
            font=("Segoe UI", 9),
            bg=self.bg,
            fg="#aaaaaa",
        )
        footer.pack(pady=(0, 12))

    def _bind_keyboard(self):
        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<KP_Enter>", lambda event: self.calculate())
        self.root.bind("<Escape>", lambda event: self.clear())
        self.root.bind("<BackSpace>", lambda event: self.backspace())

        for char in "0123456789.+-*/%":
            self.root.bind(char, lambda event, c=char: self.add(c))

    def add(self, value):
        """Adiciona um caractere à expressão."""
        if self.expression == "0" and value.isdigit():
            self.expression = value
        else:
            self.expression += value
        self.display_var.set(self.expression)

    def clear(self):
        """Limpa a expressão atual."""
        self.expression = ""
        self.display_var.set("0")

    def backspace(self):
        """Remove o último caractere da expressão."""
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression or "0")

    def calculate(self):
        """Calcula a expressão matemática atual."""
        if not self.expression:
            return

        try:
            # A expressão é construída apenas pelos botões/teclas permitidos.
            result = eval(self.expression, {"__builtins__": None}, {})
            self.expression = str(result)
            self.display_var.set(self.expression)
        except (SyntaxError, TypeError, ZeroDivisionError):
            messagebox.showerror("Erro", "Expressão matemática inválida.")
            self.clear()


def main():
    root = tk.Tk()
    CalculadoraApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
