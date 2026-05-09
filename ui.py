from player import Player
from helpers import write
from storage_unit import StorageUnit
import tkinter as tk

class GameApp():
    def __init__(self, root, player):
        self.root = root
        self.player = player

        self.storage_unit = StorageUnit(root, player, self)
        self.root.title("Storage Searchers")
        self.root.geometry("800x700")
        self.root.configure(bg="black")
        
        self.background_screen = tk.Text(self.root, padx=5, pady=5, background="black", foreground="white", font=("Fixedsys", 18))
        self.unit_frame = tk.Frame(root, bg="gray")
        self.hud = tk.Label(root, bg="gray", fg="white", text=f"${self.player.money}", font=("Fixedsys", 16))
        self.continue_button = tk.Button(self.root, text="Continue", command=self.get_name, background="white", fg="black")
        self.inventory_button = tk.Button(self.root, text="Inventory", command=self.show_inventory, background="white", foreground="black")
        #inventory_back_button = tk.Button(self.root, text="Back", command=return_from_inventory, background="white", foreground="black")
        
        self.background_screen.tag_configure("center", justify="center")

        
    def main_menu(self):
        self.player.current_state = "main menu"

        self.play_button = tk.Button(self.root, text="Play", command=self.intro_screen, background="white", foreground="black")
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_game, background="white", foreground="black")
        self.settings_button = tk.Button(self.root, text="Settings", command=self.settings, background="white", foreground="black")

        self.background_screen.pack(side="top", fill="x", expand=True)
        write(self.background_screen, "\n\n\n\n Storage Searchers", True, "center")

        self.play_button.place(relx=0.5, rely=0.5, anchor="center", width=150, height=50)
        self.quit_button.place(relx=0.5, rely=0.7, anchor="center", width=150, height=50)
        self.settings_button.place(relx=0.5, rely=0.6, anchor="center", width=150, height=50)

    def show_inventory(self):
        self.continue_button.place_forget()
        if self.player.current_state != "main lot" and self.player.current_state == "tutorial":
            for box in self.storage_unit.active_boxes:
                box.place_forget()
        elif self.player.current_state == "main lot":
            self.storage_unit.unit_frame.place_forget()
        elif self.player.current_state == "open unit":
            for box in self.storage_unit.active_boxes:
                box.place_forget()
        self.background_screen.config(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="black")
        self.inventory_back_button.place(relx=0.7, rely=0.9, width=150, height=50)
        write(self.background_screen, f"\n\nInventory:\n{self.player.inventory}\n\n\n{self.player.boxes_opened}\n\n\n\nFilament: {self.player.filament}", True, "center")

    def return_from_inventory(self):
        pass


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
    
    def get_name(self):
        self.background_screen.configure(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.continue_button.place_forget()
        self.name_entry = tk.Entry(self.root, font=("Fixedsys", 16), justify="center")
        self.name_entry.place(relx=0.5, rely=0.5, anchor="center", width=200, height=40)
        self.name_entry_button = tk.Button(self.root, text="Continue", command=self.tutorial_unit)
        self.name_entry_button.place(relx=0.5, rely=0.6, anchor="center", width=150, height=50)
        self.name_entry.focus_set()
        player_name = self.name_entry.get()
        self.player_name = player_name
        #player = Player(self.player_name)
    
    def tutorial_unit(self):
        self.player.current_state = "tutorial"
        
        self.background_screen.config(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="dimgray")
        self.hud.place(rely=0.95, relx=0.5, anchor="center")
        self.name_entry.place_forget()
        self.name_entry_button.place_forget()
        self.inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
        write(self.background_screen, "\nGrandpa's Storage", True, "center")
        self.storage_unit.spawn_boxes(6)
        self.hud.lift()
        #if self.player.boxes_opened == 6:
            #self.continue_button.config(command=self.auction_lot())
            #self.continue_button.place(relx=0.1, rely=0.9, width=150, height=50)
    
    def auction_lot(self):
        pass

    def open_unit(self):
        self.player.current_state = "open unit"


    def open_shop(self):
        pass
        
    
    def quit_game(self):
        self.root.destroy()

    def settings(self):
        self.background_screen.configure(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.play_button.place_forget()
        self.quit_button.place_forget()
        self.settings_button.place_forget()
        write(self.background_screen, "\nSettings", True, "center")