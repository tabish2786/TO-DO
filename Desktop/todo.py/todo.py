todo = []

while True:
    print("|| TODO LIST ||")
    print("1. ADD NEW TASKS")
    print("2. VIEW ALL TASKS")
    print("3. REMOVE SOME TASKS")
    print("4. VIEW COMPLETED TASKS")
    print("5. EXIT")
    Z = input("CHOOSE ANY OF THE OPTION:")

    if Z == "1":
        T = input("ENTER THE NEW TASK")
        if T != "":
            todo.append(T)
            print("TASK ADDED")
        else:
            print("TASK CAN'T BE ADDED")