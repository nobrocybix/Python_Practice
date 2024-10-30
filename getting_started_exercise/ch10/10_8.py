files = ["cats.txt", "dogs.txt"]

def pet(file):
    try:       
        with open(file) as file_objects:
            names = file_objects.readlines()

            for name in names:
                print(name.rstrip())

    except FileNotFoundError:
        print(file + "檔案不存在")        

for file in files:
    pet(file)