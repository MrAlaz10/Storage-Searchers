import json
import os
import random
from loot import *
from player import Player
from helpers import write
from storage_unit import StorageUnit
from constants import font_colors
from shop import Shop
import tkinter as tk
from tkinter import ttk

class GameApp():
    def __init__(self, root, player):
        self.root = root
        self.player = player
        self.save_slot_buttons = []
        self.shop = Shop(self)

        self.storage_unit = StorageUnit(root, player, self)
        self.root.title("Storage Searchers")
        self.root.geometry("1200x1100")
        self.root.configure(bg="black")

        style = ttk.Style(self.root)
        style.theme_use("default")

        style.configure("Treeview", background="black", foreground="white", fieldbackground="black", font=("Fixedsys", 14))
        style.configure("Treeview.Heading", background="gray", foreground="white", font=("Fixedsys", 16))
        
        self.background_screen = tk.Text(self.root, padx=5, pady=5, background="black", foreground="white", font=("Fixedsys", 18))
        self.unit_frame = tk.Frame(root, bg="gray")
        self.crafting_frame = tk.Frame(root, bg="black")
        self.error_label = tk.Label(root, bg="black", fg="red", text="ERROR", font=("Fixedsys", 20))
        self.hud = tk.Label(root, bg="gray", fg="white", text=f"${self.player.money}", font=("Fixedsys", 16))
        self.continue_button = tk.Button(self.root, text="Continue", command=self.get_name, background="white", fg="black")
        self.inventory_button = tk.Button(self.root, text="Inventory", command=self.show_inventory, background="white", foreground="black")
        self.inventory_back_button = tk.Button(self.root, text="Back", command=self.return_from_inventory, background="white", foreground="black")
        self.save_quit = tk.Button(self.root, text="Save & Quit", command=self.quit_game, background="white", foreground="black")
        self.shop_button = tk.Button(self.root, text="Shop", command=self.open_shop, background="white", foreground="black")
        self.crafted_items_button = tk.Button(self.root, text="Crafted Items", state=tk.NORMAL, background="white", foreground="black", command=self.show_crafted_items)
        self.sell_button1 = tk.Button(self.root, text="Sell x1", command=lambda: self.shop.sell_item(1), background="white", foreground="black")
        self.sell_button5 = tk.Button(self.root, text="Sell x5", command=lambda: self.shop.sell_item(5), background="white", foreground="black")
        self.crafting_button = tk.Button(self.root, text="Crafting", state=tk.NORMAL, background="white", foreground="black", command=self.crafting_screen)

        self.background_screen.bind("<B1-Motion>", lambda e: "break")       # Stops click-and-drag highlighting
        self.background_screen.bind("<Double-Button-1>", lambda e: "break") # Stops double-click word highlighting
        self.background_screen.tag_configure("center", justify="center")
        
    def main_menu(self):
        self.player.current_state = "main menu"
        for btn in self.save_slot_buttons:
            btn.place_forget()
        self.inventory_back_button.place_forget()

        self.play_button = tk.Button(self.root, text="Play", command=self.intro_screen, background="white", foreground="black")
        self.load_button = tk.Button(self.root, text="Load Game", command=self.load_game_screen, background="white", foreground="black")
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_without_saving, background="white", foreground="black")
        self.settings_button = tk.Button(self.root, text="Settings", command=self.settings, background="white", foreground="black")

        self.background_screen.configure(state="normal")
        self.background_screen.delete("1.0", tk.END)
        #self.background_screen.pack(side="top", fill="x", expand=True)
        self.background_screen.place(relx=0.5, rely=0.5, anchor="center", relwidth=1.0, relheight=1.0)
        
        write(self.background_screen, "\n\n\n\n Storage Searchers", True, "center")

        self.play_button.place(relx=0.5, rely=0.5, anchor="center", width=150, height=50)
        self.load_button.place(relx=0.5, rely=0.6, anchor="center", width=150, height=50)
        self.quit_button.place(relx=0.5, rely=0.8, anchor="center", width=150, height=50)
        self.settings_button.place(relx=0.5, rely=0.7, anchor="center", width=150, height=50)

    def load_game_screen(self):
        self.background_screen.configure(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.play_button.place_forget()
        self.load_button.place_forget()
        self.quit_button.place_forget()
        self.settings_button.place_forget()
        self.inventory_back_button.place(relx=0.7, rely=0.9, width=150, height=50)
        self.inventory_back_button.config(command=self.main_menu)


        for i in range(1, 4):
            filename = f"save_file_{i}.json"
            btn_text = f"Empty Slot"
            btn_state = tk.DISABLED

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    try:
                        data = json.load(file)
                        player_name = data.get("name", "Player")
                        btn_text = f"Load: {player_name}"
                        btn_state = tk.NORMAL
                    except json.JSONDecodeError:
                        btn_text = f"Corrupted Save"
            
            save_game_button = tk.Button(self.root, text=btn_text, state=btn_state, background="white", foreground="black")
            save_game_button.config(command=lambda s=i: self.perform_load_game(s))
            save_game_button.place(relx=0.5, rely=0.3 + (i * 0.1), anchor="center", width=200, height=50)
        
            self.save_slot_buttons.append(save_game_button)
        write(self.background_screen, "\nSelect Save File", True, "center")

    def show_inventory(self):
        self.continue_button.place_forget()
        self.save_quit.place_forget()
        self.shop_button.place_forget()
        self.crafting_button.place_forget()
        
        self.crafted_items_button.place(relx=0.1, rely=0.1, width=150, height=50)
        
        if self.player.current_state != "main lot" and self.player.current_state == "tutorial":
            for box in self.storage_unit.active_boxes:
                box.place_forget()
        elif self.player.current_state == "main lot":
            self.unit_frame.place_forget()
        elif self.player.current_state == "open unit":
            for box in self.storage_unit.active_boxes:
                box.place_forget()
        
        self.background_screen.config(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="black")
        self.inventory_back_button.place(relx=0.7, rely=0.9, width=150, height=50)
        self.inventory_back_button.config(command=self.return_from_inventory)
        write(self.background_screen,
               f"\n----Inventory----\n\nBoxes Opened: {self.player.boxes_opened} --- Filament: {self.player.filament}\n\n--------------------------------------------------------\n", 
               True, "center")
        sorted_inventory = sorted(self.player.inventory.items(), key=lambda x: x[1], reverse=True)
        for item, quantity in sorted_inventory:
            color = "white"
            tag_name = "white_tag"
            if item in box_items_common:
                color = font_colors[0]
                tag_name = "common_tag"
            elif item in box_items_rare:
                color = font_colors[1]
                tag_name = "rare_tag"
            elif item in box_items_legendary:
                color = font_colors[2]
                tag_name = "legendary_tag"
            
            self.background_screen.tag_configure(tag_name, foreground=color, justify="center")
            self.background_screen.config(state="normal")
            if item not in filament_cost:
                self.background_screen.insert(tk.END, f"{item}: {quantity}\n", tag_name)
            self.background_screen.config(state="disabled")

    def show_crafted_items(self):
        self.crafted_items_button.place_forget()
        self.background_screen.config(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="black")
        self.inventory_back_button.place(relx=0.7, rely=0.9, width=150, height=50)
        self.inventory_back_button.config(command=self.show_inventory)
        write(self.background_screen,
               f"\n----Crafted Items----\n\nFilament: {self.player.filament}\n\n--------------------------------------------------------\n", 
               True, "center")
        for item in self.player.inventory:
            if item in self.player.inventory and item in filament_cost:
                color = font_colors[3]
                tag_name = "crafted_tag"

                self.background_screen.tag_configure(tag_name, foreground=color, justify="center")
                self.background_screen.config(state="normal")
                self.background_screen.insert(tk.END, f"{item}\n", tag_name)
                self.background_screen.config(state="disabled")

    def return_from_inventory(self):
        if self.player.current_state == "tutorial":
            self.background_screen.config(state="normal")
            self.background_screen.delete("1.0", tk.END)
            self.background_screen.config(bg="dimgray")
            
            self.inventory_back_button.place_forget()
            self.crafted_items_button.place_forget()
            
            self.inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
            
            write(self.background_screen, "\nGrandpa's Storage", True, "center")
            
            if self.player.boxes_opened == 6:
                self.continue_button.config(command=self.auction_lot)
                self.continue_button.place(relx=0.1, rely=0.9, width=150, height=50)
                self.active_boxes = {}
            
        
        if self.player.current_state == "main lot":
            self.background_screen.configure(state="normal")
            self.background_screen.configure(background="gray")
            self.background_screen.delete("1.0", tk.END)
            
            self.continue_button.place_forget()
            self.inventory_back_button.place_forget()
            self.crafted_items_button.place_forget()
            if hasattr(self, 'shop_tree') and self.shop_tree.winfo_exists():
                self.shop_tree.destroy()

            self.unit_frame.place(relx=0.5, rely=0.5, anchor="center")
            self.save_quit.place(relx=0.1, rely=0.1, width=150, height=50)
            self.inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
            self.shop_button.place(relx=0.7, rely=0.1, width=150, height=50)
            if self.player.old_3d_printer == True:
                self.crafting_button.place(relx=0.7, rely=0.15, width=150, height=50)
            
            write(self.background_screen, f"\n\n\nStorage Lot", True, "center")
        
        if self.player.current_state == "open unit":
            self.background_screen.config(state="normal")
            self.background_screen.delete("1.0", tk.END)
            self.background_screen.config(bg="dimgray")
            
            self.inventory_back_button.place_forget()
            self.crafted_items_button.place_forget()
            
            write(self.background_screen, f"\n\n\nStorage Unit", True, "center")
            
            self.inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
            
            if self.storage_unit.temp_boxes_opened == self.box_amount:
                self.continue_button.config(command=self.auction_lot)
                self.continue_button.place(relx=0.1, rely=0.9, width=150, height=50)
                self.active_boxes = {}

        for box in self.storage_unit.active_boxes:
            box.place(relx=self.storage_unit.active_boxes[box][0], rely=self.storage_unit.active_boxes[box][1])

    def intro_screen(self):        
        self.background_screen.configure(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.play_button.place_forget()
        self.quit_button.place_forget()
        self.load_button.place_forget()
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
    
    def tutorial_unit(self):
        self.player.current_state = "tutorial"
        self.player.name = self.name_entry.get()
        self.player.current_save_slot = self.player.get_empty_slot()
        self.player.save_game(self.player.current_save_slot)
        
        self.background_screen.config(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="dimgray")
        self.hud.place(rely=0.95, relx=0.5, anchor="center")
        self.name_entry.place_forget()
        self.name_entry_button.place_forget()
        self.hud.config(text=f"${self.player.money}")
        self.inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
        write(self.background_screen, "\nGrandpa's Storage", True, "center")
        self.storage_unit.spawn_boxes(6)
        self.hud.lift()

    def auction_lot(self):
        self.player.current_state = "main lot"        
        
        self.continue_button.place_forget()
        self.inventory_back_button.place_forget()        
        self.crafted_items_button.place_forget()
        self.sell_button1.place_forget()
        self.sell_button5.place_forget()
        if hasattr(self, 'shop_tree') and self.shop_tree.winfo_exists():
            self.shop_tree.destroy()

        self.background_screen.configure(state="normal")
        self.background_screen.configure(background="gray")
        self.background_screen.delete("1.0", tk.END)

        self.hud.config(text=f"${self.player.money}")
        
        self.hud.place(rely=0.95, relx=0.5, anchor="center")
        self.inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
        self.save_quit.place(relx=0.1, rely=0.1, width=150, height=50)
        self.shop_button.place(relx=0.7, rely=0.1, width=150, height=50)
        if self.player.old_3d_printer == True:
            self.crafting_button.place(relx=0.7, rely=0.15, width=150, height=50)

        # enumerate() gives us BOTH the position (index: 0, 1, 2...) AND the value (price: 150, 300...)
        for index, price in enumerate(self.storage_unit.unit_prices):
        # Check affordability: Set state to NORMAL if we have enough money, otherwise DISABLED
            if (index + 1) in self.player.purchased_units:
                btn_state = tk.DISABLED
                btn_text = f"Unit #{index + 1}\nPurchased"
            else:

                btn_state = tk.NORMAL if self.player.money >= price else tk.DISABLED
                btn_text = f"Unit #{index + 1}\nPurchase for\n ${price}"
            # Create the button inside unit_frame
            btn = tk.Button(self.unit_frame, text=btn_text,
                            bg="white", fg="black", width=15, height=5, state=btn_state)

            # THE LAMBDA TRICK:
            # We take a "snapshot" of the current index (i=index), price (p=price), and button (b=btn).
            # We put them in an "envelope" (lambda) so buy_unit doesn't run until clicked.
            btn.configure(command=lambda i=index, p=price, b=btn: self.storage_unit.buy_unit(i, p, b))

            # THE GRID MATH:
            # Floor division (// 3) handles rows: keeps 3 items per row (0,0,0, 1,1,1)
            # Modulo (% 3) handles columns: cycles through 0, 1, 2 over and over
            btn.grid(row=index // 3, column=index % 3, padx=10, pady=10)
            
        self.unit_frame.place(relx=0.5, rely=0.5, anchor="center")
        write(self.background_screen, f"\n\n\nStorage Lot", True, "center")

    def open_unit(self):
        self.player.current_state = "open unit"
        self.save_quit.place_forget()
        self.box_amount = random.randint(5, 8)
        self.background_screen.config(state="normal")
        self.unit_frame.place_forget()
        self.shop_button.place_forget()
        self.inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="dimgray")
        self.hud.place(rely=0.95, relx=0.5, anchor="center")
        write(self.background_screen, f"\n\n\nStorage Unit", True, "center")
        self.storage_unit.spawn_boxes(self.box_amount)
        self.hud.lift()
    
    def open_shop(self):
        self.background_screen.config(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="black")
        
        self.inventory_button.place_forget()
        self.save_quit.place_forget()
        self.shop_button.place_forget()
        self.unit_frame.place_forget()
        self.crafting_button.place_forget()
        
        self.inventory_back_button.place(relx=0.7, rely=0.9, width=150, height=50)
        self.inventory_back_button.config(command=self.auction_lot)
        
        write(self.background_screen, f"\n\nShop is currently under construction!", True, "center")

        self.shop_tree = ttk.Treeview(self.root, columns=("Item", "Quantity", "Value"), show="headings")
        
        self.shop_tree.heading("Item", text="Item Name")
        self.shop_tree.heading("Quantity", text="Qty")
        self.shop_tree.heading("Value", text="Value($)")

        self.shop_tree.column("Item", width=250, anchor="w") # "w" means West/Left-aligned
        self.shop_tree.column("Quantity", width=100, anchor="center")
        self.shop_tree.column("Value", width=100, anchor="center")

        self.shop_tree.tag_configure("common_tag", foreground=font_colors[0])
        self.shop_tree.tag_configure("rare_tag", foreground=font_colors[1])
        self.shop_tree.tag_configure("legendary_tag", foreground=font_colors[2])
        self.shop_tree.tag_configure("crafted_tag", foreground=font_colors[3])
        self.shop_tree.tag_configure("white tag", foreground="white")

        self.shop_tree.place(relx=0.5, rely=0.5, anchor="center", height=600, width=700)
        self.sell_button1.place(relx=0.27, rely=0.8, width=150, height=50)
        self.sell_button5.place(relx=0.6, rely=0.8, width=150, height=50)

        sorted_inventory = sorted(self.player.inventory.items(), key=lambda x: x[1], reverse=True)
        for item, quantity in sorted_inventory:
            color_tag = "white tag"
            if item in box_items_common:
                color_tag = "common_tag"
            elif item in box_items_rare:
                color_tag = "rare_tag"
            elif item in box_items_legendary:
                color_tag = "legendary_tag"
            elif item in filament_cost:
                color_tag = "crafted_tag"

            self.shop_tree.insert("", tk.END, values=(item, quantity, valuables_price.get(item, "N/A")), tags=(color_tag,))

    def quit_game(self):
        self.player.save_game(self.player.current_save_slot)
        self.root.destroy()

    def quit_without_saving(self):
        self.root.destroy()

    def settings(self):
        self.background_screen.configure(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.play_button.place_forget()
        self.quit_button.place_forget()
        self.settings_button.place_forget()
        write(self.background_screen, "\nSettings", True, "center")

    def perform_load_game(self, i):
        for btn in self.save_slot_buttons:
            btn.place_forget()
        self.player.load_game(i)
        self.hud.config(text=f"${self.player.money}")

        self.auction_lot()

    def show_loot_overlay(self, loot):
        for box in self.storage_unit.active_boxes:
            box.config(state=tk.DISABLED)
        
        self.loot_frame = tk.Frame(self.root, bg="black", highlightbackground="white", highlightthickness=2, bd=2, relief=tk.RIDGE)
        self.loot_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=400)
        tk.Label(self.loot_frame, text="Loot Found!", font=("Fixedsys", 16), bg="black", fg="white").pack(pady=10)

        for item in loot:
            color = "white"
            if item in box_items_common:
                color = font_colors[0]
            elif item in box_items_rare:
                color = font_colors[1]
            elif item in box_items_legendary:
                color = font_colors[2]
            
            lbl = tk.Label(self.loot_frame, text=item, font=("Fixedsys", 14), bg="black", fg=color)
            lbl.pack(pady=2)

        self.background_screen.bind("<Button-1>", self.close_loot_overlay)
        self.loot_frame.bind("<Button-1>", self.close_loot_overlay)
        for widget in self.loot_frame.winfo_children():
            widget.bind("<Button-1>", self.close_loot_overlay)
        
    def close_loot_overlay(self, event):
        self.loot_frame.destroy()
        self.background_screen.unbind("<Button-1>")
        for box in self.storage_unit.active_boxes:
            box.config(state=tk.NORMAL)

    def crafting_screen(self):
        self.background_screen.config(state="normal")
        self.background_screen.delete("1.0", tk.END)
        self.background_screen.config(bg="black")
        
        self.inventory_button.place_forget()
        self.save_quit.place_forget()
        self.shop_button.place_forget()
        self.unit_frame.place_forget()
        self.crafting_button.place_forget()
        
        self.inventory_back_button.place(relx=0.7, rely=0.9, width=150, height=50)
        self.inventory_back_button.config(command=self.auction_lot)
        
        for item in 
            craft_items_button = tk.Button(self.crafting_frame, text=btn_text, 
                                       bg="white", fg="black", width=15, height=5, state=btn_state )
            self.crafting_frame.place(relx=0.5, rely=0.5)
        
        write(self.background_screen, f"\n\nCrafting Screen is currently under construction!", True, "center")
