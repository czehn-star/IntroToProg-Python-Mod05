# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   CZehner, 11/1/25, Modified script
# ------------------------------------------------------------------------------------------ #

#Import libraries
import simplejson as json
import _io

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
csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
file = _io.TextIOWrapper  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print("File must exist before running this script.") #check for the file and data preexisting
    print("Technical error message:")
    print(e, e.__doc__, type(e), sep='\n')
    file = open(FILE_NAME, 'w') # Creates the file if it didn't exist
    file.write(json.dumps(students, indent=4)) # Creates the format for a list in the json file
    file.close()
except Exception as e:
    print("There was a non specific error")
    print("Techincal error message:")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    print("Closing file")
    file.close()

while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        try:
            # Input the data
            student_first_name = input("Enter the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name must contain only letters.")

            student_last_name = input("Enter the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name must contain only letters.")

            course_name = input("Enter the course's name? ")

            student_data = {'FirstName': student_first_name, 'LastName': student_last_name, 'CourseName': course_name}
            students.append(student_data)
            print(f'{student_data["FirstName"]} {student_data["LastName"]} is registered for '
                  f'{student_data["CourseName"]}.')

        #Exceptions print outs
        except ValueError as e:
            print(e)
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

        #Display current student data
    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f"{student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        continue

    #Save the data to file.json
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, 'w')
            json.dump(students, file, indent=4)
            file.close()
            print("You have saved all the data to the file")
            continue
        except FileNotFoundError as e:
            print("File not found.")
            print("Technical error message:")
            print(e, e.__doc__, type(e), sep='\n')

        except TypeError as e:
            print(e)
            print("Make sure the data is formatted for JSON ")
            print(e, e.__doc__, type(e), sep='\n')

        except Exception as e:
            print("There was a non specific error")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                print("Closing file")
                file.close()
                print("Data saved successfully")
                continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program ended")






