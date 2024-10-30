def make_album(artist, title, Number_of_Songs=''):
    
    album = {'Artist': artist, 'Title': title}
    
    if Number_of_Songs:
        album['Number_of_Songs'] = Number_of_Songs
    return album


print(make_album('Michael Jackson', 'Thriller'))
print(make_album('Pink Floyd', 'The Dark Side of the Moon'))
print(make_album('Nirvana', 'Nevermind', 10))