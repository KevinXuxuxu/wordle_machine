from collections import Counter
from random import choice

class NotAWordException(Exception):
    pass

class Wordle:

    def __init__(self, word: str = None, load: bool = True):
        self.words = None
        if load or not word:
            with open('word_list.txt', 'r') as f:
                self.words = set([line.strip() for line in f.readlines()])
        self.word = word if word else choice(list(self.words))

    def reset(self, word: str = None):
        if not word:
            if not self.words:
                raise Exception('Words not loaded, must set a word to reset!')
            self.word = choice(list(self.words))
        else:
            self.word = word

    def guess(self, guessed: str) -> str:
        if self.words and guessed not in self.words:
            raise NotAWordException()
        rtn = [_ for _ in '_____']
        cnt = Counter(self.word)
        for i, c in enumerate(self.word):
            if c == guessed[i]:
                rtn[i] = '!'
                cnt[c] -= 1
        for i, c in enumerate(self.word):
            g = guessed[i]
            if g == c:
                continue
            elif cnt[g] > 0:
                rtn[i] = '?'
        return ''.join(rtn)

def main():
    W = Wordle()
    print('Welcome to Wordle!')
    i = 1
    while i <= 6:
        print(f'Guess {i}: ', end='')
        guessed = input()
        try:
            print('Result:  ' + W.guess(guessed))
            if guessed == W.word:
                print('Congrats!')
                return
            i += 1
        except NotAWordException:
            print('Guess must be a proper word with 5 letters!')
    print('Sorry! The correct word is ' + W.word)

if __name__ == '__main__':
    main()
