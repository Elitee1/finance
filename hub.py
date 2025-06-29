import customtkinter
import pandas as pd 
from main import main, contentFrame, app





buttonAusgabeMonat = customtkinter.CTkButton(contentFrame, text= "Ausgaben 20.01.2025", command=main)
buttonAusgabeMonat.pack(pady=12, padx=12, )


app.mainloop()



