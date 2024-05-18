# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   JP,13MAT24,Created Script
#   JP,16MAY24,Added Exception
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''
csv_data: str = ''
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

#create a dictionary
'''
This portion is to create a json file, assuming that there has not been a file that
has not been created or a defined pathway. >>>>
'''
import json

try:
    file = open(FILE_NAME, "r")
    student_table = json.load(file)
    for item in students:
        print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, Course: {item['Course']}")
except FileNotFoundError as e:
    print("JSON file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
try:
    print("Prof. Justin will create a JSON for you..")
    student_row1: dict = {"FirstName": "First Name", "LastName": "Last Name", "Course": "Course"}
    student_table: list = [student_row1]
    file = open("Enrollments.json", "w")
    json.dump(student_table, file)
    file.close()
finally:
    print("JSON successfully created")


'''
<<<< This portion is to create a json file, assuming that there has not been a file that
has not been created or a defined pathway. 
'''

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            # Check that the input does not include numbers
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            
        finally:
            course_name = input("Please enter the name of the course: ")
            csv_data += f"{student_first_name},{student_last_name},{course_name}\n"
            student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "Course": course_name}
        student_table.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        print("\nCurrent registered students:")
        print(csv_data)
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(student_table, file)
        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        else:
            file.close()
            print("The following data was saved to file!")
            # try to read data from json
        finally:
            file = open(FILE_NAME, "r")
            student_table = json.load(file)
            for item in student_table:
                print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, Course: {item['Course']}")
            file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
