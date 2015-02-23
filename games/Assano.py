# -*- Coding: utf-8 -*-
# Assano game implementation.

from Game import Game
from Player import Player
from util import getInt
from constants import CONSOLE

class Assano(Game):
    def __init__(self):
        super().__init__()
        self.minPlayers = 2
        self.maxPlayers = 6 # What is actual max?

    def setup(self):
        super().setup()
        self.endScore = getInt("How many points to win?", default = 500)

    def nextTurn(self):
        super().nextTurn()

        while True:
            print("Round finished [R], Summary [S] or End [E]", end=" ")
            data = input(CONSOLE).lower()
            if data not in ["r", "s", "e"]:
                continue

            if data == "r":
                IDs = list(self.players.keys())
                wid = getInt("Which player won the round? (player number)",
                             allowed = IDs)
                wp = self.players[wid]
                IDs.remove(wid)
                points = 0
                for pid in IDs:
                    player = self.players[pid]
                    score = getInt("Negative score for {}".format(player.getName()))
                    points += score
                    player.addScore(score * -1)
                wp.addScore(points)
                if wp.getScore() >= self.endScore:
                    self._setFinished()
                else:
                    self._printSummary()
                break

            elif data == "s":
                self._printSummary()

            elif data == "e":
                self._setFinished()
                break

    def start(self):
        print("\n=== Game started ===\n")
            
    def end(self):
        print("\n=== Game ended after {} turns ===".format(self.totalTurns))
        self._printSummary()
        win = self._getWinner()
        print("The winner is {} with {} points!"
              .format(win.getName(), win.getScore()))

    def _createPlayer(self, num):
        while True:
            name = input("Name of player #{}: ".format(num))
            if len(name) == 0:
                continue

            score = getInt("Initial score of player #{}".format(num),
                           default = self.initScore,
                           signed = False)
            
            self._setPlayer(num, Player(name, score))
            break

    def _printSummary(self):
        print("\nGame Summary:")
        for num in self.players.keys():
            player = self.players[num]
            print("  {}: {}, {} points"
                  .format(num, player.getName(), player.getScore()))
        print("")
