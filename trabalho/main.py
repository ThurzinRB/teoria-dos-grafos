from dbclasses import *
from GraphFunctions import Graph

def canReceive(playerId, itemId):
    #1 : olha se player já visitou dungeon que dropa 
    #2: olha se player pode estar naquela dungeon
    itemDungeon = []
    playerVisits = []

    #recolhe todas as dungeons que possuem item
    for drop in drops:
        if drop.itemId == itemId:
            itemDungeon.append(drop.dungeonId)
    #recolhe todas as dungeons que o player visitou
    for visit in visits:
        if visit.playerId == playerId:
            playerVisits.append(visit.dungeonId)
            
    # caso o player não tenha visitado nenhuma dungeon que dropa aquele item ele é trapaceiro
    intersect = list(set(itemDungeon) & set(playerVisits)) #id das possíveis dungeons
    if len(intersect) == 0:
        return [False, 'Não visitou dungeon que dropa item']
    
    # caso ele visitou, tem que ver se ele tinha os requisitos pra visitar aquela dungeon
    # print(playerVisits)
    for i in intersect:
        dfs = prerequisites.DFS(i)
        if set(dfs).issubset(set(playerVisits)):
            return [True, 'cidadão de bem']
    
    return [False, 'Não tem prerequisitos']
        

# Importa Item
file_path = 'trabalho/DB/Items.grafos.csv'
csv_data = read_csv_file(file_path)
csv_data.pop(0)
items = []
items = [Item(row[0], row[1]) for row in csv_data]


# Importa Dungeon
file_path = 'trabalho/DB/Dungeons.grafos.csv'
csv_data = read_csv_file(file_path)
csv_data.pop(0)
dungeons = []
dungeons = [Dungeon(row[0], row[1]) for row in csv_data]


# Importa Drops
file_path = 'trabalho/DB/Drops.grafos.csv'
csv_data = read_csv_file(file_path)
csv_data.pop(0)
drops = []
drops = [Drops(row[0], row[1]) for row in csv_data]


# Importa player
file_path = 'trabalho/DB/Players.grafos.csv'
csv_data = read_csv_file(file_path)
csv_data.pop(0)
players = []
players = [Player(row[0], row[1]) for row in csv_data]


# Importa playerHas
file_path = 'trabalho/DB/Has.grafos.csv'
csv_data = read_csv_file(file_path)
csv_data.pop(0)
playerHas = []
playerHas = [PlayerHas(row[0], row[1]) for row in csv_data]


# Importa Visits
file_path = 'trabalho/DB/Visits.grafos.csv'
csv_data = read_csv_file(file_path)
csv_data.pop(0)
visits = []
visits = [Visits(row[0], row[1], row[2]) for row in csv_data]


#criação do grafo de pré requisitos
prerequisites = Graph(len(dungeons))
readPrerequisites(prerequisites, 'trabalho/DB/Prerequisites.grafos.csv')
# print(prerequisites.graph[6])

prerequisites.save_dot_file('grafo.dot')

# canReceive(1,1)
print(canReceive(2, 10)) # [False, 'Não tem prerequisitos']
print(canReceive(2, 8)) # [False, 'Não visitou dungeon que dropa item']
print(canReceive(1, 1)) # [True, cidadão de bem]

print(prerequisites.Toposort())

