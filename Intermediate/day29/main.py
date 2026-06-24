from tkinter import *
import random
import string
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = string.ascii_lowercase
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title='Oops', message="Please don't leave any fields empty!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f'These are the details entered: \nEmail: {email}'
            f'\nPassword: {password} \nIs it ok to save?',
        )

        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(
                    f'{website_input.get()} | {username_input.get()} | {password_input.get()} \n'
                )
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text='Website')
website_label.grid(column=0, row=1)
username_label = Label(text='Email/Username')
username_label.grid(column=0, row=2)
password_label = Label(text='Password')
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
username_input = Entry(width=35)
username_input.insert(0, 'miguel@gmail.com')
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_pwd_button = Button(
    text='Generate Password', command=generate_password
)
generate_pwd_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
