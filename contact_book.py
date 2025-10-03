contacts = []  # list but will hold only ONE contact

def add_contact():
  name = input("Enter name: ")
  phone = input("Enter phone: ")
  email = input("Enter email:")
  contacts.append({"name": name, "phone": phone, "email": email})
  print("Contact saved!")

def view_contact():
    if not contacts:
        print("No contact saved yet.")
    else:
        print("\n--- Contact ---")
        print(f"Name: {contacts[0]['name']}")
        print(f"Phone: {contacts[0]['phone']}")
        print(f"Email: {contacts[0]['email']}")
        print("----------------")

def exit_app():
    print("Goodbye!")
    exit()

# ----------------------
# MAIN PROGRAM LOOP
# ----------------------
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        exit_app()
    else:
        print("Invalid choice. Try again.")


  