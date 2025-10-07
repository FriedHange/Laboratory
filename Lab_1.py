#Laboratory 1
from os import system as os
def calculate_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
    
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to the program.")
    
def find_max(*args):
    number_input = float(input("Enter numbers separated by spaces: "))
    number = [] 
    for num in str(number_input).split():
        number.append(float(num))
    
    print(f"The maximum number is: {max(number)}")
    
def create_user_profile():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    profile = {
        "First Name": first_name,
        "Last Name": last_name
    }
    while True:
        key = input("Enter additional field name (or press Enter to finish): ")
        if not key:
            break
        value = input(f"Enter value for {key}: ")
        profile[key] = value
    print("User Profile:")
    for key, value in profile.items():
        print(f"{key}: {value}")
        
def main():
    os("cls")
    while True:
        print("\nPlease choose an option:")
        print("1. Calculate area of a rectangle")
        print("2. Greet user")
        print("3. Find maximum number")
        print("4. Create user profile")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            calculate_area()
        elif choice == "2":
            greet_user()
        elif choice == "3":
            find_max()
        elif choice == "4":
            create_user_profile()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        os("pause")
        os("cls")
main()