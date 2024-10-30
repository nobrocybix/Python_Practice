filename = "learning_python.txt"

with open(filename) as learning:     
    contents = learning.read()
    print(contents)    


with open(filename) as learning:     
    for line in learning:
        print(line.rstrip())

print("\n")

with open(filename) as learning:
    lines = learning.readlines()
    
for line in lines:
    print(line.rstrip())