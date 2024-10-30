def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):

    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i] 
       
    
magicians = ['David Copperfield', 'Harry Houdini', 'Teller', 'Derren Brown', 'Carrie Fisher']

make_great(magicians)
show_magicians(magicians)
