from tkinter import *   # imports every single class


def button_clicked():
    print("I Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("Chente's GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)     # adds border/padding around

# Label
my_label = Label(text="I Am A Label", font=("Ariel", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Button 1", command=button_clicked)
button.grid(column=1, row=1)

# New Button
button2 = Button(text="Button 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

# This is what keeps the window open on the screen. At end of code
window.mainloop()
