class Player():
    def __init__(self, name):
        self.name = name
        self.money = 500
        self.filament = 150
        self.items_sold = 0
        self.items_crafted = 0
        self.storage_units_opened = 0
        self.boxes_opened = 0
        self.old_3d_printer = False
        self.tutorial_completed = False

    def spend_money(self, amount):
        if amount <= self.money:
            self.money -= amount 
        else:
            pass            #add error message later  


    def add_money(self, amount):
        self.money += amount
    
    def get_money(self):
        return self.money