from player import get_money()
from helpers import write
import tkinter as tk

class GameApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Storage Searchers")
        self.root.geometry("800x700")
        self.root.configure(bg="black")

        self.hud = tk.Label(root, bg="gray", fg="white", text=f"${self.money}", font=("Fixedsys", 16))
        self.continue_button = tk.Button(self.root, text="Continue", command=self.tutorial_unit, background="white", fg="black")

        
    def main_menu(self):
        self.background_screen = tk.Text(self.root, padx=5, pady=5, background="black", foreground="white", font=("Fixedsys", 18))
        self.background_screen.tag_configure("center", justify="center")

        self.play_button = tk.Button(self.root, text="Play", command=self.intro_screen, background="white", foreground="black")
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_game, background="white", foreground="black")
        self.settings_button = tk.Button(self.root, text="Settings", command=self.settings, background="white", foreground="black")

        self.background_screen.pack(side="top", fill="x", expand=True)
        write(self.background_screen, "\n\n\n\n Storage Searchers", True, "center")

        self.play_button.place(relx=0.5, rely=0.5, anchor="center", width=150, height=50)
        self.quit_button.place(relx=0.5, rely=0.7, anchor="center", width=150, height=50)
        self.settings_button.place(relx=0.5, rely=0.6, anchor="center", width=150, height=50)

    def show_inventory(self):
        pass
        #continue_button = tk.Button(self.root, text="Continue", command=tutorial_unit, background="white", foreground="black")
        #inventory_button = tk.Button(self.root, text="Inventory", command=show_inventory, background="white", foreground="black")
        #inventory_back_button = tk.Button(self.root, text="Back", command=return_from_inventory, background="white",
                                        #foreground="black")
        
    
    def intro_screen(self):        
        self.background_screen.configure(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.play_button.place_forget()
        self.quit_button.place_forget()
        self.settings_button.place_forget()
        self.continue_button.place(relx=0.5, rely=0.9, anchor="center", width=150, height=50)
        write(self.background_screen,
            f"\n\n\n\nWelcome to Storage Searchers, you've just lost \nyour job and taken everything out of your bank \naccount in order to fulfill a lifelong \ndream. Become rich. Buy a storage unit and pray \nto your god there's something valuable in it.",
            True, "center")
    
    def tutorial_unit(self):
        
        self.background_screen.config(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="dimgray")
        self.hud.place(rely=0.95, relx=0.5, anchor="center")
        self.continue_button.place_forget()
        self.inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
        write(self.background_screen, "\nGrandpa's Storage", True, "center")
        #spawn_boxes(6)
        
    
    def quit_game(self):
        self.root.destroy()

    def settings(self):
        self.background_screen.configure(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.play_button.place_forget()
        self.quit_button.place_forget()
        self.settings_button.place_forget()
        write(self.background_screen, "\nSettings", True, "center")