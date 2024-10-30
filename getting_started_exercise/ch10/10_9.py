files = ["cats.txt", "dogs.txt"]

def pet(file):
    try:       
        with open(file) as file_objects:
            names = file_objects.readlines()

            for name in names:
                print(name.rstrip())

    except FileNotFoundError:
        pass        

for file in files:
    pet(file)