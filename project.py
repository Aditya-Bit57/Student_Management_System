students = []

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        data = {
            "Name": name,
            "Age": age
        }

        students.append(data)
        print("Student Added Successfully")

    elif choice == "2":
        for s in students:
            print(s)

    elif choice == "3":
        search = input("Enter name: ")

        for s in students:
            if s["Name"] == search:
                print(s)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")