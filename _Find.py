
"""___THIS MODULE INCLUDES SEARCHING WINDOW___"""
import os
import sys
try:
    import main
    import Additional_foo as foo
    import _Delete
    import _Addnew
    import _Edit
except ImportError as f:
    import datetime
    print("Import problem. Restart the app\n")
    error_log = open("C:\\Users\\Boris\\PycharmProjects\\lab1\\error_log.txt", 'a')
    error_log.write(str(datetime.datetime.now()))
    error_log.write(str(f))
    error_log.write('\n')
    error_log.close()
    sys.exit()


def PrintInfoMenu():
    """______________________SQL request__________________________"""

    request = input(
                    "\nPlease choose the needed category and enter the value."
                    "\n________________________________ "
                    "\n1 - Search by First name"
                    "\n2 - Search by Middle name "
                    "\n3 - Search by Last name"
                    "\n4 - Search by Age"
                    "\n5 - Search by Birth date "
                    "\n6 - Search by City"
                    "\n7 - Search by Country"
                    "\n8 - Search by Phone number"
                    "\n9 - Print all contacts"
                    "\n10 - Search by Name and Surname"
                    "\n0 - Step back\n")

    if request in main.requestPool:
        user_input = input("Enter {} in correct format. "
                           "\nFor phone: start with '8' "
                           "\nFor BIRTH DATE: you are to use the next data representation"
                           " <yyyy-mm-dd>\n "
                           .format(main.command_line.get(request))).lower().capitalize().strip()
        main.cursor.execute("SELECT * FROM Yellowbook WHERE {0} = \"{1}\" ".
                            format(main.command_line.get(request), user_input.strip()))
    elif request == '0':
        foo.exit_continue("Go to the menu?\n")

    elif request == '9':
        main.cursor.execute("SELECT * FROM Yellowbook ")

    elif request == '10':
        user_input_surname = input("Enter {} ".format(main.command_line.get("1"))).strip().lower().capitalize()
        user_input_name = input("Enter {} ".format(main.command_line.get("3"))).strip().lower().capitalize()
        print(user_input_surname, user_input_name)
        main.cursor.execute("SELECT * FROM Yellowbook WHERE {0} = \"{1}\" AND {2} = \"{3}\""
                            .format("[First name]", user_input_surname,
                                    "[Last name]", user_input_name))
    else:
        print("___________________________\nCommand is incorrect! Check if  the commands number is right.\n ")
        PrintInfoMenu()

    # Receives the result of the SQL request
    result = main.cursor.fetchall()

    """
     >> VERIFIES IF RESULT EXISTS IN CURRENT TABLE.
    """

    if len(result) == 0:
        user_input = input("This record does not exist yet.\n "
                           "Would you like to create a new record (1) or find another(2)."
                           "\nEnter 1 or 2 or any to exit.\r")
        if user_input == '1':
            _Addnew.AddContactMenu()
        elif user_input == '2'  :
            PrintInfoMenu()
        else:
            main.Mainmenu()

    for i in result:
        print(i)

    user_input = input("\n-- Window -- "
                           "\n1 - Edit"
                           "\n2 - Delete"
                           "\n3 - Menu"
                           "\nAnother - to Exit\n")

    """_____________________________Next menu window__________________________________"""

    if user_input == '1':
        # If result includes more attachments than 1, user need to choose the one only.
        if len(result) > 1:
            for i in result:
                print(i)
            while True:
                first_name = input("Enter the first name of editing contact")
                last_name = input("Enter the last name of editing contact")
                check_list = [x for x in first_name if x not in foo.symbols]
                if (len(check_list) == len(first_name)) and (len(first_name) > 0):
                    check_list = [x for x in last_name if x not in foo.symbols]
                    if len(check_list) == len(last_name):
                        last_name = last_name.lower().capitalize()
                        first_name = first_name.lower().capitalize()
                        break
                    else:
                        print("Your input was incorrect! This field should consist of letters and digits:\r")

                else:
                    print("Your input was incorrect! This field should consist of letters and digits:\r")

            main.cursor.execute("SELECT * FROM Yellowbook WHERE {0} = \"{1}\" AND {2} = \"{3}\"".
                                format("[First name]", first_name, "[Last name]", last_name))
            result = main.cursor.fetchall()
            if len(result) == 0:
                print("Such record does not exist.")
                PrintInfoMenu()
        print(result[0][0], ' ', result[0][2])

        # We call result[0][0] as result returned by cursor.fetchall.
        # Fetchall returns a list of tuples.
        # So we need to penetrate the structure consistently to get the needed value.

        _Edit.EditMenu(result[0][0], result[0][2])


    elif user_input == '2':
        _Delete.DelContactMenu()

    elif user_input == '3':
        main.Mainmenu()

    else:
        main.Mainmenu()
    foo.exit_continue("Return to the main menu?")


