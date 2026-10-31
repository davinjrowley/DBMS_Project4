
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
                
                
                self.conn.commit()
            except pymysql.MySQLError as e:
                self.conn.rollback()
                print("Could not level up character: ", e)
            

    def viewSpellbook(self, c):
        self.cur.execute("SELECT spellLvl, spellName FROM learns WHERE className = %s", c)
    
        records = self.cur.fetchall()
   
        if records:
            for record in records:
                print(record)
        else:
            print("No record found.")


    def viewOpenSlots(self, char):
        try:
            self.cur.execute(
                """SELECT castType FROM characters
                JOIN class ON characters.class = class.name
                WHERE characters.name = %s""",
                (char,)
            )

            result = self.cur.fetchone()

            if result is None:
                print("Character not found!")
                return

            castType = result[0]

            self.cur.execute(
                "SELECT lvl FROM characters WHERE name = %s",
                (char,)
            )
            charLvl = self.cur.fetchone()[0]

            if castType == "Full":
                self.cur.execute(
                    """SELECT lvl1, lvl2, lvl3, lvl4, lvl5,
                          lvl6, lvl7, lvl8, lvl9
                   FROM slotProgression
                   WHERE playerLvl = %s AND castType = %s""",
                (charLvl, castType)
            )
            else:
                self.cur.execute(
                """SELECT lvl1, lvl2, lvl3, lvl4, lvl5
                   FROM slotProgression
                   WHERE playerLvl = %s AND castType = %s""",
                (charLvl, castType)
            )

            slots = self.cur.fetchone()

            if slots is None:
                print("No slot progression found!")
                return

            for lvl, slotLvl in enumerate(slots, start=1):
                if slotLvl is None:
                    slotLvl = 0

                self.cur.execute(
                    """SELECT COUNT(*) FROM prepared
                   WHERE charName = %s AND spellLvl = %s""",
                (char, lvl)
                )

                used = self.cur.fetchone()[0]
                remaining = slotLvl - used

                print(f"Level {lvl}: {remaining} slots remaining")

        except pymysql.MySQLError as e:
            print("Could not check open slots:", e)


    def learnSpell(self, char, spell):
        
        try:
            # Check to see if that spell is in spell list.
            self.cur.execute("SELECT lvl, class, castType FROM characters JOIN class ON characters.class = class.name WHERE characters.name = %s ", (char,))
        
            result = self.cur.fetchone()

            if result is None:
                print("Character not found.")
                return

            charLvl, charClass, charCastType = result
        
            self.cur.execute(
            "SELECT spellLvl FROM learns WHERE className = %s AND spellName = %s",
            (charClass, spell)
            )

            spellResult = self.cur.fetchone()

            if spellResult is None:
                print("You cannot learn that spell!")
                return

            spellLvl = spellResult[0]
            
            if (spellLvl is not None):
                # Check if the character has an open slot of that level
                self.cur.execute("SELECT spellLvl FROM learns WHERE spellName = %s", (spell,))
                spellLvl = self.cur.fetchone()[0]

                self.cur.execute("SELECT * FROM prepared WHERE charName = %s AND spellLvl = %s", (char, spellLvl))
                spellsOfLvl = self.cur.fetchall()

                slotColumn = f"lvl{spellLvl}"

                self.cur.execute(
                    f"SELECT `{slotColumn}` FROM slotProgression WHERE playerLvl = %s AND castType = %s",
                    (charLvl, charCastType)
                )

                if len(spellsOfLvl) >= self.cur.fetchone()[0]:
                    print("You have already prepared your maximum of " + spellLvl + " spell slots! Please forget a spell and try again.")
                    return
                else:
                    self.cur.execute("INSERT INTO prepared (charName, spellName, spelllvl) VALUES (%s, %s, %s)", (char, spell, spellLvl))
                    
                self.conn.commit()
                print("Spell added!")
            else:
                self.conn.rollback()
                print("You can not learn that spell!")
            
        except pymysql.MySQLError as e:
            print("Could not add spell!")
            
    def unPrepare(self, char, spell):
        try:
            self.cur.execute(
                "SELECT charName FROM `prepared` WHERE charName = %s",
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
