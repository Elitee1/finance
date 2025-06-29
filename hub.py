from main import FinanceApp
import customtkinter

app_instance = FinanceApp()

customtkinter.CTkButton(app_instance.contentFrame, text="Ausgaben 20.01.2025", command=lambda: app_instance.show_amount(100)).pack()

app_instance.run()
