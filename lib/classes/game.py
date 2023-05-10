class Game:
    def __init__(self, title):
        self._title = title
        self._results = []
        self._players = []
        
    def results(self, new_result=None):
        from classes.result import Result
        pass
    
    def players(self, new_player=None):
        from classes.player import Player
        pass
    
    def average_score(self, player):
        pass

    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if len(title) > 0 and len(self._title) < 1:
            self._title = title
        else:
            print("Title can not be changed after the game starts!")


    title = property(get_title, set_title)