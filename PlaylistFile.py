class PlaylistManagement:
    def __init__(self):
        pass

class Playlist(PlaylistManagement):
    def __init__(self, name, format, path):
        self.playlistList = []
        self.format = format
        self.playlistName = name
        self.path = _format + os.sep + "playlists" + os.sep + name + ".txt"

class PlaylistList:
    def __init__(self):
        path = _format + os.sep + "playlists"
        self.__playlists = []
