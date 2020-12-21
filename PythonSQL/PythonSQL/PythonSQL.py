import sqlite3

def executeCommand(str):
    connection = getconnection()
    cursor = connection.cursor()
    cursor.execute(str)
    connection.commit()

def executeReader(str):
    connection = getconnection()
    cursor = connection.cursor()
    cursor.execute(str)
    return cursor.fetchall()

def AddCity(city):
    executeCommand(f"INSERT INTO Cities VALUES (null,'{city}')")

def addBuilding(city_ID,building_name, address):
    executeCommand(f"INSERT INTO buildings VALUES (null,'{city_ID}', '{building_name}', '{address}')")

def addCabinet(building_id, cab, floor):
    executeCommand(f"INSERT INTO cabinets VALUES ('{building_id}', '{cab}', '{floor}')")

def printsCities():
    rows = executeReader(f"SELECT city FROM cities")
    for row in rows:
        print(row)
    return len(rows)

def printBuildings():
    rows = executeReader("SELECT cities.city, building_name, building_address FROM buildings JOIN cities ON buildings.city_id = cities.id")
    for row in rows:
        print(row)
    return len(rows)

def printCabinets():
    rows = executeReader("SELECT buildings.building_name, cabinets.cabinet_cab, cabinets.cabinet_floor FROM cabinets JOIN buildings ON cabinets.building_id = buildings.id")
    for row in rows:
        print(row)
    return len(rows)

def printtable(tablename) -> int:
    rows = executeReader(f"SELECT * FROM {tablename}")
    for row in rows:
        print(row)
    return len(rows)

def gettable(tablename) -> list:
    rows = executeReader(f"SELECT * FROM {tablename}")
    return rows

def getconnection() -> sqlite3.dbapi2.Connection:
    connection = sqlite3.connect('buildings.db')
    return connection

def initializationTables():
    connection = getconnection()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cities(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    city text)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS buildings(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL,
    building_name text,
    building_address text,
    FOREIGN KEY (city_ID) REFERENCES cities(id))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS cabinets(
    building_id INTEGER NOT NULL, 
    cabinet_cab INTEGER NOT NULL, 
    cabinet_floor INTEGER NOT NULL, 
    FOREIGN KEY (building_id) REFERENCES buildings(id),
    CONSTRAINT pr_key PRIMARY KEY (building_id,cabinet_cab))""")
    connection.commit()

def DropAll():
    executeCommand("Drop table cities")
    executeCommand("Drop table buildings")
    executeCommand("Drop table cabinets")

def ClearAll():
    executeCommand("Delete from cabinets")
    executeCommand("Delete from buildings")
    executeCommand("Delete from cities")

if __name__ == '__main__':
    connection = sqlite3.connect('buildings.db')
    cursor = connection.cursor()

    DropAll()
    initializationTables()

    AddCity('Краснодар')
    addBuilding(1,"КубГУ","Ставропольская 149")
    addCabinet(1,100,0)
    addCabinet(1,200,0)

    printsCities()
    print("________________________")
    printBuildings()
    print("________________________")
    printCabinets()
