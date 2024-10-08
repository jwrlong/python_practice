test = input ("name: ")
print(test)

cube = 8  # The number for which we want to find the cube root

# Iterate through possible guesses for the cube root
for guess in range(abs(cube) + 1):
    # Check if the cube of the guess is equal to the absolute value of the cube
    if guess**3 >= abs(cube):
        break  # Exit the loop if the cube of guess is greater than or equal to cube

# After the loop, check if the guess was correct
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    # If the cube was negative, make guess negative
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))