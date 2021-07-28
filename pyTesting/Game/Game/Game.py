from  Functions import Functions
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Game_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Game_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Game_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None



class Toplevel1:
    def flagFlipLogic(self, flag):
        if flag == True:
            self.playerFlag = False
        else:
            self.playerFlag = True
    def __init__(self, top=None):
        # Variables
        myGameLogic= Functions()
        self.playerFlag = True
        def resetLabels():
            self.Button1.configure(text=myGameLogic.location1)
            self.Button2.configure(text=myGameLogic.location2)
            self.Button3.configure(text=myGameLogic.location3)
            self.Button4.configure(text=myGameLogic.location4)
            self.Button5.configure(text=myGameLogic.location5)
            self.Button6.configure(text=myGameLogic.location6)
            self.Button7.configure(text=myGameLogic.location7)
            self.Button8.configure(text=myGameLogic.location8)
            self.Button9.configure(text=myGameLogic.location9)
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("404x341+712+419")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#17202A")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.272, rely=0.059, height=31, width=194)
        self.Label1.configure(background="#424949")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#AEB6BF")
        self.Label1.configure(text='''Game Test TicTacToe''')

        self.Button1 = tk.Button(top)
        self.Button1.configure(command=lambda:[myGameLogic.but1Function(self.playerFlag),self.Button1.configure(text=myGameLogic.location1),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button1.place(relx=0.248, rely=0.293, height=44, width=47)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#424949")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text=myGameLogic.location1)

        self.Button2 = tk.Button(top)
        self.Button2.configure(command=lambda:[myGameLogic.but2Function(self.playerFlag),self.Button2.configure(text=myGameLogic.location2),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button2.place(relx=0.446, rely=0.293, height=44, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#424949")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text=myGameLogic.location2)

        self.Button3 = tk.Button(top)
        self.Button3.configure(command=lambda:[myGameLogic.but3Function(self.playerFlag),self.Button3.configure(text=myGameLogic.location3),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button3.place(relx=0.644, rely=0.293, height=44, width=47)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#424949")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text=myGameLogic.location3)

        self.Button4 = tk.Button(top)
        self.Button4.configure(command=lambda:[myGameLogic.but4Function(self.playerFlag),self.Button4.configure(text=myGameLogic.location4),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button4.place(relx=0.248, rely=0.499, height=44, width=47)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#424949")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text=myGameLogic.location4)

        self.Button5 = tk.Button(top)
        self.Button5.configure(command=lambda:[myGameLogic.but5Function(self.playerFlag),self.Button5.configure(text=myGameLogic.location5),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button5.place(relx=0.446, rely=0.499, height=44, width=47)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#424949")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text=myGameLogic.location5)

        self.Button6 = tk.Button(top)
        self.Button6.configure(command=lambda:[myGameLogic.but6Function(self.playerFlag),self.Button6.configure(text=myGameLogic.location6),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button6.place(relx=0.644, rely=0.499, height=44, width=47)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#424949")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text=myGameLogic.location6)

        self.Button7 = tk.Button(top)
        self.Button7.configure(command=lambda:[myGameLogic.but7Function(self.playerFlag),self.Button7.configure(text=myGameLogic.location7),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button7.place(relx=0.248, rely=0.704, height=44, width=47)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#424949")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text=myGameLogic.location7)

        self.Button8 = tk.Button(top)
        self.Button8.configure(command=lambda:[myGameLogic.but8Function(self.playerFlag),self.Button8.configure(text=myGameLogic.location8),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button8.place(relx=0.446, rely=0.704, height=44, width=47)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#424949")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text=myGameLogic.location8)

        self.Button9 = tk.Button(top)
        self.Button9.configure(command=lambda:[myGameLogic.but9Function(self.playerFlag),self.Button9.configure(text=myGameLogic.location9),self.flagFlipLogic(self.playerFlag),self.Label1.configure(text=myGameLogic.result)])
        self.Button9.place(relx=0.644, rely=0.704, height=44, width=47)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#424949")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text=myGameLogic.location9)

        self.reset = tk.Button(top)
        self.reset.configure(command=lambda:[myGameLogic.resetFunction(),resetLabels()])
        self.reset.place(relx=0.880, rely=0.880, height=44, width=47)
        self.reset.configure(activebackground="#ececec")
        self.reset.configure(activeforeground="#000000")
        self.reset.configure(background="#424949")
        self.reset.configure(disabledforeground="#a3a3a3")
        self.reset.configure(foreground="#AEB6BF")
        self.reset.configure(highlightbackground="#d9d9d9")
        self.reset.configure(highlightcolor="black")
        self.reset.configure(pady="0")
        self.reset.configure(text='Reset')
if __name__ == '__main__':
    vp_start_gui()





