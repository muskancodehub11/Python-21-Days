
students = []
student = {
        "name": "Musk",
        "roll": 41,
        "marks": 90
}
students.append(student)




def add_student():
    name = input("Enter student name : ")
    roll = int(input("Enter student roll number : "))
    marks = int(input("Enter student marks : "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")



def view_student():

    if len(students) == 0:
        print("No students found.")
        return

    print("\n------ Student List ------")

    for s in students:
        print(f"Name  : {s['name']}")
        print(f"Roll  : {s['roll']}")
        print(f"Marks : {s['marks']}")
        


def update_student():

    roll = int(input("Enter roll number to update: "))

    for s in students:

        if s["roll"] == roll:

            s["name"] = input("Enter new name: ")
            s["marks"] = int(input("Enter new marks: "))

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():

    roll = int(input("Enter roll number to delete: "))

    for s in students:

        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def menu():
    print("====== Student Management System ======")
    print("1. Add student")
    print("2. View student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")



while True:
    menu()
    choice = int(input("Enter your choice : "))

    if choice == 1:
       add_student()
    elif choice == 2:
       view_student()
    elif choice == 3:
       update_student()
    elif choice == 4:
       delete_student()
    elif choice == 5:
       break
    else:
       print("Invalid choice. Please try again.")
