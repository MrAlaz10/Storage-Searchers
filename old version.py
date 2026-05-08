import tkinter as tk
import random

# ------SAVED DATA-------
inventory = {}
current_state = ""
purchased_units = []

# --------------OTHER-----------------
box_amount = 0
temp_boxes_opened = 0
active_boxes = {}
unit_prices = [150, 300, 500, 600, 800, 1000]


def buy_unit(index, price, clicked_button):
    global money
    if money >= price:
        money -= price
        hud.config(text=f"${money}")
        clicked_button.config(state="disabled", command=open_unit(), text=f"Unit #{index + 1}\nPURCHASED")
        purchased_units.append(f"Unit{index + 1}")
    else:
        error_label.place(rely=0.5, relx=0.5, anchor="center")
        error_label.lift()
        root.after(2000, error_message_remove)



def open_unit():
    global boxes_opened, current_state, temp_boxes_opened, box_amount
    temp_boxes_opened = 0
    box_amount = random.randint(5, 8)
    current_state = "open unit"
    background_screen.config(state="normal")
    unit_frame.place_forget()

    background_screen.delete("1.0", tk.END)
    background_screen.config(bg="dimgray")
    hud.place(rely=0.95, relx=0.5, anchor="center")
    write(background_screen, f"\n\n\nStorage Unit", True, "center")
    hud.lift()
    spawn_boxes(box_amount)
    if temp_boxes_opened == box_amount:
        continue_button.config(command=play_game)
        continue_button.place(relx=0.1, rely=0.9, width=150, height=50)


def play_game():
    global current_state, purchased_units
    current_state = "main lot"
    background_screen.configure(state="normal")
    background_screen.configure(background="gray")
    background_screen.delete("1.0", tk.END)
    continue_button.place_forget()
    inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)

    # hud.place(rely=0.95,relx=0.5,anchor="center")

    # enumerate() gives us BOTH the position (index: 0, 1, 2...) AND the value (price: 150, 300...)
    for index, price in enumerate(unit_prices):
        # Check affordability: Set state to NORMAL if we have enough money, otherwise DISABLED
        btn_state = tk.NORMAL if money >= price else tk.DISABLED

        # Create the button inside unit_frame
        btn = tk.Button(unit_frame, text=f"Unit #{index + 1}\nPurchase for\n ${price}",
                        bg="white", fg="black", width=15, height=5, state=btn_state)

        # THE LAMBDA TRICK:
        # We take a "snapshot" of the current index (i=index), price (p=price), and button (b=btn).
        # We put them in an "envelope" (lambda) so buy_unit doesn't run until clicked.
        btn.configure(command=lambda i=index, p=price, b=btn: buy_unit(i, p, b))

        # THE GRID MATH:
        # Floor division (// 3) handles rows: keeps 3 items per row (0,0,0, 1,1,1)
        # Modulo (% 3) handles columns: cycles through 0, 1, 2 over and over
        btn.grid(row=index // 3, column=index % 3, padx=10, pady=10)

    unit_frame.place(relx=0.5, rely=0.5, anchor="center")
    write(background_screen, f"\n\n\nStorage Lot", True, "center")


def return_from_inventory():
    global active_boxes, current_state, temp_boxes_opened, box_amount
    if current_state == "tutorial":
        background_screen.config(state="normal")
        background_screen.delete("1.0", tk.END)
        background_screen.config(bg="dimgray")
        hud.place(rely=0.95, relx=0.5, anchor="center")
        inventory_back_button.place_forget()
        inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
        if boxes_opened == 6:
            continue_button.config(command=play_game)
            continue_button.place(relx=0.1, rely=0.9, width=150, height=50)
        write(background_screen, "\nGrandpa's Storage", True, "center")
    elif current_state == "main lot":
        background_screen.configure(state="normal")
        background_screen.configure(background="gray")
        background_screen.delete("1.0", tk.END)
        continue_button.place_forget()
        inventory_back_button.place_forget()
        unit_frame.place(relx=0.5, rely=0.5, anchor="center")
        inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
        write(background_screen, f"\n\n\nStorage Lot", True, "center")
    elif current_state == "open unit":
        background_screen.config(state="normal")
        background_screen.delete("1.0", tk.END)
        background_screen.config(bg="dimgray")
        inventory_back_button.place_forget()
        if temp_boxes_opened == box_amount:
            continue_button.config(command=play_game)
            continue_button.place(relx=0.1, rely=0.9, width=150, height=50)
        inventory_button.place(relx=0.7, rely=0.9, width=150, height=50)
    for box in active_boxes:
        box.place(relx=active_boxes[box][0], rely=active_boxes[box][1])


inventory_label = tk.Label(root, bg="black", fg="white", font=("Fixedsys", 16))
error_label = tk.Label(root, bg="black", fg="red", text="ERROR", font=("Fixedsys", 20))




