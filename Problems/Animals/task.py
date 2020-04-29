# read animals.txt
file = open('animals.txt', 'r')
animal_list = file.readlines()
# and write animals_new.txt
new_file = open('animals_new.txt', 'w')
for animal in animal_list:
    animal = animal.rstrip()
    new_file.write(animal + ' ')
file.close()
new_file.close()
