class GameStats:
    def __init__(self, ai_settings) -> None:
        self.ai_settings = ai_settings
        self.reset_status()
        self.game_active = False
        self.high_score = 0

    def reset_status(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1