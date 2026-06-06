tasks = []
   
while True:
    print("\n1. Add task")
    print("2. view tasks")
    print("3. exit")

    choice = input("enter your choice:")

    if choice == "1":
        task = input("enter task:")
        tasks.append(task)
        print("Task added!")

    elif choice =="2":
            print("\nTo-Do-List:")
            for i,task in enumerate(tasks,1):
                print(f"{i}. {task}")
    elif choice =="3":
            print("Goodbye!")
            break
    else:
            print("invalid choice!")