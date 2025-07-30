def display_menu():
    print("\n CONTACT BOOK")
    print("1.Add contact")
    print("2.Delete contact")
    print("3.Update contact")
    print("4.Display contact")
    print("5.Search Contact")
    print("6.Exit")

contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")

def view_contact():
    if not contacts:
        print("Contact Not Found")
        return
    for name,info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("\n")
    
def delete_contact():
    name = input("Enter name of contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    del contacts[name]
    print("Contact deleted successfully.")


def update_contact():
    name = input("Enter the name to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email address: ").strip()
        contacts[name] = {"phone": phone, "email": email}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def search_contact():
    name = input("Enter name of contact to search: ").strip()
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")
    
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        view_contact()
    elif choice == '5':
        search_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")