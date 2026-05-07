from constants import box_colors
from helpers import write
import tkinter as tk
import random
from loot import *

class StorageUnit:
    def __init__(self, root):
        self.root = root
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
        if boxes_opened == 10:
            loot = ["old 3D printer", "used filament spool"]
            self.filament += 100
            self.old_3d_printer = True
        else:
            loot = self.generate_loot(items_amount)
            for item in loot:
                if item in self.inventory:
                    self.inventory[item] += 1
                elif item in self.junk:
                    pass
                else:
                    self.inventory[item] = 1
        for item in loot:
            write(self.background_screen, item, True, "center")
        if current_state == "tutorial":
            if boxes_opened == 6:
                self.continue_button.config(command=self.play_game)
                self.continue_button.place(relx=0.1, rely=0.9, width=150, height=50)
                self.active_boxes = {}
        elif current_state == "open unit":
            if self.temp_boxes_opened == self.box_amount:
                self.continue_button.config(command=self.play_game)
                self.continue_button.place(relx=0.1, rely=0.9, width=150, height=50)