import tkinter as tk
from tkinter import filedialog

from lxml import etree
import svgwrite
import sexpdata

root = tk.Tk()
root.title("Convert2Fritzing")

# Small window size
root.geometry("420x120")
root.resizable(False, False)

# Main frame
frame = tk.Frame(root)
frame.pack(expand=True)

label = tk.Label(frame, text="Select tool:")
label.pack(pady=10)

button_frame = tk.Frame(frame)
button_frame.pack()

btn1 = tk.Button(button_frame, text="Convert BRD", command=brd2svg)
btn1.pack(side="left", padx=8)

btn2 = tk.Button(button_frame, text="Convert LBR", command=lbr2fzpz)
btn2.pack(side="left", padx=8)

btn3 = tk.Button(button_frame, text="Convert KiCAD_PCB", command=kicad_pcb2svg)
btn3.pack(side="left", padx=8)

root.mainloop()
