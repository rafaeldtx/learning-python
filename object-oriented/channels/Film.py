from Program import Program

class Film(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes} - Duration: {self.duration}min'
