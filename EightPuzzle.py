import random

goalState =    [[1,2,3],
                [4,5,6],
                [7,8,0]]

currentState =    [[1,2,3],
                  [4,5,6],
                [7,8,0]]

class EightPuzzleManager:
    def __init__(self):
        pass

    def stateIsMatch(self,state1,state2):
        if state1==state2:
            return True
        else:
            return False


if __name__ == '__main__':
    print(len(goalState))
    x = EightPuzzleManager()
    y = x.stateIsMatch(currentState,goalState)
    print(y)
    