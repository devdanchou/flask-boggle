from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    return {"gameId": game_id, "board": f"{game.board}"}

@app.post("/api/score-word")
def score_word():
    """ return JSON response of game id and word """
    word = request.json["word"]
    game_id = request.json["gameId"]

    curr_game = games[game_id]

    if curr_game.is_word_in_word_list(word) and
        curr_game.check_word_on_board(word):
        return jsonify({result: "ok"})
    elif not curr_game.is_word_in_word_list(word):
        return jsonify({result: "not-word"})
    elif not curr_game.check_word_on_board(word):
        return jsonify({result: "not-on-board"})


    # if word not in games[game_id].word_list:
    #     return {result: "not-word"}
    #









