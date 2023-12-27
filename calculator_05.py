from tkinter import *

# window and title
mega = Tk()
mega.title("Real Calculator")

# user input
e = Entry(mega, width=40, borderwidth=15)
e.grid(row=0, column=0,columnspan=4, padx=20, pady=20)

# button functions
def button_click(value):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + value)

def button_clear():
    e.delete(0, END)

def button_equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# buttons 
button_7 = Button(mega, text="7",padx=40,pady=20, command=lambda: button_click("7"))
button_7.grid(row=1, column=0)
button_8 = Button(mega, text="8",padx=40,pady=20, command=lambda: button_click("8"))
button_8.grid(row=1, column=1)
button_9 = Button(mega, text="9",padx=40,pady=20, command=lambda: button_click("9"))
button_9.grid(row=1, column=2)
button_div = Button(mega, text="/",padx=40,pady=20, command=lambda: button_click("/"))
button_div.grid(row=1, column=3)

button_4 = Button(mega, text="4",padx=40,pady=20, command=lambda: button_click("4"))
button_4.grid(row=2, column=0)
button_5 = Button(mega, text="5",padx=40,pady=20, command=lambda: button_click("5"))
button_5.grid(row=2, column=1)
button_6 = Button(mega, text="6",padx=40,pady=20, command=lambda: button_click("6"))
button_6.grid(row=2, column=2)
button_mul = Button(mega, text="*",padx=40,pady=20, command=lambda: button_click("*"))
button_mul.grid(row=2, column=3)

button_1 = Button(mega, text="1",padx=40,pady=20, command=lambda: button_click("1"))
button_1.grid(row=3, column=0)
button_2 = Button(mega, text="2",padx=40,pady=20, command=lambda: button_click("2"))
button_2.grid(row=3, column=1)
button_3 = Button(mega, text="3",padx=40,pady=20, command=lambda: button_click("3"))
button_3.grid(row=3, column=2)
button_sub = Button(mega, text="-",padx=40,pady=20, command=lambda: button_click("-"))
button_sub.grid(row=3, column=3)
button_add = Button(mega, text="+",padx=40,pady=20, command=lambda: button_click("+"))
button_add.grid(row=4, column=3)

button_0 = Button(mega, text="0",padx=40,pady=20, command=lambda: button_click("0"))
button_0.grid(row=4, column=0, columnspan=2, sticky="we")
button_dot = Button(mega, text=".",padx=40,pady=20, command=lambda: button_click("."))
button_dot.grid(row=4, column=2, sticky="we")
button_equal = Button(mega, text="=",padx=40,pady=20, command=button_equal)
button_equal.grid(row=5, column=2, columnspan=2, sticky="we")

button_clear = Button(mega, text="Clear", padx=40,pady=20,command=button_clear)
button_clear.grid(row=5, column=0, columnspan=2, sticky="we")

# main loop
mega.mainloop()
