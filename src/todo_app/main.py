from tasks import add_task, list_tasks, mark_task_done # type: ignore

def main():
    while True:
        print("\nTodo App")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Done")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as done: "))
            mark_task_done(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main()
    