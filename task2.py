record = []

def new_employee():

    data = []
    emp_id = input("Enter employee id:")
    name = input("Enter employee Name:")
    expirience = input("Enter Expirinece:")
    department = input("Enter employee department:")
    data.append(emp_id)
    data.append(name)
    data.append(int(expirience))
    data.append(department)
    record.append(data)  # Appending data to record array
    print(record)
    print("--------------------------")
    print("Student Data Inserted successfully")
    print("--------------------------")
    return


def display_employee():

    j=1
    for item in record:
        for x in item:

             print(j," ",x)

        j+=1

def update_employee():  # function to update student data
    upd_index = int(input("Enter index(From 0) to update data :"))
    if upd_index <= len(record) :
        new_id = input("Enter new employee id:")
        new_name = input("Enter new name:")
        new_exp = input("Enter new expirince:")
        new_dept =  input("Enter new departments:")
        record[int(upd_index)][0] = new_id  # Overwriting existing value
        record[int(upd_index)][1] = new_name
        record[int(upd_index)][2] = new_exp
        record[int(upd_index)][3] = new_dept
        print("----------------------")
        print("Student Data updated successfully")
        print("----------------------")


    else:
        print("invalid input")

def delete_employee():  # Function to delete student data
    del_index = input("Enter index(From 0) to Delete student record:")
    del record[int(del_index)]  # del method to remove element
    print("----------------------")
    print("Student Data Deleted successfully")
    print("----------------------")


while True:  # Displaying the option menu infinitely
    print("Enter 1 to create new employee Record")

    if len(record) >= 1:  # Validating the option whether student data exists or not
        print("Enter 2 to Update a employee record")

    if len(record) >= 1:
        print("Enter 3 to Delete a employee record")

    if len(record) >= 1:
        print("Enter 4 to Display employee records")


    inp = input("Enter your choice")

    if int(inp) == 1:
        new_employee()

    elif int(inp) == 2 and len(record) >= 1:
        update_employee()

    elif int(inp) == 3 and len(record) >= 1:
        delete_employee()

    elif int(inp) == 4 and len(record) >= 1:
        display_employee()

    else:
        print("Invalid Choice, Try again!")
