from tkinter import *  # imports every single class


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 3)
    km_result_label.config(text=km)


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)  # adds border/padding around

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=("Ariel", 14, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Ariel", 14, "bold"))
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=("Ariel", 14, "bold"))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Ariel", 14, "bold"))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


# This is what keeps the window open on the screen. At end of code
window.mainloop()
