#password generator
import random, string
from tkinter import *

window = Tk()
window.configure(bg='white')
window.geometry("570x400")
positive_infnity = float('inf')
list = []



def yes():


    f = open("your_new_password.txt","w+")
    f.write('This is your new password ' + ("" .join(list)))
    print("balls!")
    #main()
    #print("The text file has been saved to your computer")
    save = Label(window, text="The file has been saved to your computer as your_new_password.txt", font=("Helvetica", 14), fg =("black"), bg=("white"))
    save.pack()


def no():
    exit()



def button_click():
    password_length = w.get()

    length = int(password_length)
    all_char = string.ascii_letters * 6 + string.digits + string.punctuation



    for i in range(int(password_length)):
        list.append(random.choice(all_char))


    password = ("" .join(list))
    first = Label(window, text="You new password is:", font=("Helvetica", 14), fg =("black"), bg=("white"))
    first.pack()
    newpass_Message = Label(window, text=password, font=("Helvetica", 14), fg =("black"), bg=("white"))
    newpass_Message.pack()

    def main():
        f = open("your_new_password.txt","w+")


        #f.write('This is your new password ' + ("" .join(list)))

    if length < 7:
        seven = Label(window, text="Passwords that are less than 7 characters are easy to crack.", font=("Helvetica", 14), fg =("black"), bg=("white"))
        seven.pack()


    if length in range(7, 15):
        #print('This is a very secure password!')
        very = Label(window, text="This is a very secure password!", font=("Helvetica", 14), fg =("black"), bg=("white"))
        very.pack()

    if length > 15:
        #print('Woah! This is a very secure password!')
        woah = Label(window, text="Woah! This is a very secure password!", font=("Helvetica", 14), fg =("black"), bg=("white"))
        woah.pack()

    save = Label(window, text="Do you want to save your password to a text file?", font=("Helvetica", 14), fg =("black"), bg=("white"))
    save.pack()
    CheckVar1 = StringVar()
    CheckVar2 = StringVar()
    C1 = Checkbutton(window, text = "Yes", variable = CheckVar1,command=yes,  height=1, width = 3)
    C1.deselect()
    C1.pack()
    C2 = Checkbutton(window, text = "No", variable = CheckVar2,command=no, height=1, width = 3)
    C2.deselect()
    C2.pack()




w = Entry()
w.pack()
b = Button(text="Go!", command=button_click)
b.pack()
#password_length = int(input("How long do you want your password to be?"))
#length = password_length




window.mainloop()











