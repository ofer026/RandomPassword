import tkinter as tk
import random
import pyautogui

chars = ['\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't',
         'y', 'u', 'i', 'o', 'p', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'A', 'S', 'D', 'S', 'F', 'G', 'H', 'J', 'K', 'L',
         'Q',
         'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#',
         '$',
         '%', '&', '*', '(', ')', '-', '_', '=', '+', ';']


# print(chars[random.randint(0, len(chars) - 1)])
def gen_password():
    try:
        length = int(len_entry.get())
    except ValueError:
        pyautogui.alert(text="Please enter a whole number")
        return 0
    password = ""
    for char in range(length):
        password += chars[random.randint(0, len(chars) - 1)]
    genpass_display_text_field.delete("1.0", "end")
    genpass_display_text_field.insert("1.0", password)


def savepassword():
    while True:
        try:
            with open("Passwords.txt", "r+") as textg:
                a = textg.read()
                if a == "":
                    with open("Passwords.txt", "w+") as textf:
                        password_to_save = genpass_display_text_field.get("1.0", "end")
                        textf.write(password_to_save)
                        pyautogui.alert(text="Password Saved! see it at Passwords.txt")
                        textf.close()
                        break
                else:
                    with open("Passwords.txt", "a+") as textf:
                        password_to_save = genpass_display_text_field.get("1.0", "end")
                        textf.write(password_to_save)
                        pyautogui.alert(text="Password Saved! see it at Passwords.txt")
                        textf.close()
                        break
            # with open("Passwords.txt", "ar" ) as textf:
            # password_to_save = genpass_display_text_field.get("1.0", "end")
            # textf.write("\n" + password_to_save)
            # pyautogui.alert(text="Password Saved! see it at Passwords.txt")
        except FileNotFoundError:
            cr = open("Passwords.txt", "x")


win = tk.Tk()
win.geometry("800x800")
win.title("Random Password Generator")
# ------ Labels -----------
len_label = tk.Label(text="Enter the number of characters that you want your password to contain",
                     font=("Roboto Light", 16))
len_label.place(x=0, y=0)
genpass_label = tk.Label(text='Generated Password: ', font=("Roboto Light", 16))
genpass_label.place(x=2, y=44)
# -------- Entry ---------
len_entry = tk.Entry(width=28)
len_entry.place(x=4, y=28)
# ------- Text field --------
genpass_display_text_field = tk.Text(width=40, height=18, font=("Roboto Light", 14))
genpass_display_text_field.place(x=2, y=74)
# --------- Butttons ---------
gen_button = tk.Button(text="Generate Password", font=("Roboto Light", 12), width=16, height=4, command=gen_password)
gen_button.place(x=560, y=100)
save_button = tk.Button(text="Save Password", font=("Roboto Light", 12), width=16, height=4, command=savepassword)
save_button.place(x=560, y=200)

# TODO create an exe of this (make sure that every thing is good before)

win.mainloop()
