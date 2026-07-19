#student management

class Student:
    def __init__(self,name,age,major):
        self.name = name
        self.age = age
        self.major = major
        self.is_attendance = True

    
    def show_info(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"major : {self.major}")

        if self.is_attendance == True:
            print("this student is attend the class")
        else:
            print("this student didn't attend the class")

    def absent(self):
        self.is_attendance = False

    def present(self):
        self.is_attendance = True



students = []

#program
print("===== Student Management =====")
print("1. Add Student")
print("2. Show Students")
print("3. Search Student")
print("4. Make Student Absent")
print("5. Make Student Present")
print("6. Exit")
print()

while True:
    print()
    choice = input("type the number to access the program: ")
    print()
    if choice == "1":
       print("======= Add Student Program =======")
       print()
       name = input("enter your name: ").lower()
       age = int(input("enter your age: "))
       major = input("enter your major: ").lower()
       student = Student(name,age,major)
       students.append(student)
       print("student added successfully")

    elif choice == "2":
       print("showing the student")
       if not students:
           print("there is no student in the list")
       else:
             for i in students:
                i.show_info()
                print()

    elif choice == "3":
          print("======= Search Student Program =======")

          if not students:
               print("There are no students in the list.")

          else:
             search = input("Enter the student name: ").lower()

             found = False

             for i in students:
                  if search == i.name.lower():
                     print("\nStudent Found!")
                     i.show_info()
                     found = True
                  break

             if not found:
                print("Student was not found.")

    elif choice == "4":
        print("===== Absent Program =====")

        if not students:
              print("There are no students in the list.")

        else:
             search = input("Enter student name: ")

        found = False

        for i in students:
            if search.lower() == i.name.lower():
                i.absent()
                print("Attendance updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")
        
    elif choice == "5":
             print("===== Present Program =====")

             if not students:
                print("There are no students in the list.")

             else:
                   search = input("Enter student name: ")

             found = False

             for i in students:
                 if search.lower() == i.name.lower():
                    i.present()
                    print("Attendance updated successfully!")
                    found = True
                    break

             if not found:
                 print("Student not found.")

    elif choice == "6":
        print("thank you for using the program")
        break
        
        

        
          

    