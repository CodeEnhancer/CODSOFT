contacts={}
def add_contact():
  name=input("Enter name: ")
  phone=input("Enter phone number: ")
  if name in contacts:
    print("This contact already exists.")
  else:
    contacts[name]= phone
    print("contact added successfully")

def delete_contact():
    name=input("Enter the name:")
    if name in contacts:
            del contacts[name]
            print("Contact deleted Successfully")
    else:
            print("The contact does not exist")
        
def update_contact():
    name=input("Enter the name: ")
    for contact in contacts:
        if(contact==name):
            phone=int(input("Enter the new phone number "))
            contacts[name]=phone
            print("Contact Updated")
            break
        else:
            print("This Contact does not exist ")
                
def search_contact():
    name=input("Enter the name : ")
    for contact in contacts:
        if(contact.lower() == name.lower()):
            print("contact is found")
            print(contact,contacts[name])
def display_contacts():
    if contacts=={}:
        print("There are no contacts")
    else:
        print("contacts list:")
    for name,phone in contacts.items():
        print(name,phone)

while True:
    print("Contact Book Menu:")
    print("1.Add Contact")
    print("2.Delete Contact")
    print("3.Update Contact")
    print("4.Search Contact")
    print("5.Display Contacts")
    print("6.Exit")               

    choice=int(input("Enter your choice (1-6): "))
    if (choice==1):
        add_contact()

    elif choice==2:
        delete_contact()

    elif(choice==3):
        update_contact()

    elif(choice==4):
        search_contact()

    elif(choice==5):
        display_contacts()

    elif(choice==6):
        print("Exiting Contact book,Goodbye!")
        break
    else:
        print("Invalid choice,please enter a number between 1-6")

    


 
