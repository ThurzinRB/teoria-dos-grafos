from dbclasses import *
from GraphFunctions import Graph



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
print(prerequisites.graph[6])

prerequisites.save_dot_file()




