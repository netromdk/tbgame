# -*- Coding: utf-8 -*-
# Base class for implementing game logic.

from abc import ABCMeta, abstractmethod
from util import getInt

class Game(metaclass = ABCMeta):
    def __init__(self):
        self.numPlayers = None
        self.minPlayers = 2
        self.maxPlayers = 2
        self.players = {}
        self.initScore = 0
        self.endScore = None
        self.turn = 0
        self.totalTurns = 0
        self.finished = False

    def setup(self):
        self.numPlayers = getInt("How many players? [min={}, max={}]"
                                 .format(self.minPlayers, self.maxPlayers),
                                 min = self.minPlayers, max = self.maxPlayers)
        for i in range(self.numPlayers):
            self._createPlayer(i + 1)

    def nextTurn(self):
        self.turn += 1
        self.totalTurns += 1

    def isFinished(self):
        return self.finished

    def _setFinished(self):
        self.finished = True

    def _resetTurns(self):
        self.turn = 0

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def _createPlayer(self, num):
        pass

    def _setPlayer(self, num, player):
        self.players[num] = player

    def _getWinner(self):
        keys = list(self.players.keys())
        max = (self.players[keys[0]], keys[0])
        for key in keys:
            player = self.players[key]
            if player.getScore() > max[0].getScore():
                max = (player, key)
        return max

