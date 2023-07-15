# from turtle import Turtle, Screen
#
# timmy = Turtle()  # Turtle is a class name and timmy is an object
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen() # Screen is also a class name
# print(my_screen.canvheight)  # canvheight is an attribute
# my_screen.exitonclick() # exitonclick is a method

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
