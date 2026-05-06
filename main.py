import tkinter as tk
from ui import GameApp


def main():
    root = tk.Tk()
    app = GameApp(root)
    app.main_menu()
    root.mainloop()

if __name__ == "__main__":
    main()
