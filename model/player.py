from marshmallow import Schema, fields


class Player:
    def __init__(self, playerName, roundScore, totalScore, isActive):
        self.playerName = playerName
        self.roundScore = roundScore
        self.totalScore = totalScore
        self.isActive = isActive
        self.roll = 1

    def __str__(self):
        return " // ".join([str(playerData) for playerData in [self.playerName, self.roundScore, self.totalScore, self.isActive, self.roll]])

class PlayerSchema(Schema):
    playerName = fields.Str()
    roundScore = fields.Number()
    totalScore = fields.Number()
    isActive = fields.Boolean()
    roll = fields.Number()