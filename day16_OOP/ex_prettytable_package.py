from prettytable import PrettyTable

# add methods like add.colum
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

# you can also change the objects attribute for example the appearance of table
table.align = "l"

print(table)

