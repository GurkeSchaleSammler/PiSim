class Ecosystem:
    def __init__(self):
        self.organisms = []

    def add_organism(self, organism):
        self.organisms.append(organism)

    def simulate_day(self):
        for organism in self.organisms[:]:
            if not organism.live_one_day():
                self.organisms.remove(organism)
