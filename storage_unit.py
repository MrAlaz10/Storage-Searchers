from constants import box_colors
from helpers import write
from player import Player
import tkinter as tk
import random
from loot import *
#from ui import GameApp

class StorageUnit:
    def __init__(self, root, player, game_app):
        self.root = root
        self.player = player
        self.game_app = game_app
        self.active_boxes = {}
        self.unit_prices = [150, 300, 500, 600, 800, 1000]

    def spawn_boxes(self, max_amount):
        safe_zones = [(0.2, 0.2), (0.5, 0.3), (0.8, 0.2), (0.2, 0.6), (0.5, 0.8), (0.8, 0.5), (0.4, 0.5), (0.8, 0.8)]
        for index in range(max_amount):
            base_x = safe_zones[index][0]
            base_y = safe_zones[index][1]
            random_location_x = base_x + random.uniform(-0.06, 0.05)
            random_location_y = base_y + random.uniform(-0.06, 0.05)
            random_height = random.randint(4, 5)
            random_width = random.randint(4, 8)
            box_color_picker = random.randint(1, 4)
            box_button = tk.Button(self.root, text="Open", bg=box_colors[box_color_picker], fg="white", font=("Fixedsys", 14),
                                width=random_width, height=random_height)
            box_button.config(command=lambda b=box_button: self.open_box(b))
            box_button.place(relx=random_location_x, rely=random_location_y)
            self.active_boxes[box_button] = (random_location_x, random_location_y)
        #hud.lift()

    def open_box(self, button):
        button.place_forget()
        del self.active_boxes[button]
        items_amount = random.randint(3, 5)
        if self.player.boxes_opened == 10:
            loot = ["old 3D printer", "used filament spool"]
            self.player.filament += 100
            self.player.old_3d_printer = True
        else:
            loot = self.generate_loot(items_amount)
            for item in loot:
                if item in self.player.inventory:
                    self.player.inventory[item] += 1
                elif item in junk:
                    pass
                else:
                    self.player.inventory[item] = 1
        for item in loot:
            write(self.game_app.background_screen, item, True, "center")
        if self.player.current_state == "tutorial":
            if self.player.boxes_opened == 6:
                self.game_app.continue_button.config(command=self.game_app.play_game)
                self.game_app.continue_button.place(relx=0.1, rely=0.9, width=150, height=50)
                self.active_boxes = {}
        elif self.player.current_state == "open unit":
            if self.player.temp_boxes_opened == self.box_amount:
                self.game_app.continue_button.config(command=self.game_app.play_game)
                self.game_app.continue_button.place(relx=0.1, rely=0.9, width=150, height=50)
        
    def generate_loot(self, amount_to_roll):
        rolled_items = []
        for index in range(amount_to_roll):
            percentage = random.uniform(0.0, 1.0)
            if percentage < 0.6:
                rolled_items.append(random.choice(junk))
            elif percentage < 0.9:
                rolled_items.append(random.choice(box_items_common))
            elif percentage < 0.98:
                rolled_items.append(random.choice(box_items_rare))
            else:
                rolled_items.append(random.choice(box_items_legendary))
        return rolled_items