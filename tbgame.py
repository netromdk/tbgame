# -*- Coding: utf-8 -*-
# Requires python 3.x+

# tbgame implements turn-based games for making board games easier to
# play without requiring a lot of paper and pencils.
import sys
from Assano import Assano

GAMES = {"assano": Assano}

def usage():
    print("Usage: {} [-h] <game>".format(sys.argv[0]))
    print("\nAvailable games:")
    for g in GAMES:
        print("  {}".format(g))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        usage()
        exit(-1)

    cmd = sys.argv[1].strip().lower()
    if cmd == "-h":
        usage()
        exit(0)

    if not cmd in GAMES:
        print("Game not found: {}".format(cmd))
        exit(-1)
        
    print("Game: {}\n".format(cmd))
    game = GAMES[cmd]()
    game.setup()
    game.start()
    while not game.isFinished():
        game.nextTurn()
    game.end()
