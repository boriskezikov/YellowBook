"""___THIS MODULE INCLUDES FUNCTIONS USING IN THE PROGRAM EXACTLY OFTEN___"""
import datetime
import sys
import random

try:
    import main
except ImportError as f:
    error_log = open("C:\\Users\\Boris\\PycharmProjects\\lab1\\error_log.txt", 'a')
    error_log.write(str(datetime.datetime.now()))
    error_log.write(str(f))
    error_log.write('\n')
    print("Import problem. Restart the app")
    sys.exit()


""" ____The function checks if string consists of letters and digits and _ ____"""

# Symbols forbidden in First,Middle,Lase names etc.
symbols = ['!', '.', ',', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '"', '№',
           ';', '?', '/', '\\', '~', '`', '\'',':' '<', '>', '{', '}', '[', ']', '|']


def isalnum(space, data):

    """
        Creates a list composed of elements which are not included into the 'restrictions' list. 
        Next, compares  current list and user-entered string lengths.
        If they match each other, so the user-input is correct.    
    
    """
    user_input_list = [x for x in space if x not in symbols]

    # НАПИСАТЬ РАНДОМНУЮ ФУНКЦИЮ ПРОВЕРКИ НА ПРОБЕЛЫ

    if len(user_input_list) == len(space) and (len(space) != 0):
        space = space.lower().capitalize()
        data.append(space.strip())
        return
    else:
        print("Your input was incorrect! This field should consist of letters and digits:\n")
        isalnum(input(), data)


"""_____The function asks user to exit or go the main menu______"""


def exit_continue(*args):
    if input("{} y/n".format(args)).lower() == 'y':
        main.Mainmenu()
    else:
        print("Thanks for choosing us!")
        sys.exit()


"""__Universal function provides to interact with Data Base__"""


def search_delete_edit(command, paramName, paramVal):
    if main.cursor:
        if command == "select":
            main.cursor.execute("SELECT * FROM Yellowbook WHERE {0} = \"{1}\" ".format(paramName, str(paramVal)).lower().capitalize())
            main.conn.commit()
            return main.cursor.fetchall()
        elif command == "delete":
            main.cursor.execute("SELECT * FROM Yellowbook WHERE {0} = \"{1}\" ".format(paramName, paramVal.lower().capitalize))
            if main.cursor.fetchall() is True:
                main.cursor.execute("DELETE FROM Yellowbook WHERE {0} = \"{1}\" ".format(paramName, str(paramVal)).lower().capitalize())
                main.conn.commit()
                return 1
            else:
                return 0

        elif command == "edit":
            main.cursor.execute("UPDATE Yellowbook SET {0} = \"{1}\" ".format(paramName, str(paramVal)).lower().capitalize())
            main.conn.commit()
            return 1
        else:
            raise UserWarning
    else:
        print("No connection with database")
        return 0

def errorLog(f):
    error_log = open("C:\\Users\\Boris\\PycharmProjects\\lab1\\error_log.txt", 'a')
    error_log.write(str(datetime.datetime.now()))
    error_log.write(str(f))
    error_log.write('\n')
    error_log.close()

# Function "whitespace_extract" gets a value and calls a random symbol in the string.
# Next, it checks if neighbour symbols are not whitespaces.
# So thanks this uncomplicated algorithm we have an opportunity to uniquely reveal
# if user input consists of whitespaces only


def whitespace_extract(value):
    x = random.randrange(len(value))
    if x != 0:
        if value[x] == ' ':
            if value[x+1]:
                if value[x-1]:
                    if (value[x+1] == ' ') and (value[x-1] == ' '):
                        print("This space must include 1 not white space symbol at least")
                        return 0
                    else:
                        return 0
                print("This space must include 1 not white space symbol at least")
                return 0
            print("This space must include 1 not white space symbol at least")
            return 0
        return 1
    print("This space must include 1 not white space symbol at least")
    return 0













