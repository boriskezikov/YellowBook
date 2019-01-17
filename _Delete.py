"""__DELETE WINDOW__ """

try:
    import main
    import Additional_foo as foo
    import _Find
except ImportError as f:
    import datetime
    print("Import problem. Restart the app")
    error_log = open("C:\\Users\\Boris\\PycharmProjects\\lab1\\error_log.txt", 'a')
    error_log.write(str(datetime.datetime.now()))
    error_log.write(str(f))
    error_log.write('\n')
    error_log.close()
    exit()


def DelContactMenu():

    """ ___SQL REQUEST EXECUTION___"""

    request = input(
        "\nPlease choose the needed category and enter the value."
        "\n________________________________ "
        "\n1 - Delete by First name"
        "\n2 - Delete by Middle name "
        "\n3 - Delete by Last name"
        "\n4 - Delete by Age"
        "\n5 - Delete by Birth date "
        "\n6 - Delete by City"
        "\n7 - Delete by Country"
        "\n8 - Delete by Phone number"
        "\n9 - Delete all contacts"
        "\n10 - Delete by First name and Last name"
        "\n0 - Step back")

    if request in main.requestPool:
        user_input = input("Enter {} ".format(main.command_line.get(request))).strip().capitalize()
        print(user_input)

        main.cursor.execute("Select *"
                            " FROM Yellowbook "
                            "WHERE {0} = \"{1}\"".
                            format(main.command_line.get(request), user_input))
        if len(main.cursor.fetchall()) > 0:

            main.cursor.execute("DELETE FROM Yellowbook WHERE {0} = \"{1}\" ".
                                format(main.command_line.get(request), user_input))
            print("Successfully deleted")
        else:
            print("Such record(s) does not exist.")
            DelContactMenu()

    elif request == '0':
        foo.exit_continue("Go to the menu?")

    elif request == '9':
        main.cursor.execute("DELETE "
                            "FROM Yellowbook ")
        print("Successfully deleted")

    elif request == '10':
        user_input_surname = input("Enter {} ".format(main.command_line.get("1"))).strip().capitalize()
        user_input_name = input("Enter {} ".format(main.command_line.get("3"))).strip().capitalize()
        print(user_input_surname, user_input_name)
        main.cursor.execute("DELETE "
                            "FROM Yellowbook"
                            " WHERE {0} = \"{1}\" AND {2} = \"{3}\""
                            .format(main.command_line.get("1"), user_input_surname,
                                    main.command_line.get("3"), user_input_name))
    else:
        print("___________________________\nCommand is incorrect! Check if  the commands number is right. ")
        _Find.PrintInfoMenu()

    main.conn.commit()

    main.Mainmenu()









