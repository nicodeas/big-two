# big-two
Originating in Hong Kong, Big Two is a strategic trick-taking card game that demands well-timed plays and tactical foresight. Players take turns playing valid cards or combinations (tricks) from their hands, aiming to be the first to empty their hand or to have the fewest cards when another player finishes. 

## Files
algorithm.py - the main entry point to the bot

compile.py - compiles files to an output file

objects/ - has all the separate classes and logic. Files inside this will be added to algorithm.py

imports.py - contains the necessary file imports that algorithm.py will use

match.py - holds info of the entire game, unused rn but we'll see

game.py - the game state, myData object will be created from this probably updated (subject to change as 
needed)

rank.py, suit.py - ranks and suits

hand.py - used to get different tricks from a given hand or set of cards

card.py - defines what a card is

compare.py - has all the comparators to compare different tricks

one_card.py - logic for what to do when we play a one card trick

two_card.py - logic for what to do when we play a two card trick

## Important files
compare.py
Effectively only has one output publicly used function which is `is_trick_stronger(trick1, trick2)`. This internally figures out how many cards in that trick: 1, 2, 3, 5 and returns whether trick1 is greater than trick2. 

algorithm.py
Based on how many cards in the trick, it calls a different function.
If it is the first move, or the initial move of the game, these get addressed by different functions.

one_card.py
This file has the logic for one card algos. One main public call that takes in relevant information and outputs the final trick to be played.

two_card.py 
Same thing as one_card.py but for two cards.

mock.py
Contains some mock objects for testing such as mock_match_state.

test_algorithm.py
Contains unit tests.

test.py
Sandbox testing file for manual testing.

compile.py
Probably don't need to touch, but it compiles everything into a single file.

## Editing workflow
If you create a new file that needs to be compiled, add it inside /objects and then add it to the list in compile.py
Add a comment: "# MERGE FROM HERE" from where the file needs to merge from. Add import statements before this comment.

Add this file to the list of imports inside imports.py

If you use any external libraries, import that into the main algorithm.py as well as wherever else u use it.

Testing is done by running: `pytest test_algorithm.py`. Depending on the import, this will test the non compiled version, or the compiled version. `from algorithm import *` or `from out.algorithm import *`. Make sure you test the compiled output after compiling.

To compile: `python3 compile.py`

Ideally functions used by algorithm.py should be pretty agnostic to the type of trick, so keep all the logic in internal files.




