    cont_book={'sam':'8589923412'}
    ch=1
    while(ch<6):
        print(" 1.Add Contact \n 2.Delete Contact \n 3.Edit contact \n 4.Search Contact \n 5.List Contact \n 6.Exit \n")
        ch = int(input("Enter your choice: "))
        if ch==1:
            name=input("Enter the name: ")
            ph=input("Enter phone number: ")
            cont_book[name]=ph
            print("Contact added successfully! ")
        elif ch==2:
            d_key=input("Enter the contact to be deleted: ")
            if d_key not in cont_book:
                print("No such contact exist in the contact book!")
            else:
                cont_book.pop(d_key)
                print("Contact deleted successfully! ")
        elif ch==3:
            e_key=input("Enter the contact to be edited: ")
            if e_key not in cont_book:
                print("No such contact exist in the contact book!")
            else:
                e_ph=input("Enter the new contact number: ")
                cont_book.update({e_key:e_ph})
                print("Contact Edited successfully! ")
        elif ch==4:
             s_key=input("Enter the contact to search: ")
             if s_key in cont_book:
                 print("The contact found: ",cont_book.get(s_key))
             else:
                 print("Contact not found!")
        elif ch==5:
             print("The contact book is")
             print()
             print("Name \t\t Number")
             for x,y in cont_book.items():
                print(x,"\t\t",y)
        else:

            if ch==6:
                continue
            print("Invalid input")



