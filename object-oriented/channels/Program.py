class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, likes):
        self._likes = likes.title()

    def __str__(self):
        return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes}'

class Film(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes} - Duration: {self.duration}min'

class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes} - Seasons: {self.seasons}'

class Playlist:
    def __init__(self, name, programs):
        self._name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]
