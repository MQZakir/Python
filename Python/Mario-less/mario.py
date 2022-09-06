from cs50 import get_int

# Loop for getting a correct input on an integer from 1 to 8
while True:
    height = get_int("Height: ")
    width = height
    if height > 0 and height <= 8:
        break

# loop for printing the wall
for i in range(1, height + 1):
    hash = i
    space = width - hash

    print(" " * space, end="")
    print("#" * hash)
