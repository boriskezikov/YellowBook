
import sqlite3
import datetime
import sys
try:
    import _Addnew
    import _Find
    import _Delete
    import Additional_foo as foo
except ImportError as f:
    print("Import problem. Restart the app")
    error_log = open("C:\\Users\\Boris\\PycharmProjects\\lab1\\error_log.txt", 'a')
    error_log.write(str(datetime.datetime.now()))
    error_log.write(str(f))
    error_log.write('\n')
    error_log.close()
    sys.exit()


global conn


try:
    # Creating connection with stored data base
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    # Cursor is a special object stores the result of SELECT command.
    cursor = conn.cursor()
except sqlite3.OperationalError as error:
    foo.errorLog(error)
    sys.exit()

command_line = {'1': "[First name]", '2': "[Middle name]", '3': "[Last name]",
                '4': "Age", '5': "[Birth date]", '6': "City",
                '7': "Country", '8': "Phone"}
requestPool = ['1', '2', '3', '4', '5', '6', '7', '8']

error_log = open("C:\\Users\\Boris\\PycharmProjects\\lab1\\error_log.txt", 'a')

def Mainmenu():

    button = input("________________________________\nWelcome to the Yellow book browser. "
                   "\nPress the needed number to move next."
                   "\n________________________________ "
                   "\nTo Find Information - 1 "
                   "\nTo Add Contact - 2"
                   "\nTo Delete Contact - 3"
                   "\nTo exit - 4"
                   "\n________________________________")
    if button:
        if button == '1':
            _Find.PrintInfoMenu()
        elif button == '2':
            _Addnew.AddContactMenu()
        elif button == '3':
            _Delete.DelContactMenu()
        elif button == '4':
            sys.exit(0)

        else:
            foo.exit_continue("This command is incorrect. Check if the commands' number is right."
                              "Probably you tried to input not a digit ( if so, try again)\n")
            Mainmenu()
    else:
        Mainmenu()


if __name__ == '__main__':
    try:
        Mainmenu()
        sys.exit()
    except BaseException as error:
        foo.errorLog(error)
        print("Check the log!")
        Mainmenu()





