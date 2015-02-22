# -*- Coding: utf-8 -*-
# Base class for implementing game logic.

from abc import ABCMeta, abstractmethod
from util import getInt

class Game(metaclass = ABCMeta):
    def __init__(self):
        self.minPlayers = 2
        self.maxPlayers = 2
        self.players = {}
        self.initScore = 0
        self.endScore = None
        self.turn = 0
        self.finished = False

    def setup(self):
        numPlayers = getInt("How many players? [min={}, max={}]"
                            .format(self.minPlayers, self.maxPlayers),
                            min = self.minPlayers, max = self.maxPlayers)
        for i in range(numPlayers):
            self._createPlayer(i + 1)

    def nextTurn(self):
        self.turn += 1
        print("[Turn {}]".format(self.turn))

    def isFinished(self):
        return self.finished

    def _setFinished(self):
        self.finished = True

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
        max = list(self.players.values())[0]
        for player in self.players.values():
            if player.getScore() > max.getScore():
                max = player
        return max

