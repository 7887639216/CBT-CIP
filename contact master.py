class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactMaster:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email)
        self.contacts.append(new_contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} removed successfully.")
                return
        print(f"Contact {name} not found.")

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}")

def main():
    contact_master = ContactMaster()

    while True:
        print("\n1. Add a new contact")
        print("2. Remove an existing contact")
        print("3. Display all contacts")
        print("4. Exit contact master")

        choice = int(input("Please enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_master.add_contact(name, phone_number, email)
        elif choice == 2:
            name = input("Enter name of contact to remove: ")
            contact_master.remove_contact(name)
        elif choice == 3:
            contact_master.display_contacts()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
