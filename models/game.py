from models.player import Player
class Game():
    def result(self, player1, player2):

        if player1.choice == player2.choice:
            return None
        if player1.choice == "rock" and player2.choice == "scissors":
            return player1.choice
        if player1.choice == "paper" and player2.choice == "rock":
            return player1.choice
        if player1.choice == "scissors" and player2.choice == "paper":
            return player1.choice
        return player2.choice   

    


        

  

