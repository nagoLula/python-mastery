def write_note():
    note = input("Write a note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved!")


def read_notes():
    print("\nYour saved notes:")

    try:
        with open("notes.txt", "r") as file:
            for line in file:
                print("- " + line.strip())
    except FileNotFoundError:
        print("No notes found yet.")


def main():
    while True:
        print("\n1. Write a note")
        print("2. Read notes")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            write_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
