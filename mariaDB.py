
import pymysql

class MariaDB:
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='stuegre',
            passwd='stuegre',
            db='stuegre'
        )
        self.cur = self.conn.cursor()

    def closeConnection(self):
        self.cur.close()
        self.conn.close()

    def lookUp(self, x, y):
    
        tables = {"class", "characters", "spell"}
    
        if y not in tables:
           print("Invalid table error")
           return

        query = f"SELECT * FROM {y} WHERE name = %s"
        cur.execute(query, (x,))
        #comma is the cause it needs to be a tuple even when there is only one input
    
        records = cur.fetchall()
   
        if records:
            for record in records:
                print(record)
        else:
            print("No record found.")

    def createCharacter(self, name):
    
        try:
            lvl = int(input("Enter your level: "))
        except ValueError:
            print("Invalid level. Enter a whole number.")
            return
    
        className = input("Enter your class: ")
    
        if lvl < 1 or lvl > 20:
            print("Invalid level")
            return

        try:
            cur.execute(
                "SELECT name FROM `class` WHERE name = %s",
                (className,)
            )

            if cur.fetchone() is None:
                print("Invalid class")
                return

            query1 = "INSERT INTO characters (name, lvl, class) VALUES (%s, %s, %s)"

            cur.execute(query1, (name, lvl, className))

            conn.commit()
            print("Character created successfully")

        except pymysql.MySQLError as e:
            conn.rollback()
            print("Could not create character:", e)

def levelUp(self, char):
    #char = input("Enter character name: ")

    self.cur.execute("SELECT lvl FROM characters WHERE name = %s", char)

    charLvl = self.cur.fetchone()[0]
    
    if (charLvl == 20):
        print(f"{char} is at maximum level!")
    else:
        try:
            # Update characters to have lvl + 1
            query1 = "UPDATE characters SET lvl = lvl + 1 WHERE name = %s"
            self.cur.execute(query1, (char,))
            self.cur.execute(query1, (char,))


            # Updates invests to have their class specifics
            # Has to check if the Wait we may not need this
            """
            cur.execute("SELECT class FROM characters WHERE name = %s", char)
            charClass = cur.fetchone()[0]
            
            cur.execute("SELECT castType FROM class WHERE name = %s", charClass)
            castType = cur.fetchone()[0]
            
            """
            
        except pymysql.MYSQLError as e:
            conn.rollback()
            print("Could not level up character: ", e)
            

    def viewSpellbook(c):
        cur.execute("SELECT spellLvl, spellName FROM learns WHERE name = %s", c)
    
        records = cur.fetchall()
   
        if records:
            for record in records:
                print(record)
        else:
            print("No record found.")
    

    def learnSpell(char, spell):
        """
        char = input("Enter character name: ")
    
        spell = input("Enter desired spell: ")
        """
        
    def unPrepare(char, spell):
        try:
            cur.execute(
                "SELECT charName FROM `prepared` WHERE name = %s",
                (char,)
            )

            if cur.fetchone() is None:
                print("Invalid character")
                return

            cur.execute("SELECT spellName FROM `prepared` WHERE spellName = %s",
                (spell,)
            )

            if cur.fetchone() is None:
                print("Invalid spell")
                return

            query1 = "DELETE FROM `prepared` WHERE charName = %s AND spellName = %s"

            cur.execute(query1, (char, spell))

            conn.commit()
            print("Spell unprepared successfully")

        except pymysql.MySQLError as e:
            conn.rollback()
            print("Could not unprepare spell:", e)
 
    def closeConnection():
        cur.close()
        conn.close()
