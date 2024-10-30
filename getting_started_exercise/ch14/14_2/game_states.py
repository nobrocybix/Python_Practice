class GameState():

    def __init__(self, g_settings):
        '''Initialize statistics'''
        self.s = g_settings

        # Game active status
        self.running = False

        self.reset_score()
        self.reset_miss()
        
    def reset_score(self):
        # Reset HIT Scores
        self.hit = self.s.hit

    def reset_miss(self):
        # Reset miss numbers
        self.miss = self.s.miss