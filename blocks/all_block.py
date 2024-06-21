from blocks.cobblestone import Cobblestone
from blocks.gold_ore import GoldOre
from blocks.iron_ore import IronOre
from blocks.player import Player


class AllBlock:
    def __init__(self):
        self.player = Player()

        self.cobblestone = Cobblestone()
        self.iron_ore = IronOre()
        self.gold_ore = GoldOre()

    def get_list_block(self):
        return [self.cobblestone, self.iron_ore, self.gold_ore]
