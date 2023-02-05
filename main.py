from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# Password Generator Project
# creating password based on choosing random symbols
# add the functionality of removing pas
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    entry3.delete(0, END)
    password = "".join(password_list)
    entry3.insert(0, password)
    pyperclip.copy(password)


# searching for a password
# extracting data from the json file
def search():
    try:
        with open("Passwords.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="No file", message="There is no file")

    else:
        if entry1.get() in data:
            messagebox.showinfo(title=entry1.get(),
                                message=f"Email:{data[entry1.get()]['email']} \nPassword:{data[entry1.get()]['password']}")
        else:
            messagebox.showwarning(message="No website found")


# saving data to the json file
def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    # lineForFile = f"{website} | {email} |{password}\n"
    json_data = {
        website: {
               "email": email,
               "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showerror(message="There are fields empty")
        return
    else:
        try:
            with open("Passwords.json", mode="r") as file:
                try:
                    data = json.load(file)
                except:
                    data = json_data

        except FileNotFoundError:
            with open("Passwords.json", mode="w") as file:
                json.dump(json_data, file, indent=2)

        else:
            data.update(json_data)
            with open("Passwords.json", mode="w") as file:
                json.dump(data, file, indent=2)
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)


# Building ui using tkinter module
window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

entry1 = Entry(width=25)
entry1.grid(row=1, column=1)
entry1.focus()

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

entry2 = Entry(width=25)
entry2.grid(row=2, column=1)
entry2.insert(0, "Your Mail/Name")

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

entry3 = Entry(width=25)
entry3.grid(row=3, column=1)

button1 = Button(text="Generate Password", width=15, command=generatePassword)
button1.grid(row=3, column=2)

button2 = Button(text="Add", width=30, command=save)
button2.grid(row=4, column=1, columnspan=2)

button3 = Button(text="Search", width=16, command=search)
button3.grid(row=1, column=2)


window.mainloop()
