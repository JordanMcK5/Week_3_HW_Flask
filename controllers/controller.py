from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route("/")
def index():
    return render_template("base.html", title="RPS")

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game()

    winner = game.play(player_1, player_2)
    
    return render_template("results.html", player_1=player_1, player_2=player_2, winner=winner)

