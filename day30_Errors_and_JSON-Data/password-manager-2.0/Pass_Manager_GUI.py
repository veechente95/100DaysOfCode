from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip  # can copy text to clipboard automatically
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)  # adds character in between lists, in this case an empty space
    password_entry.insert(0, password)
    pyperclip.copy(password)  # auto copies generated pass to clipboard


# ------------------------------ SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # checks if there is no entry
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Make sure all fields are not empty")
    else:
        # try block which can fail
        try:
            with open("data.json", mode="r") as data_file:
                # reads old data as dict
                data = json.load(data_file)
        # except block deals with any failures
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # writes new data back to JSON file
                json.dump(new_data, data_file, indent=4)
        # else block which runs if there were no issues
        else:
            # updates old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # saves updates data
                json.dump(data, data_file, indent=4)
        # runs no matter what
        finally:
            website_entry.delete(0, END)  # delete from first entry to end
            password_entry.delete(0, END)  # delete from first entry to end


# ------------------------------ FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File Not Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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
website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()  # focuses to this entry to start typing right away when launched
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "test@gmail.com")  # inserts prepopulated text (0 for start, END for end of another text)
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
