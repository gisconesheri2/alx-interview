#!/usr/bin/python3
"""
Functionality to open locked boxes
"""
from typing import Set, List, Tuple


def open_boxes(keys: Set[int], boxes_open: Set[int], boxes: List[List[int]]) -> Tuple[Set[int], Set[int], List[int]]:
    """
    Open a box:
        @keys - set of integers representing current keys available
        @boxes_open - set of integers reresenting boxes already open
        @boxes - list of lists; inner list represent a box containing
            zero or more keys

        Return:
            keys - an updated @keys containig any extra keys found
            boxes_open - an updated @boxes_open containing any extra
                boxes opened
            box_keys - keys found in current iteration
    """
    box_keys = []
    for key in keys:
        # there is a direct relation between  keys and boxes_open
        if key not in boxes_open:
            # there can be keys that do not have boxes
            if key < len(boxes):
                for unknown_key in boxes[key]:
                    box_keys.append(unknown_key)
                boxes_open.add(key)
    # add unique keys found to the keys set
    for k in box_keys:
        keys.add(k)
    return (keys, boxes_open, box_keys)


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    checks if all boxes in boxes can be opened
    @boxes: list of lists; inner lists represent boxes which can have
            zero or more keys to open other boxe
    """
    # first box is always open
    keys_out = {0}
    boxes_open_out = {0}

    # add keys in first box to known keys
    for k in boxes[0]:
        keys_out.add(k)

    box_keys_out = boxes[0]
    # when all boxes that can be opened are opened,
    # or all keys that can be found are found
    # box_keys_out will be an empty list
    while len(box_keys_out) > 0:
        keys_out, boxes_open_out, \
            box_keys_out = open_boxes(keys_out, boxes_open_out, boxes)

    if len(boxes_open_out) == len(boxes):
        return True
    else:
        return False

boxes = [[1], [2], [3], [4], []]
print(type(boxes))
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [5, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))