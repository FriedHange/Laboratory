from os import system
from math import sqrt
import pickle

#  Laboratory Tasks

#  Part 1: Lists Laboratory

#  Task 1.1: Student Grade Manager
# Objective: Create a program that manages student grades using lists
# Instructions:
# 1. Create two empty lists: one for student names and one for grades
# 2. Implement functions to:
#    - Add a student and their grade
#    - Calculate the average grade
#    - Find the highest grade
#    - Display all students and their grades
# 3. Test your functions with at least 3 sample students
# Expected Output:

# Added Alice with grade 85
# Added Bob with grade 92
# Added Charlie with grade 78

# Student Grades:
# Alice: 85
# Bob: 92
# Charlie: 78

# Average Grade: 85.0
# Highest Grade: 92
def student_grades(output):
    system("cls")
    students = []
    grades = []
    while True:
        system("cls")
        for i in range(len(students)):
            print(f"Added {students[i]} with a grade of {grades[i]}")
        name = output("Enter student name (Enter 'exit' to calculate the average grade): ")
        if name.lower() == 'exit':
            break
        grade = float(output(f"Enter grade for {name}: "))
        students.append(name)
        grades.append(grade)
    system("cls")
    print("Student Grades:")
    for i in range(len(students)):
        print(f"{students[i]}: {grades[i]}")
    for grade in grades:
        total = sum(grades)/len(grades)
    print(f"Average Grade: {total}")
    for grade in grades:
        high = max(grades)
        
#  Task 1.2: List Operations Practice
# Objective: Practice various list operations

# Instructions:
# 1. Create a list of numbers: [5, 2, 8, 1, 9, 3]
# 2. Perform the following operations and display results:
#    - Sort the list
#    - Calculate the sum
#    - Calculate the average
#    - Find maximum and minimum values
#    - Find the list length
def list_operations():
    numbers = []
    while True:
        system("cls")
        inputs = int(input("Enter numbers:(-1 to confirm) "))
        if inputs == -1:
            break
        numbers.append(inputs) 
        
    print("Original List:", numbers)
    numbers.sort()
    print("Sorted List:", numbers)
    total = sum(numbers)
    print("Sum:", total)
    average = total / len(numbers)
    print(f"Average: {average:.2f}")
    maximum = max(numbers)
    print("Maximum:", maximum)
    minimum = min(numbers)
    print("Minimum:", minimum)
    length = len(numbers)
    print("Length:", length)
    

#  Part 2: Tuples & Sets Laboratory
#  Task 2.1: Coordinate System with Tuples
# Objective: Use tuples to represent coordinates and calculate distances

# Instructions:
# 1. Define at least three points as tuples (x, y coordinates)
# 2. Implement functions to:
#    - Calculate distance between two points using the distance formula
#    - Find the midpoint between two points
# 3. Create a tuple containing all your points
# 4. Test your functions with sample coordinates

# Expected Formulas:
# - Distance: √[(x₂ - x₁)² + (y₂ - y₁)²]
# - Midpoint: ((x₁ + x₂)/2, (y₁ + y₂)/2)

# Important Note: Demonstrate that tuples are immutable by trying to modify one (this should cause an error)
def tuples_and_sets():
    system("cls")
    point1 = int(input("Enter x1: ")), int(input("Enter y1: "))
    point2 = int(input("Enter x1: ")), int(input("Enter y1: "))
    point3 = int(input("Enter x1: ")), int(input("Enter y1: "))
    
    def distance(p1, p2):
        return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    
    def midpoint(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    
    points = (point1, point2, point3)
    
    print(f"Distance between {point1} and {point2}: {distance(point1, point2):.2f}")
    print(f"Midpoint between {point1} and {point2}: {midpoint(point1, point2)}")
    print(f"Distance between {point2} and {point3}: {distance(point2, point3):.2f}")
    print(f"Midpoint between {point2} and {point3}: {midpoint(point2, point3)}")
    print(f"Distance between {point3} and {point1}: {distance(point3, point1):.2f}")
    print(f"Midpoint between {point3} and {point1}: {midpoint(point3, point1)}")
    
    # Code demonstarating the Immutability of tuples
    try:
        point1[0] = 10  #Declare
    except TypeError as e:
        print("Error:", e, "Tuples are not mutable :)")
    

#  Task 2.2: Unique Word Counter with Sets
# Objective: Use sets to find unique words in text

# Instructions:
# 1. Take a sample text (at least 3 sentences)
# 2. Write a program that:
#    - Splits the text into words
#    - Creates a set of unique words
#    - Counts total words and unique words
#    - Finds the most common words
# 3. Display all results

# Sample Text: "Python is a programming language. Python is easy to learn. Python is powerful."
def unique_word_counter():
    system("cls")
    sample_text = """Python is a programming language. 
                     Python is easy to learn. 
                     Python is powerful."""
    
    words = sample_text.replace('.', '').lower().split()
    unique_words = set(words)
    
    print("Total Words:", len(words))
    print("Unique Words:", len(unique_words))
    print("Unique Word List:", unique_words)
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    most_common_word = max(word_count, key=word_count.get)
    print(f"Most Common Word: '{most_common_word}' appears {word_count[most_common_word]} times")


#  Part 3: Dictionaries Laboratory
#  Task 3.1: Student Database
# Objective: Create a student database using dictionaries

# Instructions:
# 1. Create an empty dictionary for students
# 2. Implement functions to:
#    - Add a student with ID, name, grade, and major
#    - Retrieve student information by ID
#    - Update a student's grade
#    - Display all students
# 3. Test with at least 3 sample students

# Data Structure:
# students = {
#     student_id: {
#         'name': 'Student Name',
#         'grade': 'A',
#         'major': 'Computer Science'
#     }
# }

def student_database():
    system("cls")
    students = {}
    
    def add_student(student_id, name, grade, major):
        students[student_id] = {
            'name': name,
            'grade': grade,
            'major': major
        }
    
    def get_student(student_id):
        return students.get(student_id, "Student not found.")
    
    def update_grade(student_id, new_grade):
        if student_id in students:
            students[student_id]['grade'] = new_grade
        else:
            return "Student not found."
    
    def display_students():
        for student_id, info in students.items():
            print(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}, Major: {info['major']}")
    
    # Sample Data
    add_student(1, 'Alice', 'A', 'Computer Science')
    add_student(2, 'Bob', 'B', 'Mathematics')
    add_student(3, 'Charlie', 'C', 'Physics')
    
    # Testing Functions
    display_students()
    print(get_student(2))
    update_grade(2, 'A+')
    print(get_student(2))

#  Task 3.2: Word Frequency Counter
# Objective: Use dictionaries to count word frequencies

# Instructions:
# 1. Take a sample text (2-3 sentences)
# 2. Write a program that:
#    - Counts how many times each word appears
#    - Displays words sorted by frequency
#    - Identifies the most common word
# 3. Handle case sensitivity (convert all to lowercase)

def word_frequence_counter():
    system("cls")
    sample_text = """Python is a programming language. 
                    Python is easy to learn. 
                    Python is powerful."""
    print("Sample Text:\n", sample_text)
                    
    words = sample_text.replace('.', '').lower().split()    #Split into words and convert to lowercase
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    

#  Part 4: File Handling Laboratory
#  Task 4.1: Student Records File System
# Objective: Store and retrieve student records from files

# Instructions:
# 1. Implement functions to:
#    - Save student records using pickle
#    - Load student records from pickle files
#    - Export student records to a readable text file
# 2. Create sample student data
# 3. Test saving, loading, and exporting

# File Operations:
# - Use pickle.dump() for saving
# - Use pickle.load() for loading
# - Use regular file writing for text export
def file_operations():
    
    system("cls")
    students = {
        1: {'name': 'Alice', 'grade': 'A', 'major': 'Computer Science'},
        2: {'name': 'Bob', 'grade': 'B', 'major': 'Mathematics'},
        3: {'name': 'Charlie', 'grade': 'C', 'major': 'Physics'}
    }
    
    # Save student records
    with open('students.pkl', 'wb') as f:
        pickle.dump(students, f)
    
    # Load student records
    try:
        with open('students.pkl', 'rb') as f:
            loaded_students = pickle.load(f)
            print("Loaded Students:", loaded_students)
    except FileNotFoundError:
        print("File not found. Please save the records first.")
    
    # Export to text file
    with open('students.txt', 'w') as f:
        for student_id, info in students.items():
            f.write(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}, Major: {info['major']}\n")
    
    with open('students.txt', 'r') as f:
        content = f.read()
        print("Exported Student Records:\n", content)

#  Task 4.2: File Operations Practice
# Objective: Practice different file modes

# Instructions:
# 1. Create a program that demonstrates:
#    - Writing to a new file ('w' mode)
#    - Reading from a file ('r' mode)
#    - Appending to a file ('a' mode)
# 2. Use the with statement for all file operations
# 3. Handle potential file not found errors

def file_operations_practice():
    system("cls")
    # Writing to a new file
    with open('sample.txt', 'w') as f:
        f.write("This is a sample file.\n")
        f.write("It contains multiple lines of text.\n")
    
    # Reading from the file
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print("File not found. Please create the file first.")
    
    # Appending to the file
    with open('sample.txt', 'a') as f:
        f.write("This line is appended to the file.\n")
    
    # Reading again to show appended content
    with open('sample.txt', 'r') as f:
        content = f.read()
        print("Updated File Content:\n", content)



def main(choice):
    match choice:
            case 1:
                student_grades(input)
            case 2:
                list_operations()
            case 3:
                tuples_and_sets()
            case 4:
                unique_word_counter()
            case 5:
                student_database()
            case 6:
                word_frequence_counter()
            case 7:
                file_operations()
            case _:
                print("Invalid choice. Please select a number between 1 and 7.")
while True:
    system("cls")
    main(int(input("""Select Laboratory Task (1-4):
           1. Student Grade Manager
           2. List Operations Practice
           3. Tuples & Sets Laboratory
           4. Unique Word Counter
           5. Student Database
           6. Word Frequency Counter
           7. File Handling Laboratory
           Your choice: """)))
    system("pause")
    system("cls")

# Evaluation Criteria
# - Functionality (40%): All features working correctly
# - Code Quality (30%): Clean, well-organized, commented code
# - Data Structure Usage (20%): Appropriate use of lists, tuples, sets, dictionaries
# - Error Handling (10%): Proper handling of edge cases and errors

# Submission guidelines:
# Create a new public repository
# Upload all the required files 
# Copy your repository link and submit it here https://forms.gle/N2r7o4yW1skqNFu97
