# Wordle Machine (and Wordle) (in commandline)

My implementation of the Wordle game (inspired by https://www.powerlanguage.co.uk/wordle/) and my interactive solving machine for the Wordle game. The strategy is originated from this blog post [Best Wordle Strategy — Explore or Exploit](https://slc.is/#Best%20Wordle%20Strategy%20%E2%80%94%20Explore%20or%20Exploit) and I'm still working on some optimization over that.

### How to run?

```shell
git clone https://github.com/KevinXuxuxu/wordle_machine.git
cd wordle_machine
```

- Wordle game:
```shell
# need python 3
# ! for correct letter at correct position
# ? for correct letter at wrong position
# _ for wrong letter
$ python3.9 wordle.py        
Welcome to Wordle!
Guess 1: aeros    # <- your input
Result:  _!__!
Guess 2: unlit    # <- your input
Result:  ____?
Guess 3: techs    # <- your input
Result:  ?!_?!
Guess 4: heets    # <- your input
Guess must be a proper word with 5 letters!
Guess 4: hetts    # <- your input
Guess must be a proper word with 5 letters!
Guess 4: herts    # <- your input
Guess must be a proper word with 5 letters!
Guess 4: hetes    # <- your input
Result:  !!!!!
Congrats!
```

- wordle machine (interactive mode)
```shell
# need python 3
# next guess is given, input the response in same format
$ python3.9 wordle_machine.py
Interactive mode:
Guess 1: aeros
Result:  _?___    # <- your input
Number of possible words: 568
Guess 2: unlit
Result:  _?_?_    # <- your input
Number of possible words: 52
Guess 3: binge
Result:  _!!_!    # <- your input
Number of possible words: 7
Guess 4: jinne
Result:  _!!_!    # <- your input
Number of possible words: 6
Guess 5: mince
Result:  _!!!!    # <- your input
Number of possible words: 2
Guess 6: wince
Result:  !!!!!    # <- your input
Congrats!
```

### TODO
- Better word choosing strategy (now just the first word in the possible list)
- Better cmd option for alternate strategy choice
- NFT?
- Web 3.0?