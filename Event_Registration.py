registration = []
reg_id = 1


def event_registration():
    global reg_id
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    event = input("Enter Event Name: ")

    record = {
        "id": reg_id,
        "name": name,
        "email": email,
        "event": event
    }

    registration.append(record)
    print("Registration Successful. ID:", reg_id)
    reg_id += 1
    print()


def cancel_registration():
    rid = int(input("Enter Registration ID to cancel: "))

    for r in registration:
        if r["id"] == rid:
            registration.remove(r)
            print("Registration Cancelled\n")
            return

        print("Record Not Found\n")


def display_record():
    if not registration:
        print("No registration found.\n")
        return

    print("\n---Event Registration---")
    for r in registration:
        print("ID:", r["id"], "Name :", r["name"], "Email :", r["email"], "Event :", r["event"])
        print()

    while True:
        print("=====Event Registration System=====")
        print("1 Event Registration\n")
        print("2 Cancel Registration\n")
        print("3 Display Record\n")
        print("4 Exit\n")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            event_registration()
        elif choice == "2":
            cancel_registration()
        elif choice == "3":
            display_record()
        elif choice == "4":
            print("Thank You")
            break
        else:
            print("Invalid Choice\n")
