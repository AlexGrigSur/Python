import sqlite3
import xml.etree as tree

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

def addBuildAddr(city_ID,building_name, address):
    executeCommand(f"INSERT INTO buildings_addr VALUES (null,'{city_ID}', '{building_name}', '{address}')")

def addBuilding(building_addr_id, cab, floor):
    executeCommand(f"INSERT INTO buildings VALUES ('{building_addr_id}', '{cab}', '{floor}')")


def printsCities(fio):
    rows = executeReader(f"SELECT city FROM cities")
    for row in rows:
        print(row)
    return len(rows)


def printBuildingsAddr():
    rows = executeReader(f"SELECT cities.city, building_name FROM buildings_addr JOIN cities ON buildings_addr.city_id = cities.id")
    for row in rows:
        print(row)
    return len(rows)

def printBuildings():
    rows = executeReader(f"SELECT buildings_addr.building_name, building_cab, building_floor FROM buildings JOIN buildings_addr ON buildings.building_addr_id = buildings_addr.id")
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
    cursor.execute("""CREATE TABLE IF NOT EXISTS buildings_addr(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL,
    building_name text,
    building_address text,
    FOREIGN KEY (city_ID) REFERENCES cities(id))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS buildings(
    building_addr_id INTEGER NOT NULL, 
    building_cab INTEGER NOT NULL, 
    building_floor INTEGER NOT NULL, 
    FOREIGN KEY (building_addr_id) REFERENCES buildings_addr(id),
    CONSTRAINT pr_key PRIMARY KEY (building_addr_id,building_cab))""")
    connection.commit()

def ClearAll():
    executeCommand("Delete from buildings")
    executeCommand("Delete from buildings_addr")
    executeCommand("Delete from cities")

if __name__ == '__main__':
    connection = sqlite3.connect('buildings.db')
    cursor = connection.cursor()

    initializationTables()
    ClearAll()

    AddCity('Краснодар')
    addBuildAddr(0,"КубГУ","Ставропольская 149")
    addBuilding(0,100,0)
    addBuilding(0,200,0)

    printtable("buildings")
