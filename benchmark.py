from collections import Counter

from wordle import Wordle
from wordle_machine import WordleMachine

def benchmark(n: int = 6, N: int = 10000):
    print(f'max {n} guesses, {N} plays')
    wordle = Wordle()
    wordle_machine = WordleMachine()
    steps = Counter()
    failed_cnt = 0
    failed_words = []
    for _ in range(N):
        wordle.reset()
        answer, step = wordle_machine.run(wordle, n)
        if not answer:
            failed_cnt += 1
            failed_words.append(wordle.word)
        else:
            steps[step] += 1
    print('Success stats:  ', {i: steps[i] for i in range(1, n+1)})
    print('Success distro: ', {i: steps[i] / N for i in range(1, n+1)})
    print('Failed count and rate: ', failed_cnt, failed_cnt / N)
    # print('Failed words: ', failed_words)

if __name__ == "__main__":
    benchmark()
