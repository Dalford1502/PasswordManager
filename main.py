from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_chosen = [random.choice(letters) for _ in range(random.randint(8, 10))]

    symbols_chosen = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    numbers_chosen = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_chosen + symbols_chosen + numbers_chosen
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_user_entry.get()
    pass_word = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pass_word
        }
    }

    if len(website) == 0 or len(pass_word) == 0:
        messagebox.showinfo(title="Empty dialog", message="Please ensure none of the boxes are empty")

    else:
        try:
            with open("my_passwords.json", mode="r") as save_file:
                # Read old Data
                data = json.load(save_file)

        except FileNotFoundError:
            # Catch File not found and create file
            with open("my_passwords.json", mode="w") as save_file:
                json.dump(new_data, save_file, indent=4)

        else:
            # update existing data
            data.update(new_data)
            with open("my_passwords.json", "w") as save_file:
                json.dump(data, save_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# def search_save():
#     with open("my_passwords.json") as save_file:
#         data = json.load(save_file)
#         website = website_entry.get()
#         try:
#             print(data[website])

# ---------------------------- UI SETUP ------------------------------- #


# Title
password_manager = Tk()
password_manager.title("Password Manager")
password_manager.config(padx=50, pady=50)

# Define image and apply to canvas
my_manager_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=my_manager_img)
canvas.grid(column=1, row=0)

# Define Labels and add to canvas
website_lab = Label(text="Website:")
website_lab.grid(row=1, column=0)

email_username_lab = Label(text="Email/Username:")
email_username_lab.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Define Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(0, "Default Email")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Define and add buttons
generate_pass = Button(text="Generate Password", command=gen_password)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search")
search_button.grid(row=1, column=3)

password_manager.mainloop()
