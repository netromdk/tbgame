# -*- Coding: utf-8 -*-
# Base class for implementing game logic.

from abc import ABCMeta, abstractmethod
from util import getInt
import json
from datetime import datetime

class Game(metaclass = ABCMeta):
    def __init__(self):
        self.name = None
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

    def load(self, path):
        try:
            data = json.load(open(path, "r"))
            for key in data:
                if key == "numPlayers":
                    self.numPlayers = data[key]
                elif key == "initScore":
                    self.initScore = data[key]
                elif key == "endScore":
                    self.endScore = data[key]
                elif key == "turn":
                    self.turn = data[key]
                elif key == "totalTurns":
                    self.totalTurns = data[key]
                elif key == "players":
                    pid = 1
                    for player in data[key]:
                        self._createPlayer(pid, player)
                        pid += 1
        except Exception as e:
            print("Could not resume!")
            print("Exception: {}".format(e))
            exit(-1)

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
    def _createPlayer(self, num, values = None):
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

    def _getSaveData(self):
        # Leave out minPlayers, maxPlayers, and finished on purpose!
        data = {"numPlayers": self.numPlayers,
                "initScore": self.initScore,
                "endScore": self.endScore,
                "turn": self.turn,
                "totalTurns": self.totalTurns}
        plist = []
        for player in self.players.values():
            plist.append(player.toTuple())
        data["players"] = plist
        return data

    def _save(self):
        data = self._getSaveData()
        now = datetime.now()
        path = "{}.{}.json".format(self.name, now.isoformat())
        data = json.dumps(data)
        with open(path, "wt") as f:
            f.write(data)
        print("Saved to {}".format(path))
