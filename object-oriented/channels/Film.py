from Program import Program

class Film(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

