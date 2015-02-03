"""
Cruel Summer - A Simple Sum Number Guessing Game
"""


class CruelSummer(object):
    def __init__(self):
        self.answer = None
        self.numbers = []

    def play(self):
        try:
            self._play()
        except KeyboardInterrupt:
            print 'Bye'

    def _play(self):
        choice = raw_input("Choose a 5 digit number: ")
        try:
            choice = int(choice)
        except ValueError:
            raise SystemExit('The number is invalid')

        self.numbers.append(choice)
        self.answer = int('2' + str(choice - 2))
        print '\033[0;31mIn the end, the sum will be: \033[0;33m{0}\033[0m'.format(self.answer)

        choice = raw_input("Choose your second 5 digit number: ")
        try:
            choice = int(choice)
        except ValueError:
            raise SystemExit('The number is invalid')

        self.numbers.append(choice)
        my_choice = int(''.join([str(9-int(s)) for s in str(choice)]))
        self.numbers.append(my_choice)
        print '\033[0;32mMy number: \033[0;35m{0}\033[0m'.format(my_choice)

        choice = raw_input("Choose your last 5 digit number: ")
        try:
            choice = int(choice)
        except ValueError:
            raise SystemExit('The number is invalid')

        self.numbers.append(choice)
        my_choice = int(''.join([str(9-int(s)) for s in str(choice)]))
        self.numbers.append(my_choice)
        print '\033[0;32mMy number: \033[0;35m{0}\033[0m'.format(my_choice)

        print
        for count, num in enumerate(self.numbers):
            spacer = '  +' if num == self.numbers[-1] else ''
            template = '{0:4} {1:5}' if count % 2 else '{0:4} \033[0;35m{1:5}\033[0m'
            print template.format(spacer, num)
        print '-' * 13
        print '  = \033[0;33m{0}\033[0m'.format(self.answer)
        print '-' * 13

if __name__ == '__main__':
    CruelSummer().play()

