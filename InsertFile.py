import tkinter as tk
from tkinter import filedialog

import Navigation

from CreateReport import CreateReport
from GetMetaData import MetaData

class Frame(tk.Frame):
    
    def __init__(self, parent, FRAME_HEIGHT, FRAME_WIDTH):
        self.FRAME_WIDTH = FRAME_WIDTH
        self.parent = parent

        self.pad = 15
        tk.Frame.__init__(self, self.parent, height=FRAME_HEIGHT, width=FRAME_WIDTH, padx=self.pad, pady=self.pad)
        self.grid_propagate(0)
        self.grid_columnconfigure(99, weight=1)
        
        self.CostTablePath = tk.StringVar()
        self.ReferenceTablePath = tk.StringVar()

        self.CostTablePath.set(MetaData().CostTablePath)
        self.ReferenceTablePath.set(MetaData().ReferenceTablePath)

        self.MainFrame()
        self.Navigation()

    def MainFrame(self):

        header = tk.Label(self, text = "Choose Cost Table")
        header.grid(column = 0, row = 0, sticky="w")

        Entry = tk.Entry(self, textvariable = self.CostTablePath)
        Entry.grid(column = 0, row = 1, ipadx=self.FRAME_WIDTH/5, sticky="w")
        
        BrowseButton = tk.Button(self, text="Browse...",command = lambda: self.fileDialog(self.CostTablePath))
        BrowseButton.grid(column = 1, row = 1, sticky="w")


        space = tk.Label(self, text = "")
        space.grid(column = 0, row = 2, sticky="w")


        header = tk.Label(self, text = "Choose Reference Table")
        header.grid(column = 0, row = 12, sticky="w")

        Entry = tk.Entry(self, textvariable = self.ReferenceTablePath)
        Entry.grid(column = 0, row = 13, ipadx=self.FRAME_WIDTH/5, sticky="w")
        
        BrowseButton = tk.Button(self, text="Browse...",command = lambda: self.fileDialog(self.ReferenceTablePath))
        BrowseButton.grid(column = 1, row = 13, sticky="w")


    def Navigation(self):
        self.grid_rowconfigure(99, weight=1)

        nav = Navigation.Frame(self,35,self.FRAME_WIDTH-self.pad*2)
        nav.Continue(self.Calc)
        nav.grid(row=100, column=0, columnspan=3)


    def Calc(self):
        self.PleaseWait()

        MetaData().CostTablePath = self.CostTablePath.get()
        MetaData().ReferenceTablePath = self.ReferenceTablePath.get()

        CreateReport().CalculateCosts (ReferenceTablePath=self.ReferenceTablePath.get(),CostTablePath=self.CostTablePath.get())
        self.parent.switch_frame("SelectOutput")
          
    def fileDialog(self,Path):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("Table","*.csv"),("all files","*.*")) )
        Path.set(self.filename)

    def PleaseWait(self):
        self.pack_propagate(0)

        for widget in self.winfo_children():
            widget.destroy()
        
        header = tk.Label(self, text = "Please wait...")
        header.pack()
