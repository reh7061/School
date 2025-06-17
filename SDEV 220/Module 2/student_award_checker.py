# Author: Pa Reh
# File Name: student_award_checker.py
# Description: This app accepts student names and GPAs to check if they
#              qualify for the Dean's List (GPA >= 3.5) or the
#              Honor Roll (GPA >= 3.25). Processing stops when sentinel 'ZZZ'
#              is entered for the last name.

print("Student Honors Checker")
print("To quit at any time, enter 'ZZZ' as the last name.\n")

# Priming input: get the first last name before the loop
last_name_input = input("Enter student's last name (or 'ZZZ' to quit): ").strip()

# Loop until the sentinel is entered
while last_name_input != "ZZZ":
    # Capitalize the last name for formatting
    last_name = last_name_input.capitalize()

    # Get the first name and GPA for the current student
    first_name = input("Enter student's first name: ").capitalize().strip()
    gpa = float(input("Enter student's GPA (0.0-4.0): "))

    # Output the results based on GPA
    print(f"\n--- Checking results for {first_name} {last_name} ---")
    if gpa >= 3.5:  # Dean's List criteria
        print(f"{first_name} {last_name} made the Dean's List.")
    elif gpa >= 3.25:   # Honor Roll criteria
        print(f"{first_name} {last_name} made the Honor Roll.")
    else:   # Neither criteria met
        print(f"{first_name} {last_name} did not make the Dean's List or Honor Roll.")

    # Read the next last name (sentinel check)
    last_name_input = input("Enter student's last name (or 'ZZZ' to quit): ").strip()

# End of the program
print("End of student processing.")