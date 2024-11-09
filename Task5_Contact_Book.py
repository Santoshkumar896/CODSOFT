import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @staticmethod
    def from_dict(data):
        return Contact(data["name"], data["phone"], data["email"], data["address"])

    def display_contact(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}\n")


class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.contacts = {}
        self.filename = filename
        self.load_contacts()

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        if name in self.contacts:
            print("This contact already exists.")
        else:
            self.contacts[name] = Contact(name, phone, email, address)
            print("Contact added successfully.")
            self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
            return
        print("\nContact List:")
        for contact in self.contacts.values():
            print(f"{contact.name} - {contact.phone}")

    def search_contact(self):
        query = input("Enter the name or phone number to search: ")
        found = False
        for contact in self.contacts.values():
            if contact.name == query or contact.phone == query:
                contact.display_contact()
                found = True
        if not found:
            print("No contact found with that name or phone number.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        contact = self.contacts.get(name)
        if contact:
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact.phone = phone or contact.phone
            contact.email = email or contact.email
            contact.address = address or contact.address
            print("Contact updated successfully.")
            self.save_contacts()
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
            self.save_contacts()
        else:
            print("Contact not found.")

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump({name: contact.to_dict() for name, contact in self.contacts.items()}, file)
        print("Contacts saved to file.")

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.contacts = {name: Contact.from_dict(details) for name, details in data.items()}
            print("Contacts loaded from file.")
        except FileNotFoundError:
            print("No saved contacts found.")

    def main_menu(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the Contact Manager
contact_manager = ContactManager()
contact_manager.main_menu()
