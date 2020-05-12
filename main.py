from random import randint

from flask import Flask, jsonify

from flask_cors import CORS, cross_origin

from model.player import Player, PlayerSchema

app = Flask(__name__)
CORS(app)

players = [Player("Pista", 0, 0, True), Player("Sandor", 0, 0, False)]


@app.route('/kockapp')
@cross_origin()

def kockapp():
    dobas()
    schema = PlayerSchema(many=True)
    playa = schema.dump(players)
    return jsonify(playa)

    # return "<br>".join([str(player) for player in players])


def dobas():
    activePlayerIndex = None

    for n, player in enumerate(players):
        if player.isActive:
            player.roll = randint(1, 6)
            activePlayerIndex = n

            if player.roll == 1:
                player.roundScore = 0
                players[activePlayerIndex].isActive = False
                players[(activePlayerIndex + 1) % len(players)].isActive = True
            else:
                player.roundScore += player.roll


if __name__ == '__main__':
    app.run()
