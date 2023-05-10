class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

    def get_score(self):
        return self._score

    def set_score(self, score):
        if 1 <= score <= 5000:
            self._score = score
        else:
            print("Score must be between 1 and 5000")

    def get_player(self):
        print(self._player.username)
        return self._player

    def set_player(self, player):
        from classes.player import Player
        if isinstance(player, Player):
            self._player = player
        else:
            print(f"Player must be <class Player> instead of {type(player)}")
    
    def get_game(self):
        return self._game

    def set_game(self, game):
        from classes.game import Game
        if isinstance(game, Game):
            self._game = game
        else:
            print(f"Game must be <class Game> instead of {type(game)}")

    score = property(get_score, set_score)
    player = property(get_player, set_player)
    game = property(get_game, set_game)