"""
User Identification Program
The user will be defined. Get the data of this user
method. Obtain information from user as follow:
First Name
Last Name
Age
Date of birth(just year)
Pass the user's information to the list and display
the screen using the for loop. Print all user
information on the screen.
If he is under 18, print "You can not go out because
it is too dangerous" on the screen.
If he is over 18, print "You can go out to the street"
on the screen.
"""

from typing import List, Union

Checklist: List[List[Union[str, int]]] = []
x = int(input("How many users do you define it?"))
print("Enter the following your information!!! ")

for i in range(x):

    print(f"{i + 1}. person information")
    First_Name = str(input("First name: "))
    Last_Name = str(input("Last name: "))
    Age = int(input("Age: "))
    Year_of_Birth = int(input("Year of birth: "))

    if Age >= 18:
        a = "You can go out to the street"
        List = [First_Name, Last_Name, Age, Year_of_Birth, a]
        Checklist.append(List)
        continue

    else:
        a = "You can not go out because it is too dangerous"
        List = [First_Name, Last_Name, Age, Year_of_Birth, a]
        Checklist.append(List)

for j in Checklist:
    print(*j)
