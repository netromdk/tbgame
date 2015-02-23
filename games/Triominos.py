# -*- Coding: utf-8 -*-
# Triominos game implementation.

from Game import Game
from Player import Player
from util import getInt
from constants import CONSOLE

class Triominos(Game):
    def __init__(self):
        super().__init__()
        self.minPlayers = 2
        self.maxPlayers = 6
        self.curid = 1 # Current player ID

    def setup(self):
        super().setup()
        self.endScore = getInt("How many points to win?", default = 500)

    def nextTurn(self):
        super().nextTurn()

        newRound = False
        curPlayer = self.players[self.curid]
        print("\n=== Turn {}: {} (#{}) ==="
              .format(self.turn, curPlayer.getName(), self.curid))
        while True:
            print("\n[T]ake piece (-5)\n"
                  "[C]an't play piece (-10)\n"
                  "[P]lay piece\n"
                  "[S]ummary\n"
                  "[E]nd game\n", end = " ")
            data = input(CONSOLE).lower()
            if data not in ["t", "c", "p", "s", "e"]:
                continue

            if data == "t":
                curPlayer.addScore(-5)
                continue

            elif data == "c":
                curPlayer.addScore(-10)
                break

            elif data == "p":
                score = getInt("How many points was played?")

                while True:
                    print("Made [B]ridge (40)\n"
                          "Made [H]exagon (50)\n"
                          "[R]ound won\n"
                          "[P]ass turn\n", end = " ")
                    data = input(CONSOLE).lower()
                    if data not in ["b", "h", "r", "p"]:
                        continue

                    if data == "b":
                        score += 40
                        continue

                    elif data == "h":
                        score += 50
                        continue

                    elif data == "r":
                        IDs = list(self.players.keys())
                        IDs.remove(self.curid)
                        points = 0
                        for pid in IDs:
                            player = self.players[pid]
                            left = getInt("Piece values left for {}".format(player.getName()))
                            points += left
                        curPlayer.addScore(points + 25)
                        newRound = True
                    break

                curPlayer.addScore(score)
                if newRound:
                    self._resetTurns()
                    self._printSummary()
                break

            elif data == "b":
                curPlayer.addScore(40)
                continue

            elif data == "k":
                curPlayer.addScore(50)
                continue

            elif data == "s":
                self._printSummary()

            elif data == "e":
                self._setFinished()
                break

        if curPlayer.getScore() >= self.endScore:
            self._setFinished()
        else:
            self.curid += 1
            if newRound or self.curid > self.numPlayers:
                self.curid = 1

    def start(self):
        print("\n=== Game started ===")
            
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

            self._setPlayer(num, Player(name))
            break

    def _printSummary(self):
        print("\nGame Summary:")
        for num in self.players.keys():
            player = self.players[num]
            print("  {}: {}, {} points"
                  .format(num, player.getName(), player.getScore()))
        print("")

