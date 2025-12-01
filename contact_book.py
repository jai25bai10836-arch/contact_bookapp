def add_contact(contacts):
    """Adds a new contact to the contact book."""
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address (optional): ").strip()
    
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    """Displays all contacts in the contact book."""
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\n--- Contact Book ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        print("--------------------")

def search_contact(contacts):
    """Searches for a contact by name."""
    name = input("Enter name to search: ").strip()
    if name in contacts:
        details = contacts[name]
        print(f"\nFound Contact:")
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    """Deletes a contact by name."""
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    """The main function to run the contact book application."""
    contacts = {}
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
