# main.py
import customtkinter
import pandas as pd

class FinanceApp:
    def __init__(self):
        self.datei = pd.read_csv("files/ausgaben.csv")
        self.app = customtkinter.CTk()
        self.app.geometry("800x600")
        self.app.title("Finance")

        self.kategorieFrame = customtkinter.CTkFrame(self.app, width=200)
        self.kategorieFrame.pack(side="left", fill="y", padx=12, pady=12)

        self.contentFrame = customtkinter.CTkFrame(self.app)
        self.contentFrame.pack(side="right", expand=True, fill="both", padx=12, pady=12)

        self.build_buttons()

    def build_buttons(self):
        for kategorie, betrag in zip(self.datei["Kategorie"], self.datei["Betrag"]):
            btn = customtkinter.CTkButton(
                self.kategorieFrame,
                text=kategorie,
                command=lambda b=betrag: self.show_amount(b)
            )
            btn.pack(pady=6, fill="x")

    def show_amount(self, betrag):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
        label = customtkinter.CTkLabel(self.contentFrame, text=f"{betrag} €")
        label.pack(pady=20)

    def run(self):
        self.app.mainloop()

# main.py direkt ausführbar machen
if __name__ == "__main__":
    app = FinanceApp()
    app.run()
