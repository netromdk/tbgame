# -*- Coding: utf-8 -*-
# Triominos game implementation.

from Game import Game
from Player import Player
from util import getInt, getBool
from constants import CONSOLE

class Triominos(Game):
    def __init__(self):
        super().__init__()
        self.name = "Triominos"
        self.minPlayers = 2
        self.maxPlayers = 6
        self.curid = 1 # Current player ID

    def setup(self):
        super().setup()
        self.endScore = getInt("How many points to win?", default = 400)

    def nextTurn(self):
        super().nextTurn()

        # Stop if a player has reached the end game points and all
        # players have played their turn.
        if self._checkWinner(): return

        newRound = False
        curPlayer = self.players[self.curid]
        print("\n=== Turn {}: {} (#{}) ==="
              .format(self.turn, curPlayer.getName(), self.curid))
        while True:
            print("\n[T]ake (-5), [C]an't (-10), [P]lay, [S]ummary, [E]nd, [?] Help",
                  end = " ")
            data = input(CONSOLE).lower()
            if data not in ["t", "c", "p", "s", "e", "?"]:
                continue

            if data == "t":
                curPlayer.addScore(-5)
                continue

            elif data == "c":
                curPlayer.addScore(-10)
                break

            elif data == "p":
                score = getInt("How many points was played?", zeroable = True)

                while True:
                    print("[R]ound, [P]ass, [B]ridge (+40), [H]exagon (+50), [?] Help",
                          end = " ")
                    data = input(CONSOLE).lower()
                    if data not in ["b", "h", "r", "p", "?"]:
                        continue

                    if data == "r":
                        self._getRemainingPoints(self.curid, curPlayer)
                        newRound = True

                    elif data == "b":
                        score += 40
                        continue

                    elif data == "h":
                        score += 50
                        continue

                    elif data == "?":
                        print("\n[R]ound won\n"
                              "[P]ass turn\n"
                              "Made [B]ridge (+40)\n"
                              "Made [H]exagon (+50)\n")
                        continue

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

            elif data == "?":
                print("\n[T]ake piece (-5)\n"
                      "[C]an't play piece (-10)\n"
                      "[P]lay piece\n"
                      "[S]ummary\n"
                      "[E]nd game")
                continue

        self.curid += 1
        if self._checkWinner(): return
        if newRound or self.curid > self.numPlayers:
            self.curid = 1

    def start(self):
        print("\n=== Game started ===")
            
    def end(self):
        print("\n=== Game ended after {} turns ===".format(self.totalTurns))
        self._printSummary()
        (win, wid) = self._getWinner()
        print("The winner is {} with {} points!"
              .format(win.getName(), win.getScore()))
        if getBool("Save game state to resume later?"):
            self._save()

    def _createPlayer(self, num, values = None):
        if not values:
            while True:
                name = input("Name of player #{}: ".format(num))
                if len(name) == 0:
                    continue
                self._setPlayer(num, Player(name))
                break
        else:
            self._setPlayer(num, Player(*values))

    def _printSummary(self):
        print("\nGame Summary:")
        for num in self.players.keys():
            player = self.players[num]
            print("  {}: {}, {} points"
                  .format(num, player.getName(), player.getScore()))
        print("")

    def _checkWinner(self):
        (win, wid) = self._getWinner()
        if win.getScore() >= self.endScore and self.curid > self.numPlayers:
            print("\nGame is over because {} has {} points (end score is {})."
                  .format(win.getName(), win.getScore(), self.endScore))
            self._getRemainingPoints(wid, win)
            self._setFinished()
            return True
        return False

    def _getRemainingPoints(self, cid, cp):
        IDs = list(self.players.keys())
        IDs.remove(cid)
        points = 0
        for pid in IDs:
            player = self.players[pid]
            left = getInt("Piece values left for {}".format(player.getName()),
                          zeroable = True)
            points += left
        cp.addScore(points + 25)

