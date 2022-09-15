from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # checks if there is no entry
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Make sure all fields are not empty")
    else:
        # This is the message box that checks if ok to save credentials
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \nWebsite: {website} \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("pass-data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)  # delete from first entry to end
                password_entry.delete(0, END)  # delete from first entry to end

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)  # cut (x,y) by half to center
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email / Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # focuses to this entry to start typing right away when launched
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "test@gmail.com")  # inserts prepopulated text (0 for start, END for end of another text)
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()