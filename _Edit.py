import main
import datetime
import sys

try:
    import Additional_foo as foo
    import _Addnew
    import _Find
except ImportError as f:
    error_log = open("C:\\Users\\Boris\\PycharmProjects\\lab1\\error_log.txt", 'a')
    error_log.write(str(datetime.datetime.now()))
    error_log.write(str(f))
    error_log.write('\n')
    print("Import problem. Restart the app")
    error_log.close()
    sys.exit()

def EditMenu(fname, sname):
    request = input(
        "\nPlease choose the needed category and enter the value."
        "\n________________________________ "
        "\n1 - Edit First name"
        "\n2 - Edit Middle name "
        "\n3 - Edit Last name"
        "\n4 - Edit Age"
        "\n5 - Edit Birth date "
        "\n6 - Edit City"
        "\n7 - Edit Country"
        "\n8 - Edit Phone number"
        "\n9 - Edit all"
        "\n0 - Step back")

    if request in main.command_line or request == '9' or request == '0':

        user_value = input("Enter the value. For Date, Age and Phone number press Enter: ")

        #  The next code string checks if user_input is not a string of whitespaces.
        #if foo.whitespace_extract(user_value) == 1:

        if request in main.requestPool[0:2] or request in main.requestPool[5:6]:
            value = []  # A stub for isalnum function which 2 argument is a list.
            foo.isalnum(user_value, value)
            main.cursor.execute("UPDATE Yellowbook "
                                "SET {0} = \"{1}\" "
                                "WHERE [First name] = \"{2}\" "
                                "AND [Last name] = \"{3}\"".
                                    format(main.command_line.get(request), value[0], fname, sname))

            main.conn.commit()

        elif request == '4':
            age = input("Age: ")

            while (not age.isdigit()) or (not 0 <= int(age) < 150):
                age = input(
                    "\nThis age is incorrect! Please make sure that "
                    "\nyour input consists of digits only and the age is correct! "
                    "\n( 12 - correct, '-1' - incorrect, 151 - incorrect) ")
            main.cursor.execute("UPDATE Yellowbook"
                                " SET {0} = \"{1}\" "
                                "WHERE [First name] = \"{2}\""
                                "AND [Last name] = \"{3}\"".
                                format(main.command_line.get(request), user_value, fname, sname))

        elif request == '5':

            while True:

                try:
                    date_text = datetime.date(int(input("Birth date Year:")), int(input("Birth date Month:")),
                                              int(input("Birth date Day:")))
                    datetime.datetime.strptime(str(date_text), '%Y-%m-%d')
                    main.cursor.execute("UPDATE Yellowbook "
                                        "SET {0} = \"{1}\""
                                        " WHERE [First name] = \"{2}\" "
                                        "AND [Last name] = \"{3}\"".
                                        format(main.command_line.get(request), user_value, fname, sname))
                    print("Successfully")
                    break

                except BaseException:
                    print("Incorrect data format, should be YYYY-MM-DD")

        elif request == '8':
            phone = input("Input phone number  without '8' :\r")

            while (len(phone) != 10) or (phone.isdigit() is not True) or (phone[0] == 8):
                phone = input("Try again! Input phone number  without '8' : ")
            main.cursor.execute("UPDATE Yellowbook "
                                "SET {0} = \"{1}\" "
                                "WHERE [First name] = \"{2}\""
                                "AND [Last name] = \"{3}\"".
                                format(main.command_line.get(request), user_value, fname, sname))

        elif request == '9':
            main.cursor.execute("DELETE "
                                "FROM Yellowbook "
                                "WHERE [First name] = \"{2}\""
                                "AND [Last name] = \"{3}\"".
                                format(main.command_line.get(request), user_value, fname, sname))
            _Addnew.AddContactMenu()

        elif request == '0':
            _Find.PrintInfoMenu()




