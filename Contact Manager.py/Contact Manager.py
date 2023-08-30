##اسامة محمد صالح الهرش

contacts = {}  # Dictionary to store contacts
## This function do added add_contact
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    
    print("Contact added successfully!")
## This function do search  search_contact
def search_contact():
    name = input("Enter the name to search: ")
    
    if name in contacts:
        contact = contacts[name]
        print("Name:", name)
        print("Phone:", contact['phone'])
        print("Email:", contact['email'])
    else:
        print("Contact not found!")
## This function do delete  delete_contact
def delete_contact():
    name = input("Enter the name to delete: ")
    
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
## This function do view  display_contacts
def display_contacts():
    if contacts:
        print("Contacts:")
        for name, contact in contacts.items():
            print("Name:", name)
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
    else:
        print("No contacts found.")
## This function do print operation  contact main
def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()