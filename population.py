import config
import player

class Population:
    def __init__(self) -> None:
        self.player = player.Player()

    def update_live_player(self):
        self.player.draw(config.window)