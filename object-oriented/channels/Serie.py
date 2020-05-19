from Program import Program

class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes} - Seasons: {self.seasons}'
