import sys

# Vérifiez d'abord s'il y a au moins un argument
if len(sys.argv) > 2:
    print("AssertionError : more thant one argument is provided")
    sys.exit()

# Ensuite, essayez de convertir l'argument en un entier
try:
    arg = int(sys.argv[1])
except ValueError:
    print("AssertionError : argument is not an integer")
    sys.exit()

# Maintenant, vous pouvez vérifier si l'argument est pair ou impair
if arg % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")