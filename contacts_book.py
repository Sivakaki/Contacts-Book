# ------------------------------ Contact Book Program ------------------------------
# This program allows users to:
# 1. Add contacts (Name, Phone, Email)
# 2. View all saved contacts
# 3. Search for a contact by name
# 4. Delete a contact by name
# Data is stored in a file called "contacts.txt" in CSV format (name,phone,email)
# -----------------------------------------------------------------------------------


def add_contact():
    """Adds a new contact to the contacts.txt file"""

    # Taking user input for contact details
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    # Opening the file in append mode to add contact
    with open("contacts.txt", 'a') as file:
        file.write(f"{name},{phone},{email}\n")  # Writing in CSV format
    print("Contact saved successfully.")


def view_contacts():
    """Displays all contacts saved in contacts.txt"""

    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()  # Read all lines

            # Check if the file is empty
            if not contacts:
                print("No contacts found.")
            else:
                print("\n--- All Contacts ---")
                for contact in contacts:
                    # Splitting the stored line into respective values
                    name, phone, email = contact.strip().split(",")
                    print(f"Name: {name} | Phone: {phone} | Email: {email}")

    except FileNotFoundError:
        print("Contacts file not found. Please add a contact first.")


def search_contact():
    """Searches for a contact by name"""

    name_to_search = input("Enter name to search: ").lower()
    found = False  # Flag to check if the contact is found

    try:
        with open("contacts.txt", "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")
                # Comparing lowercase for case-insensitive comparison
                if name.lower() == name_to_search:
                    found = True
                    print(f"Found -> Name: {name} | Phone: {phone} | Email: {email}")

        # If no match found
        if not found:
            print("Contact not found.")

    except FileNotFoundError:
        print("Contacts file not found. Please add a contact first.")


def delete_contact():
    """Deletes a contact by name"""

    name_to_delete = input("Enter name to delete: ").lower()
    updated_contacts = []  # List to store remaining contacts
    deleted = False  # Flag to check if deletion occurred

    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                # If name doesn't match, keep the contact
                if name.lower() != name_to_delete:
                    updated_contacts.append(contact)
                else:
                    deleted = True  # Mark that deletion occurred

        # Rewrite the file without deleted contact
        with open("contacts.txt", "w") as file:
            file.writelines(updated_contacts)

        # Show final message
        if deleted:
            print("Contact successfully deleted!")
        else:
            print("Contact not found.")

    except FileNotFoundError:
        print("Contacts file not found. Please add a contact first.")


def main():
    """Main function to run the Contact Book application"""
    while True:
        # Menu options for the user
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        # Taking user's choice
        choice = input("Enter your choice: ")

        # Calling respective functions based on user choice
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter a number between 1 to 5.")


# Entry point of the program
if __name__ == "__main__":
    main()
