class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\nEnter contact details:")
        name = input("Name: ")
        phone = input("Phone number: ")
        email = input("Email: ")
        address = input("Address: ")
        
        new_contact = {"name": name, "phone": phone, "email": email, "address": address}
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
        else:
            print("\nContacts List:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def search_contact(self):
        search_term = input("\nEnter name or phone number to search: ")
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                search_results.append(contact)
        if search_results:
            print(f"\nSearch Results for '{search_term}':")
            for result in search_results:
                print(f"Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}, Address: {result['address']}")
        else:
            print(f"No contacts found matching '{search_term}'.")

    def update_contact(self):
        name = input("\nEnter name of contact to update: ")
        found = False
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                found = True
                print("\nUpdate contact details (leave blank to keep unchanged):")
                phone = input(f"Current Phone: {contact['phone']}, New Phone: ")
                email = input(f"Current Email: {contact['email']}, New Email: ")
                address = input(f"Current Address: {contact['address']}, New Address: ")
                
                if phone:
                    contact['phone'] = phone
                if email:
                    contact['email'] = email
                if address:
                    contact['address'] = address
                
                print(f"Contact '{name}' updated successfully.")
                break
        
        if not found:
            print(f"Contact '{name}' not found.")

    def delete_contact(self):
        name = input("\nEnter name of contact to delete: ")
        found = False
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                found = True
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                break
        
        if not found:
            print(f"Contact '{name}' not found.")

    def main_menu(self):
        while True:
            print("\n1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            
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
                print("Exiting Contact Management System.")
                break
            
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

# Instantiate the ContactManager class and start the program
if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.main_menu()
