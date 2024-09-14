from algorithm import *
from mock import mock_match_state
algo = Algorithm()
action, myData = algo.getAction(state=mock_match_state)

print(action)
print(type(action[0]))
print(myData)
