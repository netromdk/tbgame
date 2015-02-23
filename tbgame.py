# -*- Coding: utf-8 -*-
# Requires python 3.x+

# tbgame implements turn-based games for making board games easier to
# play without requiring a lot of paper and pencils.
import sys
from games import Assano, Triominos

GAMES = {"assano": Assano,
         "triominos": Triominos}

def usage():
    print("Usage: {} [-h] <game> [<saved data>]".format(sys.argv[0]))
    print("Start new game or resume using saved data file.")
    print("\nAvailable games:")
    for g in GAMES:
        print("  {}".format(g))

if __name__ == "__main__":
    args = len(sys.argv)
    if args <= 1 or args > 3:
        usage()
        exit(-1)

    cmd = sys.argv[1].strip().lower()
    if cmd == "-h":
        usage()
        exit(0)

    savedData = None
    if args == 3:
        savedData = sys.argv[2]

    if not cmd in GAMES:
        print("Game not found: {}".format(cmd))
        exit(-1)

    print("Game: {}".format(cmd))
    if savedData:
        print("Resuming: {}".format(savedData))
    print("")

    game = GAMES[cmd]()
    if savedData:
        game.load(savedData)
    else:
        game.setup()
    game.start()
    while not game.isFinished():
        game.nextTurn()
    game.end()
