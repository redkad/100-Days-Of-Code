from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry_field.delete(0, END)


    pass_entry_field.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_field.get()
    email = email_entry_field.get()
    password = pass_entry_field.get()

    if website or email or password is None:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty")

    else:
        is_ok = messagebox.askyesno(title=website,
                                    message=f"These are the details entered: \n\nEmail: {email} \nPassword: {password}\n\nDo you want to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.writelines(f"{website} | {email}:{password}\n")

            messagebox.showinfo(message="Saved successfully", title="Info")

            website_field.delete(0, END)
            pass_entry_field.delete(0, END)
            website_field.focus()


# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Arial"

root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

website_field = Entry(width=53)
website_field.focus()
website_field.grid(row=1, column=1, columnspan=2)

email_field = Label(text="Email/Username:")
email_field.grid(row=2, column=0)

email_entry_field = Entry(width=53)
email_entry_field.insert(0, "collinstenge@gmail.com")
email_entry_field.grid(row=2, column=1, columnspan=2)

pass_field = Label(text="Password:")
pass_field.grid(row=3, column=0)

pass_entry_field = Entry(width=35)
pass_entry_field.grid(row=3, column=1)
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)
btn_add = Button(text="Add", width=45)
btn_add.grid(row=5, column=1, columnspan=3)
btn_add.config(command=save_pass)

txt = pass_entry_field.get()
print(txt)

root.mainloop()
