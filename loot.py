# ---------LOOT--------------
junk = ["broken vase", "family scrapbook", "old clothes", "useless documents", " damaged sports equipment",
        "rusty tools"]

box_items_common = [
    "small battery", "cables", "power supply", "small speaker",
    "circuit board", "large speaker", "medium battery", "computer fan"]

box_items_rare = [
    "graphics card", "ram", "processor", "hard drive", "monitor",
    "solid state drive", "motherboard", "mechanical keyboard"
]

box_items_legendary = [
    "vr headset",
    "vintage game console",
    "smart watch",
    "drone"
]

valuables_price = {
    # --- Common Items ---
    "cables": 2,
    "small battery": 3,
    "circuit board": 4,
    "small speaker": 5,
    "computer fan": 6,
    "medium battery": 8,
    "power supply": 12,
    "large speaker": 15,

    # --- Rare Items ---
    "mechanical keyboard": 25,
    "ram": 30,
    "hard drive": 35,
    "solid state drive": 45,
    "motherboard": 50,
    "monitor": 60,
    "processor": 75,
    "graphics card": 90,

    # --- Crafted / High-End Valuables ---
    "bluetooth headphones": 50,
    "vr headset": 100,
    "vintage game console": 100,
    "bluetooth speaker": 100,
    "important documents": 200,
    "smart watch": 250,
    "drone": 350,
    "desktop computer": 1500,
    "laptop": 800
}

craftable_recipes = {
    "bluetooth headphones": {"small battery": 2, "small speaker": 2},
    "bluetooth speaker": {"medium battery": 1, "large speaker": 2},
    "laptop": {"processor": 1, "ram": 1, "solid state drive": 1, "motherboard": 1, "monitor": 1, "small speaker": 2, "medium battery": 1, "computer fan": 1},
    "desktop computer": {"computer fan": 4, "processor": 1, "ram": 2, "solid state drive": 1, "motherboard": 1, "monitor": 1, "graphics card": 1, "mechanical keyboard": 1, "power supply": 1}
}

filament_cost = {
    "desktop computer": 500, 
    "bluetooth speaker": 150, 
    "bluetooth headphones": 50, 
    "laptop": 350
}

##### filament is 0.10 cents per unit, so 100 filament = $10, 500 filament = $50, etc. #####
