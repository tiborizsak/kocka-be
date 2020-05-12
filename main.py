from random import randint

from flask import Flask, jsonify

from flask_cors import CORS, cross_origin

from model.player import Player, PlayerSchema

app = Flask(__name__)
players = [Player("Pista", 0, 0, True), Player("Sandor", 0, 0, False)]

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/kockapp', methods=['POST'])
def kockapp():
    dobas()
    schema = PlayerSchema(many=True)
    playa = schema.dump(players)
    return jsonify(playa)

    # return "<br>".join([str(player) for player in players])
    # return "Hello World!"


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

    # if player.roll == 1:
    #     players[activePlayerIndex].isActive = False
    #     players[(activePlayerIndex + 1) % len(players)].isActive = True


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


if __name__ == '__main__':
    app.run()
