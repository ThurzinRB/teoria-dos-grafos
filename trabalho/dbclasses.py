import csv
class Visits:
    def __init__(self, PlayerId, DungeonId, time):
        self.playerId = PlayerId
        self.dungeonId = DungeonId
        self.time = time

class Drops:
    def __init__(self, DungeonId, ItemId):
        self.dungeonId = DungeonId
        self.itemId = ItemId
        
class PlayerHas:
    def __init__(self, PlayerId, ItemId):
        self.playerId = PlayerId
        self.itemId = ItemId

class Dungeon:
    def __init__(self, DungeonName, DungeonId):
        self.name = DungeonName
        self.id = DungeonId

class Item:
    def __init__(self, itemName, itemId):
        self.name = itemName
        self.id = itemId

class Player:
    def __init__(self, itemName, itemId):
        self.name = itemName
        self.id = itemId


def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data