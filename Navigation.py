import tkinter as tk

class Frame(tk.Frame):
    
    def __init__(self, master, height, width):
        tk.Frame.__init__(self, master, height=height, width=width)#, bg="red"
        self.grid_propagate(0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(1, weight=1)

    def Back(self,Action):
        b1 = tk.Button(self, text="Back",command=Action)
        b1.grid(column=0,row=1, padx=5, pady=5)

    def Continue(self,Action):
        b1 = tk.Button(self, text="Continue",command=Action)
        b1.grid(column=2,row=1, padx=5, pady=5)

    def Finish(self,Action):
        b1 = tk.Button(self, text="Finish",command=Action)
        b1.grid(column=3,row=1, padx=5, pady=5)