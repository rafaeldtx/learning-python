class Playlist:
    def __init__(self, name, programs):
        self._name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]
