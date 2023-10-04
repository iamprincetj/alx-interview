#!/usr/bin/python3

'''Lock boxes '''


def canUnlockAll(boxes):
    ''' A method that determines if all the boxes can be opened '''
    if boxes == 0:
        return False
    if not isinstance(boxes, list):
        return False
    if len(boxes) == 0:
        return False

    unlock = {0: "unlocked"}
    keys = [key for key in boxes[0] if key not in unlock]
    while keys:
        new_keys = []
        for key in keys:
            if key not in unlock and key < len(boxes):
                unlock[key] = "unlocked"
                new_keys += [i for i in boxes[key] if i not in unlock]
                keys = new_keys
    return len(unlock) == len(boxes)
