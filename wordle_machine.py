from collections import defaultdict
from typing import Callable, List
from wordle import Wordle

FIRST_GUESS = 'audio'

class WordleMachine:

    def __init__(self, quiet: bool = True):
        self.quiet = quiet
        with open('word_list.txt', 'r') as f:
            self.words = [l.strip() for l in f.readlines()]

    def print(self, sth):
        if not self.quiet:
            print(sth)

    def filter(self, source: List[str], guessed: str, result: str) -> List[str]:
        q_letters = defaultdict(list)
        e_letters = defaultdict(list)
        n_letters = set()
        for i, c in enumerate(guessed):
            if result[i] == '_':
                n_letters.add(c)
            elif result[i] == '?':
                q_letters[c].append(i)
            else:  # '!'
                e_letters[c].append(i)
        def condition(word: str) -> bool:
            w = [_ for _ in word]
            for e in e_letters:
                for i in e_letters[e]:
                    if w[i] != e:
                        return False
                    w[i] = '*'
            for q in q_letters:
                if q not in w:
                    return False
                for i in q_letters[q]:
                    if w[i] == q:
                        return False
            for n in n_letters:
                if n in w:
                    return False
            return True
        return [w for w in source if condition(w)]

    def run(self, wordle: 'Wordle', n: int = 6) -> str:
        guessed = FIRST_GUESS
        self.print('Guess 1: ' + guessed)
        result = wordle.guess(guessed)
        self.print('Result:  ' + result)
        source = self.words.copy()
        for i in range(1, n):
            source = self.filter(source, guessed, result)
            self.print(len(source))
            if len(source) < 100:
                self.print(source)
            guessed = source[0]
            self.print(f'Guess {i+1}: ' + guessed)
            result = wordle.guess(guessed)
            self.print('Result:  ' + result)
            if result == '!!!!!':
                self.print('Congrats!')
                return guessed
        self.print('Sorry, correct answer is ' + wordle.word)
        return None
