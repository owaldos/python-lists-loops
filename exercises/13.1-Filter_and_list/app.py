
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def name_with_letter_r(name):
    if name.find('R')== 0:
        return name

resulting_names= list(filter(name_with_letter_r, all_names))
print(resulting_names)




