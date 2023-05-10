class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        
    def results(self, new_result=None):
        from classes.result import Result
        
        pass
    
    def games_played(self, new_game=None):
        from classes.game import Game
        pass
    
    def played_game(self, game):
        pass
    
    def num_times_played(self, game):
        pass
    
    @classmethod
    def highest_scored(cls, game):
        pass
    

    def get_username(self):
        return self._username

    def set_username(self, name):
        if 2 <= len(name) <= 16:
            self._username = name
        else:
            print("Username must be between 2 and 16 characters.")
    
    username = property(get_username, set_username)