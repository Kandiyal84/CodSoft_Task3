contact = {}


def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))
while True:
    choice = int(input(" 1. Add new contact \n 2. View contact \n 3. Search Contact \n 4. Update contact \n"
                       " 5. Delete contact \n 6. Exit \n Enter Your Choice :  "))
    if choice == 1:
        Name = input(" Enter the contact name :  ")
        Phone = input(" Enter the Mobile number :  ")
        print(" contact added ")
        contact[Name] = Phone

    elif choice == 2:
        if not contact:
            print(" Empty Contact Book. ")
        else:
            display_contact()

    elif choice == 3:
        search_name = input(" Enter the contact name :  ")
        if search_name in contact:
            print(search_name, ":", contact[search_name])
        else:
            print(" No result found ")

    elif choice == 4:
        edit_contact = input(" Enter the contact name to be updated :  ")
        if edit_contact in contact:
            phone = input(" Enter mobile number :  ")
            contact[edit_contact] = phone
            print(" Contact updated ")
            display_contact()
        else:
            print(" No result found ")

    elif choice == 5:
        del_contact = input(" Enter the Contact to be deleted :  ")
        if del_contact in contact:
            confirm = input(" Do you want to delete this contact yes/no? ")
            if confirm == 'yes' or confirm == 'Yes':
                contact.pop(del_contact)
            display_contact()
        else:
            print(" No result found ")

    else:
        break