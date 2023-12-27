import random
from tkinter import*
import pyperclip

def new():
    entry.delete(0, END)
 
    # length 
    length = var1.get()
 
    inputs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
 
    for i in range(0,length):
        password = password + random.choice(inputs)
    return password
 
# generation of password
def generate():
    password1 = new()
    entry.insert(10,password1)

# accepting password 
def accept():
	store = entry.get()
	pyperclip.copy(store)
     
# reset 
def all_reset():
    for entry in root.winfo_children():
        if isinstance(entry,Entry):
            entry.delete(0,END)

# main function
root = Tk()
var1 = IntVar()
root.geometry("1000x600")

root.title("Random Password Generator")

label = Label(root, text = "PASSWORD GENERATOR", font=('Times New Roman',30,'bold','underline'),anchor=CENTER, fg='blue')
label.grid(row=0, column=1)

# User anme input
Random_password = Label(root, text="Enter User name:", font=("arial",20))
Random_password.grid(row=1, column=0, pady=7) 
entry = Entry(root, width=35, borderwidth=10, relief='ridge', font=('arial',13) )
entry.grid(row=1, column=1, pady=20)

# label of length of password
d_label = Label(root, text="Length of the password:", font=("arial",20))
d_label.grid(row=2, column=0,  pady=7)
entry = Entry(root, textvariable=var1, width=35, borderwidth=10, relief='ridge', font=('arial',13))
entry.grid(row=2, column=1, pady=20)

# generated password box
Pass_box = Label(root, text="Generated Password:", font=("arial",20))
Pass_box.grid(row=3, column=0,pady=3)
entry = Entry(root, width=29, fg='green', borderwidth=10, relief="ridge", font=('arial',15))
entry.grid(row=3, column=1, pady=20)

# generate button
genetate_button = Button(root, text="GENERATE PASSWORD", font =('arial',17,'bold'),padx=17, pady=7, command=generate, bg="blue", bd=4, fg='white', relief='solid')
genetate_button.grid(row=4, column=1, padx=17, pady=7)

# accept button
accept_button = Button(root, text="ACCEPT", font=('arial',17),padx=15, pady=7, command=accept, bg='white',bd=4, fg='blue', relief='solid')
accept_button.grid(row=5, column=1, padx=11, pady=6)

# Reset button
Reset_button = Button(root, text="RESET", font=('arial',17),padx=15, pady=6,command=lambda:all_reset(), bg='white',bd=4, fg='blue', relief='solid')
Reset_button.grid(row=6, column=1, padx=15, pady=6)

# run mainloop
root.mainloop()
