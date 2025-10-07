#Laboratory 1
from os import system as os
clear_screen = lambda: os('cls')
def string_manipulation_name():
    name = input("Enter your full name(Merge your last name if it consists of two words): ").strip()
    names = name.split()
    
    if len(names) > 1:
        first_name = " ".join(name.capitalize() for name in names[:-1])
        last_name = names[-1].capitalize()
        
        print(f"First name: {first_name}")
        print(f"Last name: {last_name}")
    elif len(names) == 1:
        first_name = names[0].capitalize()
        print(f"First name: {first_name}")
    else:
        print("No name entered")
        
def string_formatting():
    name = input("Enter your full name(Merge your last name if it consists of two words): ").strip()
    names = name.split()
    
    if len(names) > 1:
        first_name = " ".join(name.capitalize() for name in names[:-1])
        last_name = names[-1].capitalize()
        
        print(f"First name: {first_name}")
        print(f"Last name: {last_name}")
    elif len(names) == 1:
        first_name = names[0].capitalize()
        print(f"First name: {first_name}")
    else:
        print("No name entered")

def file_name():
    first_name = str(input("Enter your first name: "))
    clear_screen()
    last_name = str(input("Enter your last name: "))
    clear_screen()
    file_use = str(input("Enter a word to summarize \nthe contents of the file(e.g., 'data', 'info', 'report'): "))
    clear_screen()
    extension = str(input("Enter the file extension (e.g., 'txt', 'csv', 'docx'): "))
    clear_screen()
    file_name = "{}_{}_{}_11-09-2001.{}".format(first_name.lower(), last_name.lower(), file_use.lower(),extension.lower())
    clear_screen()
    print(f"Generated file name: {file_name}")
    
def is_valid_password(password):
    clear_screen()
    if len(password) < 8:
        print("Password should be at least 8 characters.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password should contain at least one digit.")
        return False
    if not any(char.isupper() for char in password):
        print("Password should contain at least one uppercase letter.")
        return False
    if not any(char.islower() for char in password):
        print("Password should contain at least one lowercase letter.")
        return False

    print("Password is valid.")
    return True

def sentence_manipulation():
    sentence = input("Enter a sentence: ").strip()
    words = sentence.split()
    
    if not words:
        print("No sentence entered.")
        return
    reversed_words = words[::-1]
    print("Reversed sentence:", " ".join(reversed_words))   

def main():
    clear_screen()
    while True:
        print("\nPlease choose an option:")
        print("1. Split Full name")
        print("2. File name \"generator\"")
        print("3. Password Validator")
        print("4. Reverse a Sentence")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            string_manipulation_name()
        elif choice == "2":
            file_name()
        elif choice == "3":
            while True:
                password = is_valid_password(input("Enter a password to validate: "))
                print(f"Result: {password}")
                os("pause")
                clear_screen()
                if password:    
                    break
        elif choice == "4":
           sentence_manipulation()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        os("pause")
        clear_screen()
main()