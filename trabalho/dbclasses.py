import csv
from GraphFunctions import Graph

class Visits:
    def __init__(self, PlayerId, DungeonId, time):
        self.playerId = int(PlayerId)
        self.dungeonId = int(DungeonId)
        self.time = time

class Drops:
    def __init__(self, DungeonId, ItemId):
        self.dungeonId = int(DungeonId)
        self.itemId = int(ItemId)
        
class PlayerHas:
    def __init__(self, PlayerId, ItemId):
        self.playerId = int(PlayerId)
        self.itemId = int(ItemId)

class Dungeon:
    def __init__(self, DungeonName, DungeonId):
        self.name = DungeonName
        self.id = int(DungeonId)

class Item:
    def __init__(self, itemName, itemId):
        self.name = itemName
        self.id = int(itemId)

class Player:
    def __init__(self, playerName, playerId):
        self.name = playerName
        self.id = int(playerId)


def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def readPrerequisites(grafo: Graph, path):
    data = read_csv_file(path)
    data.pop(0)
    for row in data:
        # print(' ')
        # print(row)
        if len(row[1])> 0:
            edges = map(int, row[1].split('-'))
            for edge in edges:
                # print(row[0], edge)
                grafo.addEdge(int(row[0]), edge)
    