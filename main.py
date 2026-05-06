import tkinter as tk
from ui import GameApp


def main():
    GameApp(tk.Tk()).main_menu()
    root = tk.Tk()
    root.mainloop()

if __name__ == "__main__":
    main()
