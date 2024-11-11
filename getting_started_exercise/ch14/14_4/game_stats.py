class GameStates():
    '''Track Statistics for Alien Invasions.'''
    def __init__(self, ai_settings):
        '''Initialize statistics.'''
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        self.save_high_score()
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    
    def save_high_score(self):
        """Save high score to the txt."""
        try:
            filename = "high_score.txt"
            with open(filename, "r") as hg_obj:
                high_score = hg_obj.read()

            self.high_score = int(high_score)
        except FileNotFoundError:
            self.high_score = 0