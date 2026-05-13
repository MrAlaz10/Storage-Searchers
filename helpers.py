import tkinter as tk
from loot import *

def write(screen, text, newline=True, tag=None, color="white"):
    screen.configure(state="normal")
    if newline:
        text += "\n"
    screen.insert(tk.END, text, tag)
    screen.configure(foreground=color)
    screen.configure(state="disabled")

def error_message_remove():
    pass

def check_can_craft(player, item):
    recipe = craftable_recipes[item]
    req_filament = filament_cost[item]
    if req_filament > player.filament:
        return False
    for component, required_amount in recipe.items():
        if component not in player.inventory:
            return False
        elif player.inventory[component] < required_amount:
            return False
    return True

def craft_item(player, item):
    recipe = craftable_recipes[item]
    req_filament = filament_cost[item]
    player.filament -= req_filament
    player.items_crafted += 1
    for component, required_amount in recipe.items():
        player.inventory[component] -= required_amount
        if player.inventory[component] == 0:
            del player.inventory[component]
    
    if item in player.inventory:
        player.inventory[item] += 1
    else:
        player.inventory[item] = 1
    

    

        
