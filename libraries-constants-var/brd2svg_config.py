from lxml import etree
import svgwrite
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def tkinter_gui():
    """Open a small window to input a .brd filename and return it."""
    
    # Container for the selected filename
    result = {"filename": None}

    # Create window
    win = tk.Tk()
    win.title("BRD → SVG")

    width = 420
    height = 180

    # Centre the window
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x = int((screen_w / 2) - (width / 2))
    y = int((screen_h / 2) - (height / 2))
    win.geometry(f"{width}x{height}+{x}+{y}")
    win.resizable(False, False)

    frame = ttk.Frame(win, padding=20)
    frame.pack(expand=True)

    # Instruction label
    label = ttk.Label(
        frame,
        text="Enter the input filename (with .brd extension)"
    )
    label.pack(pady=(0, 15))

    # Entry row
    row = ttk.Frame(frame)
    row.pack()
    ttk.Label(row, text="filename:").pack(side="left", padx=(0, 10))
    filename_entry = ttk.Entry(row, width=30)
    filename_entry.pack(side="left")

    # OK button
    def submit():
        result["filename"] = filename_entry.get()
        win.destroy()

    ok_button = ttk.Button(frame, text="OK", command=submit)
    ok_button.pack(pady=20)

    filename_entry.focus()
    win.mainloop()

    return result["filename"]

def tkinter_warn(msg, title="Warning"):
    root = tk.Tk()
    root.withdraw()  # hide the main window
    messagebox.showwarning(title, msg)
    root.destroy()

def get_scaling(filename):
    global tree, root
