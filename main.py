import customtkinter
import pandas as pd


def main():
    datei = pd.read_csv("files/ausgaben.csv")

    
    app = customtkinter.CTk()
    app.geometry("800x600")
    app._set_appearance_mode("System")
    app.title("Finance")

    # Haupt-Frames
    kategorieFrame = customtkinter.CTkFrame(app, width=200)
    kategorieFrame.pack(side="left", fill="y", pady=12, padx=12)

    contentFrame = customtkinter.CTkFrame(app)
    contentFrame.pack(side="right", expand=True, fill="both", pady=12, padx=12)
    contentFrame.pack_propagate(False)

    def frameSpawn(betrag):
        for widget in contentFrame.winfo_children():
            widget.destroy()
        label = customtkinter.CTkLabel(contentFrame, text=f"{betrag} €")
        label.pack(pady=20)
        print(f"Angezeigt: {betrag} €")

    
    for kategorie, betrag in zip(datei["Kategorie"], datei["Betrag"]):
        button = customtkinter.CTkButton(
            kategorieFrame,
            text=f"{kategorie}",
            command=lambda b=betrag: frameSpawn(b)
        )
        button.pack(pady=6, padx=12, fill="x")

    app.mainloop()


if __name__ == "__main__":
    main()
