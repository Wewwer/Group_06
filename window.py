import tkinter as tk

import InsertFile, SelectOutput, Overview

WINDOW_HEIGTH = 500
WINDOW_WIDTH  = 400


class GUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Report 2000')
        self.resizable(width=0, height=0)

        self._frame = None
        # self.switch_frame("InsertFile")
        # self.switch_frame("SelectOutput")
        self.switch_frame("Overview")

    def switch_frame(self, frame_name):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = eval(frame_name+".Frame")(self,WINDOW_HEIGTH,WINDOW_WIDTH)
        self._frame.pack()