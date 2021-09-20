from models.player import Player
class Game():
    def result(self, player1, player2):

        moves = {
            "rock" : "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if player1.choice == player2.choice:
            return None
        if player2.choice in moves[player1.choice]:
            return player1.choice
        return player2.choice   

    


        

  

