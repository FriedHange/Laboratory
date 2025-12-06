"""
Student Information Processing System
Laboratory Exercise - Regular Expressions and OOP
"""

import re


# ============================================================================
# PART 1: REGULAR EXPRESSION TASKS
# ============================================================================

# Task 1: Extract Student Data Using Regex
def extract_student_data(data):
    
    #Extract student information using regex with named groups
    
    pattern = r"ID:\s*(?P<id>\d{2}-\d{4})\s*\|\s*Name:\s*(?P<name>[A-Za-z\s]+)\s*\|\s*Email:\s*(?P<email>[\w\.-]+@[\w\.-]+\.\w+)\s*\|\s*Age:\s*(?P<age>\d+)"
    match = re.search(pattern, data)
    
    if match:
        return match.groupdict()
    return None


# Task 2: Validate Email Format
def validate_email(email):
    """
    Validate email format using regex
    - Must contain @
    - Valid domain
    - No spaces
    """
    pattern = r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(pattern, email) is not None


# Task 3: Replace Sensitive Info (Mask Email)
def mask_email(email):
    
    # Mask the username part of email with asterisks
    
    pattern = r"^[^@]+"
    masked = re.sub(pattern, "*****", email)
    return masked


# Task 4: Find All Words in a Name
def find_all_words(name):
    # Extract all words from a name using regex
    words = re.findall(r"[A-Za-z]+", name)
    return words


# ============================================================================
# PART 2: PYTHON OOP TASKS
# ============================================================================

# Task 5: Create a Student Class
class Student:
    
    # Student class with basic attributes   
    def __init__(self, student_id, name, email, age):
        self.student_id = student_id
        self.name = name
        # Task 6: Encapsulation - private attributes
        self.__email = email
        self.__age = age
    
    # Task 6: Getter and Setter methods
    def get_email(self):
        # Getter for email
        return self.__email
    
    def set_email(self, email):
        # Setter for email with validation
        if validate_email(email):
            self.__email = email
            return True
        else:
            print(f"Invalid email format: {email}")
            return False
    
    def get_age(self):
        # Getter for age
        return self.__age
    
    def set_age(self, age):
        # Setter for age
        if isinstance(age, int) and age > 0:
            self.__age = age
            return True
        else:
            print(f"Invalid age: {age}")
            return False
    
    def display_info(self):
        # Display student information
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.__age}")


# Task 8: Inheritance
class Scholar(Student):
    """
    Scholar class inheriting from Student
    Adds scholarship_type attribute
    """
    def __init__(self, student_id, name, email, age, scholarship_type):
        # Call parent constructor
        super().__init__(student_id, name, email, age)
        self.scholarship_type = scholarship_type
    
    def display_scholar_info(self):
        # Display scholar information including scholarship type
        self.display_info()
        print(f"Scholarship: {self.scholarship_type}")


# ============================================================================
# PART 3: INTEGRATION TASK
# ============================================================================

def validate_student_id(student_id):
    # Validate student ID format (YY-XXXX)
    pattern = r"^\d{2}-\d{4}$"
    return re.fullmatch(pattern, student_id) is not None


def validate_name(name):
    # Validate name contains only letters and spaces
    pattern = r"^[A-Za-z\s]+$"
    return re.fullmatch(pattern, name.strip()) is not None


def process_student_data(students_raw, scholarship_info=None):
    """
    Task 9: Full System Integration
    Process multiple student entries and create objects
    """
    student_records = []
    
    for raw_data in students_raw:
        # Extract data using regex
        data = extract_student_data(raw_data)
        
        if data:
            student_id = data['id']
            name = data['name'].strip()
            email = data['email']
            age = int(data['age'])
            
            # Validate formats
            if not validate_student_id(student_id):
                print(f"Invalid ID format: {student_id}")
                continue
            
            if not validate_name(name):
                print(f"Invalid name format: {name}")
                continue
            
            if not validate_email(email):
                print(f"Invalid email format: {email}")
                continue
            
            # Check if student is a scholar
            if scholarship_info and student_id in scholarship_info:
                student = Scholar(student_id, name, email, age, 
                                scholarship_info[student_id])
            else:
                student = Student(student_id, name, email, age)
            
            student_records.append(student)
        else:
            print(f"Could not parse data: {raw_data}")
    
    return student_records


def display_all_students(student_records):
    # Display all student information
    for student in student_records:
        if isinstance(student, Scholar):
            student.display_scholar_info()
        else:
            student.display_info()
        print("-" * 40)


# ============================================================================
# MAIN PROGRAM - DEMONSTRATION
# ============================================================================

def get_user_input():
    # Get student data from user input
    print("\n" + "=" * 60)
    print("ENTER STUDENT INFORMATION")
    print("-" * 60)
    print("(Press Enter without typing to finish adding students)")
    print()
    
    students_raw = []
    scholarship_info = {}
    
    while True:
        print(f"\n{'=' * 40}")
        print(f"Student #{len(students_raw) + 1}")
        print('=' * 40)
        
        # Get Student ID
        while True:
            student_id = input("Student ID (format: YY-XXXX, e.g., 25-1234): ").strip()
            if not student_id:
                if len(students_raw) == 0:
                    print("Please enter at least one student!")
                    continue
                else:
                    return students_raw, scholarship_info
            
            # Validate ID format
            if validate_student_id(student_id):
                break
            else:
                print("Invalid ID format! Use YY-XXXX (e.g., 25-1234)")
        
        # Get Name
        while True:
            name = input("Full Name (letters only): ").strip()
            if not name:
                print("Name cannot be empty!")
                continue
            
            # Validate name
            if validate_name(name):
                break
            else:
                print("Invalid name! Use letters and spaces only (no numbers or special characters)")
        
        # Get Email
        while True:
            email = input("Email address: ").strip()
            if not email:
                print("Email cannot be empty!")
                continue
            
            # Validate email
            if validate_email(email):
                break
            else:
                print("Invalid email format! Must contain @ and valid domain")
        
        # Get Age
        while True:
            age_input = input("Age: ").strip()
            if not age_input:
                print("Age cannot be empty!")
                continue
            
            try:
                age = int(age_input)
                if age > 0 and age < 150:
                    break
                else:
                    print("Please enter a valid age (1-149)")
            except ValueError:
                print("Age must be a number!")
        
        # Format the data string for processing
        raw_data = f"ID: {student_id} | Name: {name} | Email: {email} | Age: {age}"
        students_raw.append(raw_data)
        
        print(f"\n✓ Student data recorded: {name} ({student_id})")
        
        # Ask if student is a scholar
        is_scholar = input("\nIs this student a scholar? (y/n): ").strip().lower()
        if is_scholar == 'y':
            scholarship_type = input("Enter scholarship type (Academic/Athletic/etc.): ").strip()
            if scholarship_type:
                scholarship_info[student_id] = scholarship_type
                print(f"✓ Scholarship recorded: {scholarship_type}")
        
        # Ask if user wants to add another student
        print()
        continue_input = input("Add another student? (y/n): ").strip().lower()
        if continue_input != 'y':
            break
    
    return students_raw, scholarship_info


def main():    
    # ========================================================================
    # USER INPUT SECTION
    # ========================================================================
    students_raw, scholarship_info = get_user_input()
    
    if not students_raw:
        print("\nNo student data entered. Exiting program.")
        return
    
    # ========================================================================
    # PROCESS AND DISPLAY STUDENTS
    # ========================================================================
    print("\n" + "=" * 60)
    print("PROCESSING STUDENT DATA")
    print("-" * 60)
    
    # Process all students using regex extraction and validation
    all_students = process_student_data(students_raw, scholarship_info)
    
    if not all_students:
        print("\nNo valid students to display.")
        return
    
    print(f"\nSuccessfully processed {len(all_students)} student(s)")
    
    # Display all student information
    print("\n" + "=" * 60)
    print("STUDENT RECORDS")
    print("=" * 60)
    print()
    
    display_all_students(all_students)
    
    print("=" * 60)
    print("SYSTEM COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
