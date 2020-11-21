#password generator
import random, string
positive_infnity = float('inf')
password_length = int(input("How long do you want your password to be?"))

length = password_length

all_char = string.ascii_letters * 6 + string.digits + string.punctuation

list = []
for i in range(password_length):
    list.append(random.choice(all_char))


password = print("" .join(list))


def main():
    f = open("your_new_password.txt","w+")

    f.write('This is your new password ' + ("" .join(list)))

if length < 7:
    print("Passwords that are less than 7 characters are easy to crack You might want to consider using a longer pass "
          "word.")

if length in range(7, 15):
    print('This is a very secure password!')


if length > 15:
    print('Woah! This is a very secure password!')

password_save = input('do you want to save your password to a text file? y/n')
password_save.upper()

if password_save == "y":
    main()
    print("The text file has been saved to your computer")















