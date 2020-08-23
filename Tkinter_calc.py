from tkinter import *
from tkinter.messagebox import *
from random import *


def counter(key):
    if key in "0123456789+-*/.()":
        entry.insert(END, key)
    else:
        if key == "√":
            entry.insert(END, "**(0.5)")
        else:
            if key == "x²":
                entry.insert(END, "**(2)")
            else:
                if key == "x³":
                    entry.insert(END, "**(3)")
                else:
                    if key == "=":
                        try:
                            result = eval(entry.get())
                            entry.insert(END, "=" + str(result))
                        except SyntaxError:
                            showerror("Error!", "Syntax error")
                        except ZeroDivisionError:
                            showerror("Error!", "Division by zero!")
                        except NameError:
                            showerror("Error!", "Introduced text!")
                    else:
                        if key == "C":
                            entry.delete(0, END)
                        else:
                            if key == "←":
                                entry.delete(len(entry.get())-1)


def about():
    showinfo("About", "Version 2.0")


def themes(t):
    if t == 1:
        win.config(bg="lightgray")
        for i in buttons:
            i.config(fg="black", bg="white")
        win.title("Calc. White.")
    else:
        if t == 2:
            win.config(bg="darkgray")
            for i in buttons:
                i.config(fg="white", bg="dimgray")
            win.title("Calc. Dark.")
        else:
            if t == 3:
                win.config(bg="firebrick")
                win.title("Calc. Color.")
                color_random = choice(colors)
                for d in range(0, 8):
                    buttons[d].config(fg="yellow", bg=color_random)
                color_random = choice(colors)
                for d in range(8, 15):
                    buttons[d].config(fg="yellow", bg=color_random)
                color_random = choice(colors)
                for d in range(15, 24):
                    buttons[d].config(fg="yellow", bg=color_random)


def setting():
    win2 = Tk()
    win2.title("Settings")
    win2.geometry("300x150"+"+600+100")

    Label(win2, text="Themes").grid(row=0, column=0)

    t = IntVar()
    def cmd(x=1): return themes(x)
    r1 = Radiobutton(win2, text="White", variable=t, value=1, command=cmd)
    r1.grid(row=1, column=0, sticky=W)
    r1.select()

    def cmd(x=2): return themes(x)

    r2 = Radiobutton(win2, text="Dark", variable=t, value=2, command=cmd)
    r2.grid(row=2, column=0, sticky=W)

    def cmd(x=3): return themes(x)
    r3 = Radiobutton(win2, text="Color", variable=t, value=3, command=cmd)
    r3.grid(row=3, column=0, sticky=W)


win = Tk()
win.title("Calc")
win.resizable(width=False, height=False)

m = Menu(win)
win.config(menu=m)

item1 = Menu(m, tearoff=0)
m.add_cascade(label="Menu", menu=item1)
item1.add_command(label="About", command=about)

m.add_command(label="Settings", command=setting)

entry = Entry(width="60", bd=3, relief=SUNKEN)
entry.grid(row=0, columnspan=8)

colors = ["red", "green", "blue", "gray", "black"]

buttons_all = ["7", "8", "9", "0", "+", "-", "*", "/",
               "4", "5", "6", "x²", "x³", "√", "(", ")",
               "1", "2", "3", ".", "←", "C", "=", "",
               ]

buttons = []

c = 0
r = 1
for i in buttons_all:
    def cmd(x=i): return counter(x)
    btn = Button(win, text=i, width=8, bd=4, command=cmd, font=("bold"))
    btn.grid(row=r, column=c, padx=1, pady=1)
    buttons.append(btn)
    c += 1
    if c > 7:
        c = 0
        r += 1

win.mainloop()
