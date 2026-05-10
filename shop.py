import tkinter as tk
from tkinter import ttk
from player import Player
from loot import *


class Shop:
    def __init__(self, game_app):
        self.game_app = game_app
        self.player = game_app.player

    def sell_item(self, quantity):
        selected_items = self.game_app.shop_tree.selection()
        
        if not selected_items:
            return  # No item selected, do nothing

        selected_item = selected_items[0]
        item_data = self.game_app.shop_tree.item(selected_item, "values")
        item_name = item_data[0]
        item_quantity = int(item_data[1])
        item_value = int(item_data[2])
        if quantity <= item_quantity:
            total_value = item_value * quantity
            self.player.add_money(total_value)
            self.player.inventory[item_name] -= quantity
            if self.player.inventory[item_name] == 0:
                del self.player.inventory[item_name]
            if hasattr(self.game_app, 'shop_tree') and self.game_app.shop_tree.winfo_exists():
                self.game_app.shop_tree.destroy()
            self.game_app.open_shop()
            self.game_app.hud.config(text=f"${self.player.money}")
        else:
            pass    #add error message later
        
