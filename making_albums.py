def make_album(artist, albumtitle, numOftrack=0):
    albumInfo = {'Artist Name': artist, 'Album Title': albumtitle}
    if numOftrack:
        albumInfo['Number of Track'] = numOftrack
    print(albumInfo)


def fav_songs(artist, song):
    print(artist, song)
