def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    great_magicians = []
    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i] 
        great_magicians.append(magicians[i])
    return great_magicians

magicians = ['David Copperfield', 'Harry Houdini', 'Teller', 'Derren Brown', 'Carrie Fisher']

great = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great)