import tkinter as tk
from ui import GameApp
from player import Player


def main():
    root = tk.Tk()
    player = Player()
    app = GameApp(root, player)
    app.main_menu()
    root.mainloop()

if __name__ == "__main__":
    main()
