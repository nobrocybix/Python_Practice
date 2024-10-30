filename = "learning_python.txt"

with open(filename) as learning:     
    contents = learning.read()
    print(contents)    


with open(filename) as learning:     
    for line in learning:
        newline = line.replace('Python', 'C')
        print(newline.rstrip())

print("\n")

with open(filename) as learning:
    lines = learning.readlines()
    
for line in lines:
    newline = line.replace('Python', 'C')
    print(newline.rstrip())