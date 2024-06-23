from blocks.player_block import Player

from blocks.mycelium import Mycelium

from blocks.cobblestone import Cobblestone
from blocks.iron_ore import IronOre
from blocks.gold_ore import GoldOre


class AllBlock:
    def __init__(self):
        self.player = Player()

        self.mycelium = Mycelium()

        self.cobblestone = Cobblestone()
        self.iron_ore = IronOre()
        self.gold_ore = GoldOre()

    def get_list_block(self):
        return {self.cobblestone: 7,
                self.iron_ore: 3,
                self.gold_ore: 1
                }
