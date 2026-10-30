
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='stuegre',
    passwd='stuegre',
    db='stuegre'
)

cur = conn.cursor()

def lookUp():
    
    x = input("Enter a name: ")
    y = input("Enter a table: ")
    
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
    


def createCharacter():
    name = input("Enter your character's name: ")
    
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

def levelUp(char):
    #char = input("Enter character name: ")
    
    cur.execute("SELECT lvl FROM characters WHERE name = %s", char)
    
    charLvl = cur.fetchone()[0]
    
    if (charLvl == 20):
        print(f"{char} is at maximum level!")
    else:
        try:
            # Update characters to have lvl + 1
            query1 = "UPDATE characters SET lvl = lvl + 1 WHERE name = %s"
            
            cur.execute(query1, (char,))
            
            
            conn.commit()
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


def viewOpenSlots(char):
    try:
        cur.execute("SELECT castType FROM characters JOIN class ON characters.class = class.name WHERE name = %s ", char)
        castType = cur.fetchone()[0]
        
        if castType = "Full":
            cur.execute("SELECT lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9 FROM slotProgression WHERE castType = %s", castType)
        else:
            # is a half caster
            cur.execute("SELECT lvl1, lvl2, lvl3, lvl4, lvl5 FROM slotProgression WHERE castType = %s", castType)

        slots = cur.fetchall()
        
        lvl = 1
        
        for slotLvl in slots:
            cur.execute("SELECT * FROM prepared WHERE charName = %s AND spelllvl = %s", char, slots)
            used = len(cur.fetchall())
            slotLvl = slotLvl - used
            print("Lvl " + lvl + ": " + slotLvl)
            lvl += 1

    except pymysql.MYSQLError as e:
        print("Could not check open slots")


def learnSpell(char, spell):
    
    try:
        # Check to see if that spell is in spell list.
        cur.execute("SELECT lvl, class, castType FROM characters JOIN class ON characters.class = class.name WHERE name = %s ", char)
    
        charClass = cur.fetchone()[0]
        charLvl = cur.fetchone()[1]
        charCastType = cur.fetchone()[2]
    
        cur.execute("SELECT spellName FROM learns WHERE className = %s", charClass)
        
        if (cur.fetchone()[0] is not None):
            # Check if the character has an open slot of that level
            cur.execute("SELECT spellLvl FROM learns WHERE spellName = %s", spell)
            spellLvl = cur.fetchone()[0]

            cur.execute("SELECT * FROM prepared WHERE charName = %s AND spellLvl = %s", char, spellLvl)
            spellsOfLvl = cur.fetchall()

            cur.execute("SELECT lvl%s FROM slotProgression WHERE playerLvl = %s AND castType = %s", spellLvl, lvl, charCastType)

            if len(spellsOfLvl) >= cur.fetchone()[0]:
                print("You have already prepared your maximum of " + spellLvl + " spell slots! Please forget a spell and try again.")
                return
            else:
                cur.execute("INSERT INTO prepared (charName, spellName, spelllvl) VALUES (%s, %s, %s)", char, spell, spellLvl)
                
            conn.commit()
            print("Spell added!")
        else:
            conn.rollback()
            print("You can not learn that spell!")
        
    except pymysql.MYSQLError as e:
        print("Could not add spell!")



    
cur.close()
conn.close()
