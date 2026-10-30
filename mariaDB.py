
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
                
                
                self.conn.commit()
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


    def viewOpenSlots(char):
        try:
            self.cur.execute("SELECT castType FROM characters JOIN class ON characters.class = class.name WHERE name = %s ", char)
            castType = self.cur.fetchone()[0]
            
            if castType = "Full":
                self.cur.execute("SELECT lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9 FROM slotProgression WHERE castType = %s", castType)
            else:
                # is a half caster
                self.cur.execute("SELECT lvl1, lvl2, lvl3, lvl4, lvl5 FROM slotProgression WHERE castType = %s", castType)

            slots = self.cur.fetchall()
            
            lvl = 1
            
            for slotLvl in slots:
                self.cur.execute("SELECT * FROM prepared WHERE charName = %s AND spelllvl = %s", char, slots)
                used = len(self.cur.fetchall())
                slotLvl = slotLvl - used
                print("Lvl " + lvl + ": " + slotLvl)
                lvl += 1

        except pymysql.MYSQLError as e:
            print("Could not check open slots")


    def learnSpell(char, spell):
        
        try:
            # Check to see if that spell is in spell list.
            self.cur.execute("SELECT lvl, class, castType FROM characters JOIN class ON characters.class = class.name WHERE name = %s ", char)
        
            charClass = self.cur.fetchone()[0]
            charLvl = self.cur.fetchone()[1]
            charCastType = self.cur.fetchone()[2]
        
            self.cur.execute("SELECT spellName FROM learns WHERE className = %s", charClass)
            
            if (self.cur.fetchone()[0] is not None):
                # Check if the character has an open slot of that level
                self.cur.execute("SELECT spellLvl FROM learns WHERE spellName = %s", spell)
                spellLvl = self.cur.fetchone()[0]

                self.cur.execute("SELECT * FROM prepared WHERE charName = %s AND spellLvl = %s", char, spellLvl)
                spellsOfLvl = self.cur.fetchall()

                self.cur.execute("SELECT lvl%s FROM slotProgression WHERE playerLvl = %s AND castType = %s", spellLvl, lvl, charCastType)

                if len(spellsOfLvl) >= self.cur.fetchone()[0]:
                    print("You have already prepared your maximum of " + spellLvl + " spell slots! Please forget a spell and try again.")
                    return
                else:
                    cur.execute("INSERT INTO prepared (charName, spellName, spelllvl) VALUES (%s, %s, %s)", char, spell, spellLvl)
                    
                self.conn.commit()
                print("Spell added!")
            else:
                self.conn.rollback()
                print("You can not learn that spell!")
            
        except pymysql.MYSQLError as e:
            print("Could not add spell!")
            
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
