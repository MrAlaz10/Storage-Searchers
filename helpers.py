def write(screen, text, newline=True, tag=None, color="white"):
    screen.configure(state="normal")
    if newline:
        text += "\n"
    screen.insert(tk.END, text, tag)
    screen.configure(foreground=color)
    screen.configure(state="disabled")

def error_message_remove():
    pass