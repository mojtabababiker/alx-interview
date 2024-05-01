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
     Determine if the boxes inside boxes can be opened

    Parameters:
    -----------
    boxes: list, list of lists, each list contain the index
           of the box inside boxes that can opens

    return:
    -----------
    boolean: True or False, if all boxes can be opened, false otherwise
    """

    if not isinstance(boxes, list):
        return False

    opened_boxes = [0]  # save the opened boxes qeuee
    keys = [0]  # opened box
    all_boxes = len(boxes)

    while opened_boxes and boxes:
        current_box = boxes[opened_boxes.pop(0)]
        for key in current_box:
            if key not in keys and key < all_boxes:
                opened_boxes.append(key)
                keys.append(key)

        if len(keys) == all_boxes:
            return True
    return len(keys) == all_boxes

    """
    keys = [i for i in range(1, len(boxes))]
    for box, box_index in enumerate(boxes):
        if box_index in opened_boxes:
            try:
                [(keys.remove(key), opened_box.add(key))
                 for key in box if key != box_index]
            except Exception:
                # the key is 0 or, its aleardy removed or outof range
                pass


        if len(keys) == 0:
            return True

    return len(keys) == 0
    """
