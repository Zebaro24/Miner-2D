class Player:
    def __init__(self, nickname):
        self.count_cobblestone = 0
        self.nickname = nickname

        self.count_iron = 0
        self.count_gold = 0
        self.item = {"level":0, "item" : "hand"}
        self.count_tokens = 0

    def add_iron(self):
        self.count_iron += 1

    def add_gold(self):
        self.count_gold += 1

    def convert_to_token(self):
        self.count_tokens += self.count_iron * 4
        self.count_tokens += self.count_gold * 10
        self.count_tokens += self.count_cobblestone
        self.count_cobblestone, self.count_iron, self.count_gold = 0, 0, 0

    def add_cobblestone(self):
        self.count_cobblestone+=1
