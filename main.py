from mariaDB import MariaDB

def main():

    db = MariaDB()

    usr_inp = ""

    while usr_inp != "done":
        usr_inp = input("What is your command. Type help for all commands. Type done to exit: ")

        if usr_inp == "help":
            print("help\ndone\nlook up\ncreate character\nlevel up\nview spellbook\nlearn spell\nview spell slots\nunprepare")

main()