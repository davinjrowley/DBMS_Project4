
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

        query1 = "INSERT INTO characters (name, lvl) VALUES (%s, %s)"
        query2 = "INSERT INTO invests (charName, className) VALUES (%s, %s)"

        cur.execute(query1, (name, lvl))
        cur.execute(query2, (name, className))

        conn.commit()
        print("Character created successfully")

    except pymysql.MySQLError as e:
        conn.rollback()
        print("Could not create character:", e)
    
cur.close()
conn.close()
