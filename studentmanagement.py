FILENAME = "students.txt"

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")
    
    with open(FILENAME, 'a') as file:
        file.write(f"{name},{roll},{branch}\n")
    
    print("Student record added successfully!")

# Function to view all students
def view_students():
    try:
        with open(FILENAME, 'r') as file:
            records = file.readlines()
            if records:
                print("\n--- Student Records ---")
                for i, record in enumerate(records, 1):
                    name, roll, branch = record.strip().split(',')
                    print(f"{i}. Name: {name}, Roll No: {roll}, Branch: {branch}")
            else:
                print("No student records found.")
    except FileNotFoundError:
        print("No student records found yet.")

# Function to search a student by roll number
def search_student():
    roll_search = input("Enter roll number to search: ")
    found = False
    try:
        with open(FILENAME, 'r') as file:
            for record in file:
                name, roll, branch = record.strip().split(',')
                if roll == roll_search:
                    print(f"Found: Name: {name}, Roll No: {roll}, Branch: {branch}")
                    found = True
                    break
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")

# Function to update student data by roll number
def update_student():
    roll_update = input("Enter roll number to update: ")
    updated = False
    try:
        with open(FILENAME, 'r') as file:
            records = file.readlines()
        
        with open(FILENAME, 'w') as file:
            for record in records:
                name, roll, branch = record.strip().split(',')
                if roll == roll_update:
                    print(f"Updating record for {name} (Roll: {roll})")
                    name = input("Enter new name: ")
                    branch = input("Enter new branch: ")
                    file.write(f"{name},{roll},{branch}\n")
                    updated = True
                else:
                    file.write(record)
        
        if updated:
            print("Student record updated.")
        else:
            print("Roll number not found.")
    except FileNotFoundError:
        print("No student records found.")

# Function to delete a student by roll number
def delete_student():
    roll_delete = input("Enter roll number to delete: ")
    deleted = False
    try:
        with open(FILENAME, 'r') as file:
            records = file.readlines()
        
        with open(FILENAME, 'w') as file:
            for record in records:
                name, roll, branch = record.strip().split(',')
                if roll == roll_delete:
                    deleted = True
                    continue  # Skip writing this record
                file.write(record)
        
        if deleted:
            print("Student record deleted.")
        else:
            print("Roll number not found.")
    except FileNotFoundError:
        print("No student records found.")

# Main program loop
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the main function
if __name__ == "__main__":
    main()
