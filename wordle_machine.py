from collections import defaultdict
from typing import Callable, List, Tuple
from wordle import Wordle

EXPLORE_WORDS = ['aeros', 'unlit']

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
        result = [w for w in source if condition(w)]
        self.print('Number of possible words: {}'.format(len(result)))
        return result

    def select(self, source: List[str], i: str) -> str:
        guessed = source[0]
        if i < len(EXPLORE_WORDS):
            guessed = EXPLORE_WORDS[i]
        self.print(f'Guess {i+1}: ' + guessed)
        return guessed

    def guess(self, wordle: 'Wordle', guessed: str) -> str:
        # non-interactive mode
        result = wordle.guess(guessed)
        self.print('Result:  ' + result)
        return result

    def get_result(self) -> str:
        # interactive mode
        if self.quiet:
            raise Exception('Cannot use interactive mode in quiet mode.')
        print('Result:  ', end='')
        result = input()
        if len(result) == 5 or (set(result) - set('_!?')).empty():
            return result
        raise Exception('Input result is malformed! Must be 5 charactors of _, ! or ?')

    def run(self, wordle: 'Wordle' = None, n: int = 6) -> Tuple[str, int]:
        if not wordle:
            if self.quiet:
                print('Cannot use interactive mode in quiet mode.')
                return
            print('Interactive mode:')
        source = self.words.copy()
        guessed = self.select(source, 0)
        result = self.guess(wordle, guessed) if wordle else self.get_result()
        for i in range(1, n):
            source = self.filter(source, guessed, result)
            guessed = self.select(source, i)
            result = self.guess(wordle, guessed) if wordle else self.get_result()
            if result == '!!!!!':  # success
                self.print('Congrats!')
                return guessed, i+1
        if wordle:  # fail
            self.print('Sorry, correct answer is ' + wordle.word)
        return None, 7

def main():
    wordle_machine = WordleMachine(quiet=False)
    wordle_machine.run()

if __name__ == '__main__':
    main()
