#!/usr/bin/python3
"""
LockBox problem, part of ALX technical interview prepation
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.

    Write a method that determines if all the boxes
    can be opened.
"""


def canUnlockAll(boxes):
    """
     Determine if the boxes inside boxes can be opend

    Parameters:
    -----------
    boxes: list, list of lists, each list contain the index
           of the box inside boxes that can opens

    return:
    -----------
    boolean: True or False, if all boxes can be opend, false otherwise
    """

    if not isinstance(boxes, list):
        return False

    # contains the index of all boxes box, from 1 => 0 is already opened
    keys = [i for i in range(1, len(boxes))]

    for box in boxes:
        if not isinstance(box, list):
            return False
        try:
            [keys.remove(key) for key in box if key != boxes.index(box)]
        except ValueError:
            # the key is 0 or its aleardy removed
            pass
        if len(keys) == 0:
            return True

    print(f"remaining boxes => {[boxes[ky] for ky in keys]}")
    return len(keys) == 0
