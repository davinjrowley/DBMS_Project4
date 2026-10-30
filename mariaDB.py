
from typing import Self
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
        self.cur.execute(query, (x,))
        #comma is the cause it needs to be a tuple even when there is only one input
    
        records = self.cur.fetchall()
   
        if records:
            for record in records:
                print(record)
        else:
            print("No record found.")

    def createCharacter(self, name, lvl, className):
    
        try:
            lvl = int(lvl)
        except ValueError:
            print("Invalid level. Enter a whole number.")
            return
    
        if lvl < 1 or lvl > 20:
            print("Invalid level")
            return

        try:
            self.cur.execute(
                "SELECT name FROM `class` WHERE name = %s",
                (className,)
            )

            if self.cur.fetchone() is None:
                print("Invalid class")
                return

            query1 = "INSERT INTO characters (name, lvl, class) VALUES (%s, %s, %s)"

            self.cur.execute(query1, (name, lvl, className))

            self.conn.commit()
            print("Character created successfully")

        except pymysql.MySQLError as e:
            self.conn.rollback()
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
            self.conn.rollback()
            print("Could not level up character: ", e)
            

    def viewSpellbook(c):
        self.cur.execute("SELECT spellLvl, spellName FROM learns WHERE name = %s", c)
    
        records = self.cur.fetchall()
   
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
            self.cur.execute(
                "SELECT charName FROM `prepared` WHERE name = %s",
                (char,)
            )

            if self.cur.fetchone() is None:
                print("Invalid character")
                return

            self.cur.execute("SELECT spellName FROM `prepared` WHERE spellName = %s",
                (spell,)
            )

            if self.cur.fetchone() is None:
                print("Invalid spell")
                return

            query1 = "DELETE FROM `prepared` WHERE charName = %s AND spellName = %s"

            self.cur.execute(query1, (char, spell))

            self.conn.commit()
            print("Spell unprepared successfully")

        except pymysql.MySQLError as e:
            self.conn.rollback()
            print("Could not unprepare spell:", e)
 
    def closeConnection():
        self.cur.close()
        self.conn.close()
