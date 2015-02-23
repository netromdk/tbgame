# -*- Coding: utf-8 -*-
# Base class for representing a player in a game.

class Player():
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def addScore(self, value):
        self.score += value

    def toTuple(self):
        return (self.name, self.score)
