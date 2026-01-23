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
        T = input("ENTER THE NEW TASK:")
        if T != "":
            todo.append(T)
            print("TASK ADDED")
        else:
            print("TASK CAN'T BE ADDED")
    elif Z == "2":
        if len(todo) == 0:
            print("NO TASKS AVAILABLE")
        else:
            print("YOUR TASKS:")
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])
