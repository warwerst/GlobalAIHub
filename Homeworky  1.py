"""
Take 5 values from the user and write a program that
prints the values you get on the screen.
Print the type of values you received in this program on the screen.
When using print functions, do not forget to use f-string and
format usage in your program.
"""

Numbers = []
Types = []

x = int(input("How many numbers do you want to enter?  : "))

for i in range(x):
    i += 1
    if i == 1:
        y = float(input(" Enter {}st Number Value: ".format(i)))
        Numbers += [y]
        z = type(y)
        Types += [z]

    elif i > 1:
        y = float(input(f" Enter {i}th Number Value: "))
        Numbers += [y]
        z = type(y)
        Types += [z]

print(*Numbers)
print(*Types)
