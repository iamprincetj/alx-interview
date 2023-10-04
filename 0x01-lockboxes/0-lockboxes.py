#!/usr/bin/python3

'''Lock boxes '''


def canUnlockAll(boxes):
    ''' A method that determines if all the boxes can be opened '''
    if not boxes or type(boxes) is not list:
    return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    return len(unlocked) == len(boxes)
