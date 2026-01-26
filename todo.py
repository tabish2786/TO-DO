todo = []

while True:
    print("|| TODO LIST ||")
    print("1. ADD NEW TASKS")
    print("2. VIEW ALL TASKS")
    print("3. REMOVE SOME TASKS")
    print("4. EXIT")
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

    elif Z == "3":
        if len(todo) == 0:
            print("NO TASKS TO REMOVE")
        else:
            print("YOUR TASKS:")
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])

            R = int(input("ENTER TASK NUMBER TO REMOVE:"))
            if R > 0 and R <= len(todo):
                removed = todo.pop(R - 1)
                print("REMOVED TASK:", removed)
            else:
                print("INVALID TASK NUMBER")

    elif Z == "4":
        print("EXITING TODO APP")
        break

    else:
        print("INVALID OPTION, TRY AGAIN")