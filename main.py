import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for char in range(nr_letters)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,"end")
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#TODO don't leave the page empty
def saving():
    website_entry_data = website_entry.get()
    user_name_entry_data = user_name_entry.get()
    password_entry_data = password_entry.get()
    data = f"""Website: {website_entry_data}\n
               Username/email: {user_name_entry_data}\n
               Password: {password_entry_data}\n"""
    if website_entry_data == "":
        messagebox.showinfo(title="Warning", message="You didn't enter Website")
    elif user_name_entry_data == "":
        messagebox.showinfo(title="Warning", message="You didn't enter Neither Email or Username")
    elif password_entry_data == "":
        messagebox.showinfo(title="Warning", message="You didn't enter Password")
    else:
        is_ok = messagebox.askokcancel(title="Website",
                           message=f"These are details {data}")
        if is_ok:
            with open("C:\\Users\\timul\\Desktop\\python\\password-manger\\passwords.txt","a") as f:
                f.write(f"{data}")
        clear()

def clear():
    website_entry.delete(0,'end')
    password_entry.delete(0,'end') 
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Generator")
window.config(padx=20,pady=20)
canva = tkinter.Canvas(width=200,height=200)
myimg = tkinter.PhotoImage(file="C:\\Users\\timul\\Desktop\\python\\password-manger\\logo.png")
canva.create_image(70,100,image = myimg)
canva.grid(row=0,column=1,columnspan=2)
#labels
website = tkinter.Label(text="Website:")
website.grid(row=1,column=0)
user_name = tkinter.Label(text="Email/Username:")
user_name.grid(row=2,column=0)
password = tkinter.Label(text="Password:")
password.grid(row=3,column=0)
#Entries
website_entry = tkinter.Entry(width=41)

website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
user_name_entry = tkinter.Entry(width=41)
user_name_entry.grid(row=2,column=1,columnspan=2,pady=5)

user_name_entry.insert(0,"timuleooo0212@gmail.com")
password_entry = tkinter.Entry(width=23)
password_entry.grid(row=3,column=1,pady=5)
#Buttons
password_button = tkinter.Button(text="Generate Password",highlightthickness=0,bd=1,command=generate_password)
password_button.grid(row=3,column=2)
add_button = tkinter.Button(text="Add",width=35,highlightthickness=0,command=saving)
add_button.grid(row=4,column=1,columnspan=2,pady=5)

window.mainloop()