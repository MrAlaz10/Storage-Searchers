import tkinter as tk
import json
import os

class Player():
    def __init__(self):
        self.name = "Player"
        self.money = 500
        self.filament = 150
        self.items_sold = 0
        self.items_crafted = 0
        self.storage_units_opened = 0
        self.boxes_opened = 0
        self.old_3d_printer = False
        self.tutorial_completed = False
        self.inventory = {}
        self.current_state = "main menu"
        self.purchased_units = []
        self.current_save_slot = None

    def spend_money(self, amount):
        if amount <= self.money:
            self.money -= amount 
        else:
            pass            #add error message later  
        #self.hud.config(text=f"${self.player.money}")

    def add_money(self, amount):
        self.money += amount
    
    def get_money(self):
        return self.money

    def save_game(self, i):
        player_data = {
            "name": getattr(self, "name", "Player"),
            "current_save_slot": getattr(self, "current_save_slot", 3),
            "money": self.money,
            "filament": self.filament,
            "items_sold": self.items_sold,
            "items_crafted": self.items_crafted,
            "storage_units_opened": self.storage_units_opened,
            "boxes_opened": self.boxes_opened,
            "old_3d_printer": self.old_3d_printer,
            "tutorial_completed": self.tutorial_completed,
            "inventory": self.inventory,
            "current_state": self.current_state,
            "purchased_units": self.purchased_units
        }
        with open(f"save_file_{i}.json", "w") as save_file:
            json.dump(player_data, save_file)
    
    def load_game(self, i):
        self.current_save_slot = i
        if os.path.exists(f"save_file_{i}.json"):
            with open(f"save_file_{i}.json", "r") as save_file:
                player_data = json.load(save_file)
                self.name = player_data.get("name", "Player")
                self.money = player_data.get("money", 500)
                self.filament = player_data.get("filament", 150)
                self.items_sold = player_data.get("items_sold", 0)
                self.items_crafted = player_data.get("items_crafted", 0)
                self.storage_units_opened = player_data.get("storage_units_opened", 0)
                self.boxes_opened = player_data.get("boxes_opened", 0)
                self.old_3d_printer = player_data.get("old_3d_printer", False)
                self.tutorial_completed = player_data.get("tutorial_completed", False)
                self.inventory = player_data.get("inventory", {})
                self.current_state = player_data.get("current_state", "main menu")
                self.purchased_units = player_data.get("purchased_units", [])
        else:
            print("No save file found. Starting a new game.")

    def get_empty_slot(self):
        for i in range(1, 4):
            if not os.path.exists(f"save_file_{i}.json"):
                self.current_save_slot = i
                return self.current_save_slot

        self.current_save_slot = 3
        return self.current_save_slot