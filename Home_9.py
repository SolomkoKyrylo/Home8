
contacts = {}


def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone number: {phone}"


def change_phone(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} changed to: {new_phone}"
    else:
        return f"Contact {name} not found"


def get_phone(name):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found"


def show_all_contacts():
    if contacts:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "No contacts found"


def handle_command(command):
    parts = command.split()
    if len(parts) == 0:
        return "Enter a valid command"
    keyword = parts[0].lower()

    if keyword == "add":
        if len(parts) >= 3:
            name = parts[1]
            phone = " ".join(parts[2:])
            return add_contact(name, phone)
        else:
            return "Give me name and phone, e.g., 'add John Doe 123-456-7890'"

    elif keyword == "change":
        if len(parts) >= 3:
            name = parts[1]
            new_phone = " ".join(parts[2:])
            return change_phone(name, new_phone)
        else:
            return "Give me name and new phone, e.g., 'change John Doe 987-654-3210'"

    elif keyword == "phone":
        if len(parts) >= 2:
            name = parts[1]
            return get_phone(name)
        else:
            return "Enter a name to get the phone number, e.g., 'phone John Doe'"

    elif keyword == "show":
        if len(parts) >= 2 and parts[1].lower() == "all":
            return show_all_contacts()
        else:
            return "Unknown command. Use 'show all' to display all contacts."

    elif keyword == "good" or keyword == "close" or keyword == "exit":
        return "Good bye!"

    else:
        return "Unknown command"


def main():
    print("How can I help you?")
    while True:
        try:
            command = input("> ")
            result = handle_command(command)
            print(result)
            if result == "Good bye!":
                break
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
