from ForPython.util import println_colored,Color,display_loading_animation

contacts=[]


def addContact():
    print("==========================")
    name=input("Ismingizni kiriting: ")
    email=input("Elektron pochtangizni kiriting: ")
    phone=input("Telefoningizni kiriting: ")
    address=input("Manzilingizni kiriting: ")
    contacts.append({
        "name": name,
        "email": email,
        "phone": phone,
        "lastName":"Lastname",
        "address": address,
        "id": len(contacts)+1
    })
    println_colored("Kontakt qo'shildi!", Color.GREEN)

def getContactById(id):
    for contact in contacts:
        if contact["id"]==id:
            return contact
    return None
def EdidContact():
    print("==========================")
    for contact in contacts:
        print(f"ID: {contact['id']} | Name: {contact['name']} | Email: {contact['email']} | Phone: {contact['phone']} | Address: {contact['address']}")
    contactID=int(input("Enter contact ID: "))

    contact=getContactById(contactID)
    if contact:
        addres=input(f"Enter your address current({contact['address']}): ")
        contact["address"] = contact['address'] if len(addres)==0 else addres
        phone1=input(f"Enter your phone current({contact['phone']}): ")
        contact["phone"] = contact['phone'] if len(phone1)==0 else phone1
        name1=input(f"Enter your name current({contact['name']}): ")
        contact["name"] = contact['name'] if len(name1)==0 else name1
        email1=input(f"Enter your email current({contact['email']}): ")
        contact["email"] = contact['email'] if len(email1)==0 else email1
    else:
        print("Contact not found")


def deleteContact():
    print("==========================")
    for contact in contacts:
        print(f"ID: {contact['id']} | Name: {contact['name']} | Email: {contact['email']} | Phone: {contact['phone']} | Address: {contact['address']}")
    contactID=int(input("Enter contact ID: "))

    contact=getContactById(contactID)
    if contact:
        warning=input("Haqiqatan ham bu kontaktni oʻchirib tashlamoqchimisiz? y/n: ")
        if warning=="y":
            contacts.remove(contact)
        else:
            print("Action cancelled")
    else:
        print("Contact not found")


def searchContact():
    found=False
    quary=input("Enter contact name: ").lower()
    for contact in contacts:
        if   quary in contact["name"].lower():
            found=True
            print(f"ID: {contact['id']} | Name: {contact['name']} | Email: {contact['email']} | Phone: {contact['phone']} | Address: {contact['address']}")
    if not found:
     print("Contact not found")


def contactList():
    display_loading_animation("Contacts List uploading..",Color.GREEN)
    if len(contacts)!=0:
        for contact in contacts:
            print(
                f"ID:{contact['id']} {contact['name']} | {contact['email']} | {contact['phone']} | {contact['address']}")
    else:
        println_colored("No contacts found",Color.RED)


while True:
    print("1 ->  Add Contact")
    print("2 ->  Edit Contact")
    print("3 ->  Delete  Contact")
    print("4 ->  Search Contact")
    print("5 ->  List Contact")
    print("6 ->  Exit")
    choice = input("Enter your choice: ")
    if choice=="1":
        addContact()
    elif choice=="2":
        EdidContact()
    elif choice=="3":
        deleteContact()
    elif choice=="4":
        searchContact()
    elif choice=="5":
        contactList()
    elif choice=="6":
        warning=input("Chiqishga ishonchingiz komilmi? (y/n): ")
        if warning=="y":
            break
        else:
            print("Amal bekor qilindi")
    else:
        print("Yaroqsiz tanlov")

