class GameStates():

    def __init__(self, s):
        '''Initialize statistics'''
        self.s = s
        self.reset_game()        
        self.ball_total_catch = s.ball_total_catch

    def reset_game(self):
        '''Reset Game'''
        self.ball_left = self.s.ball_limit