continents_name=("Asia","Europe","North America","Africa","Australia")
print(continents_name[2])
try:
    continents_name[1]="South America"
except TypeError as error:
    print("Error found",error)



