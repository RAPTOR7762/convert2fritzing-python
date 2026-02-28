from lxml import etree
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from brd2svg_config import *

filename = ""

def brd2svg():
  global filename
  filename = tkinter_gui()

  tree = etree.parse(filename)
  root = tree.getroot()

  grid_element = root.find(".//grid")
  brd_scaling = 0
  brd_scaling_unit = ""
  
  svg_scaling = 0.001
  svg_scaling_unit = "inch"

  conversion_factor = 0
  
  if grid_element is not None:
    brd_scaling = float(grid.attrib.get("distance"))
    brd_scaling_unit = str(grid.attrib.get("unitdist"))
  else:
    brd_scaling = svg_scaling
    brd_scaling_unit = svg_scaling_unit

  if brd_scaling_unit == "inch":
    conversion_factor = round((brd_scaling / svg_scaling), 2)

if __name__ == "__main__":
  tkinter_warn("This python script is not meant to be run!")
