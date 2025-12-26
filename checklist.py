import os

def clear_screen():
    # Clears the terminal screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def show_checklist(tasks):
    print("\n--- YOUR CHECKLIST ---")
    if not tasks:
        print("Your list is empty!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[✓]" if task['done'] else "[ ]"
            print(f"{i}. {status} {task['name']}")
    print("----------------------\n")

def main():
    tasks = []
    
    while True:
        clear_screen()
        show_checklist(tasks)
        
        print("Commands: [a] Add | [c] Check/Uncheck | [d] Delete | [q] Quit")
        choice = input("Choose an option: ").lower()

        if choice == 'a':
            name = input("Enter task name: ")
            if name:
                tasks.append({"name": name, "done": False})
        
        elif choice == 'c':
            try:
                index = int(input("Task number to toggle: ")) - 1
                tasks[index]['done'] = not tasks[index]['done']
            except (ValueError, IndexError):
                input("Invalid number. Press Enter to continue...")

        elif choice == 'd':
            try:
                index = int(input("Task number to delete: ")) - 1
                tasks.pop(index)
            except (ValueError, IndexError):
                input("Invalid number. Press Enter to continue...")

        elif choice == 'q':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()