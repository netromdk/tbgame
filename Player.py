# -*- Coding: utf-8 -*-
# Base class for representing a player in a game.

class Player():
    def __init__(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def addScore(self, value):
        self.score += value
