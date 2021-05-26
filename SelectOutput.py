import tkinter as tk
from tkinter import ttk

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
        
        self.SubFrame = SubFrame(self, FRAME_WIDTH-2*self.pad)
        self.ShowDetail = tk.IntVar()
        self.TimeFrame = tk.StringVar()

        self.ExcelContent = MetaData().ExcelContent
        
        self.MainFrame ()
        self.Navigation()
        
        self.ChooseTimeFrame()

    def MainFrame (self):

        RMonth = tk.Radiobutton(self, text="Month", variable = self.TimeFrame, value = "Month", command=self.ChooseTimeFrame) # state=DISABLED; state=NORMAL
        RMonth.grid(column = 0, row = 1)

        RQuarter = tk.Radiobutton(self, text="Quarter", variable = self.TimeFrame, value = "Quarter", command=self.ChooseTimeFrame)
        RQuarter.grid(column = 1, row = 1)

        RYear = tk.Radiobutton(self, text="Year", variable = self.TimeFrame, value = "Year", command=self.ChooseTimeFrame)
        RYear.grid(column = 2, row = 1)

        # Abhängigkeit
        RMonth.select()

        ShowDetailButton = tk.Checkbutton(self, text="Create Report", variable=self.ShowDetail, onvalue=1, offvalue=0,command = self.UpdateDetails)
        ShowDetailButton.grid(column=0, row=2, columnspan=3, sticky="w")

        sep = ttk.Separator(self,orient='horizontal')
        sep.grid(column=0, row=3, sticky=(tk.W, tk.E), columnspan=3)

        self.SubFrame.grid(column=0, row=4, columnspan=3)


    def Navigation(self):
        self.grid_rowconfigure(99, weight=1)
        
        nav = Navigation.Frame(self,35,self.FRAME_WIDTH-self.pad*2)
        nav.Back(lambda: {self.parent.switch_frame("InsertFile")})
        nav.grid(row=100, column=0, columnspan=3)

    def ChooseTimeFrame(self):
        self.ShowDetail.set(self.ExcelContent[self.TimeFrame.get()]["Active"])
        self.UpdateDetails()
        
    def UpdateDetails(self):
        self.ExcelContent[self.TimeFrame.get()]["Active"]=self.ShowDetail.get()

        if self.ShowDetail.get() == 1:
            self.SubFrame.Show(self.TimeFrame.get())
        else:
            self.SubFrame.ClearFrame()
            



class SubFrame(tk.Frame):
    
    def __init__(self, parent, FRAME_WIDTH):
        self.FRAME_WIDTH = FRAME_WIDTH
        self.parent = parent
        self.pad = 0
        tk.Frame.__init__(self, self.parent, width=self.FRAME_WIDTH, padx=self.pad, pady=self.pad)

        self.ExcelContent = MetaData().ExcelContent

    def Show (self,TimeFrame):
        self.ClearFrame()

        if TimeFrame == "Month":
            self.ShowMonth()
        elif TimeFrame == "Quarter":
            self.ShowQuarter()
        elif TimeFrame == "Year":
            self.ShowYear()

    def ShowMonth(self):
        header = tk.Label(self, text = "Monthly Report")
        header.grid(column = 0, row = 0)
    
    def ShowQuarter(self):
        header = tk.Label(self, text = "Quarterly Report")
        header.grid(column = 0, row = 0)

    def ShowYear(self):
        header = tk.Label(self, text = "Yearly Report")
        header.grid(column = 0, row = 0)

    def ClearFrame(self):
        for widget in self.winfo_children():
            widget.destroy()