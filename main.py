import customtkinter 
import pandas as pd 

datei = pd.read_csv("files/ausgaben.csv")


def main():
    
    app = customtkinter.CTk()
    

    kategorieFrame = customtkinter.CTkFrame(app, width=300, height=600)
    kategorieFrame.pack(side="left", pady=12, padx=12, )

    contentFrame = customtkinter.CTkFrame(app)
    contentFrame.pack(side="right", expand=True, fill="both", pady=12, padx=12)


    app.geometry("600x600")
    app._set_appearance_mode("System")
    app.title("finance")


    kategoroieFrames = []
    kategorieButtons = []

    def frameSpawn( betrag):   

        for frame in contentFrame.winfo_children():
            frame.destroy()
        
        label = customtkinter.CTkLabel(contentFrame, text=betrag)
        label.pack(pady=12, padx=12)
        print("funktioniert")
        print("test")

        


    for index, (kategorie, betrag) in enumerate(zip(datei["Kategorie"], datei["Betrag"])): 

        
        frames = customtkinter.CTkFrame(app, width=400, height=600 )
        kategoroieFrames.append(frames)
        
        
        button = customtkinter.CTkButton(kategorieFrame ,text=kategorie, command= lambda b = betrag: frameSpawn( b ))
        button.pack(pady = 12, padx =12 )
        kategorieButtons.append(button)
    
 



        

    app.mainloop()

if __name__ == "__main__": 
    main()