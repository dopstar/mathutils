"""
George Andrew's Game
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import fibonacci, zeckendorf


class Andrew(object):
    cards = {}

    def __init__(self):
        self.create_cards()

    def create_cards(self):
        fibs = []
        for fib in fibonacci():
            if len(fibs) >= 8:
                break
            if fib != 0 and fib not in fibs:
                fibs.append(fib)
                self.cards.setdefault(fib, [])
        for zkd, card in self.cards.iteritems():
            for n in xrange(1, 200):
                if len(card) >= 25:
                    break
                if n not in card and zkd in zeckendorf(n):
                    card.append(n)

    def show_cards(self, cards=None):
        cards = cards if cards is not None else self.cards
        for zkd, card in cards.iteritems():
            print
            print ' '.join(map(str, card[0:5]))
            print ' '.join(map(str, card[5:10]))
            print ' '.join(map(str, card[10:15]))
            print ' '.join(map(str, card[15:20]))
            print

    def play(self):
        try:
            self._play()
        except KeyboardInterrupt:
            print 'Bye'

    def _play(self):
        raw_input("Pick a whole number between 1 and 50. I will tell you what you have chosen.")
        zeckendorf_sequence = []
        os.system('clear')
        for zkd, card in self.cards.iteritems():
            self.show_cards(cards={zkd: card})
            choice = raw_input("Is your number in the numbers above? [y/N] ")
            choice = choice.lower()
            if choice in ('y', 'yes'):
                zeckendorf_sequence.append(zkd)
            os.system('clear')
        print "Your number that you have picked is: {0}".format(sum(zeckendorf_sequence))