from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route("/")
def index():
    return render_template("base.html", title="RPS")

@app.route("/<player1_choice>/<player2_choice>")
def show_winner(player1_choice, player2_choice):
    player1 = Player("Player 1", player1_choice)
    player2 = Player("Player 2", player2_choice)
    winner = Game.result(Game, player1, player2)
    return render_template(
        "results.html",  
        player1_name = player1.name,
        player2_name = player2.name, 
        player1_choice = player1.choice, 
        player2_choice = player2.choice,
        winner = winner
        )

