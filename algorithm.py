from classes import *


class Algorithm:

    def getAction(self, state: MatchState):
        action = []  # The cards you are playing for this trick
        myData = state.myData  # Communications from the previous iteration

        # TODO Write your algorithm logic here

        return action, myData
