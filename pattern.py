# Pseudo code:
# Initialize a string variable.
# Create a for loop with 9 iterations.
# If the iteration is one of the first 5, add a star to the string
# Else, if the iteration is not in the first 5, remove a * from the string.

stars = ""

for i in range(1, 10):
    # adding a star to the string for the first 5 iterations
    if i <= 5:
        stars = stars + "*"
        print(stars)

    # removing a star from the string for the last 4 iterations
    else:
        stars = stars.replace("*", "", 1)
        print(stars)
