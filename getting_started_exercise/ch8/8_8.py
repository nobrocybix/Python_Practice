def make_album(artist, title, Number_of_Songs=''):
    
    album = {'Artist': artist, 'Title': title}
    
    if Number_of_Songs:
        album['Number_of_Songs'] = Number_of_Songs
    return album


while True:
    artists = input('請輸入歌手名稱:')
    titles = input('請輸入歌曲名稱:')
    list_album = make_album(artists, titles)

    print(list_album)

    if input('請問要輸入下一首歌嗎?(y/n)') == 'n':
        break

    