from lxml import etree
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from brd2svg_config import *

filename = ""

def brd2svg():
  filename = tkinter_gui()

if __name__ == "__main__":
  tkinter_warn("This python script is not meant to be run!")
