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

  brd_scaling = get_scaling()

if __name__ == "__main__":
  tkinter_warn("This python script is not meant to be run!")
