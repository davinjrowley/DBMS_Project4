from mariaDB import MariaDB

def main():

    db = MariaDB()

    usr_inp = ""

    while usr_inp != "done":
        usr_inp = input("What is your command. Type help for all commands. Type done to exit: ")

        if usr_inp == "help":
            print("help\ndone\nlook up\ncreate character\nlevel up\nview spellbook\nlearn spell\nview spell slots\nunprepare")
        elif usr_inp == "look up":
            x = input("What is the name you are trying to look up: ")
            y = input("What table are you trying to look up (characters, class, spell): ")
            db.lookUp(x, y)
        elif usr_inp == "create character":
            name = input("What is your character's name: ")
            lvl = input("What is your character's level: ")
            className = input("What is your character's class: ")
            db.createCharacter(name, lvl, className)
        elif usr_inp == "level up":
            name = input("What is your character's name: ")
            db.levelUp(name)
        elif usr_inp == "view spellbook":
            className = input("What is your character's class: ")
            db.viewSpellbook(className)
        elif usr_inp == "learn spell":
            char = input("What is the name of your character: ")
            spell = input("What is the name of the spell: ")
            db.learnSpell(char, spell)
        elif usr_inp == "view spell slots":
            char = input("What is the name of your character: ")
            db.viewOpenSlots(char)
        elif usr_inp == "unprepare":
            char = input("What is the name of your character: ")
            spell = input("What is the name of the spell: ")
            db.unPrepare(char, spell)
    db.closeConnection()

main()
