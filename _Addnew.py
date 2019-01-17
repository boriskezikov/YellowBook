
import sqlite3
import datetime
try:
    import Additional_foo as foo
    import main
    import sys
except ImportError as f:
    error_log = open("C:\\Users\\Boris\\PycharmProjects\\lab1\\error_log.txt", 'a')
    error_log.write(str(datetime.datetime.now()))
    error_log.write(str(f))
    error_log.write('\n')
    print("Import problem. Restart the app")
    error_log.close()
    sys.exit()

DATA = "Yellowbook"  # data base name


def AddContactMenu():

    """____________________________________DATA INPUT AND CORRECTNESS CHECK__________________________________________"""

    print("Now lets add new person.You should write down: First name, Middle name.. ")
    data = []  # LIST stores all INSERT information

    surname = input("First name: ")
    foo.isalnum(surname, data)  # Checks if filled data is correct ( If True returns, Else provides another try)

    middle_name = input("Middle name: ")
    foo.isalnum(middle_name, data)  # Correctness check

    name = input("Second name: ")
    foo.isalnum(name, data)

    age = input("Age: ")

    while (not age.isdigit()) or (not 0 <= int(age) < 150):
        age = input(
            "\nThis age is incorrect! Please make sure that "
            "\nyour input consists of digits only and the age is correct! "
            "\n( 12 - correct, '-1' - incorrect, 151 - incorrect) ")
    data.append(age)

    # Birth date column
    _ = input("Will you fill the birth date? If 'yes' press 'y'. If no press another.")
    if _ == 'y':
        while True:
            try:
                date_text = datetime.date(int(input("Birth date Year:")), int(input("Birth date Month:")),
                                          int(input("Birth date Day:")))
                datetime.datetime.strptime(str(date_text), '%Y-%m-%d')
                data.append(date_text)
                print("Successfully")
                break
            except BaseException:
                print("Incorrect data format, should be YYYY-MM-DD")
    else:
        data.append('-')

    phone = input("Phone number  without '8' : ")
    while (len(phone) != 10) or (phone.isdigit() is not True) or (phone[0] == 8):
        phone = input("Try again! Input phone number  without '8' : ")
    data.append('8'+phone)

    city = input("City: ")

    while not city.isalnum():
        city = input("City name can't include another symbols besides letters and digits! : ")
    data.append(city.lower().capitalize())

    country = input("Country: ")

    while not country.isalnum():
        country = input("Country name can't include another symbols besides letters and digits! : ")
    data.append(country.lower().capitalize())

    """_________________________________DATA BASE SQL COMMAND EXECUTION_____________________________________"""

    main.cursor.execute('SELECT EXISTS (SELECT [First name],[Last name]'
                        ' FROM {0} '
                        ' WHERE [First name] = "{1}" and [Last name] = "{2}")'.format(DATA, data[0], data[2]))

    flag = main.cursor.fetchone()  # fetchone returns a tuple with one element

    if flag[0] != 1:

        # UNIQUE ERROR HANDLING
        try:
            main.cursor.execute("INSERT"
                                " INTO Yellowbook "
                                "VALUES (?,?,?,?,?,?,?,?)", data)
        except sqlite3.IntegrityError as f:
            foo.errorLog(f)
            foo.exit_continue("Return to menu?\n")

    else:
        print(" \nThe Yellowbook does not support 2 or more records with similar [First name] and {Second name] fields."
              " \nFill in another Surname.\n ")
        foo.exit_continue("Menu?")

    main.conn.commit()  # Saves changes in data base

    foo.exit_continue("Return to menu?\n")  # Asks user for  the next step (exit program or not)
