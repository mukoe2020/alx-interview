#!/usr/bin/python3
"""
the lockboxe problem:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1,
and each box may contain keys to the other boxes.
* A key with the same number as a box opens that box.
* You can assume all keys will be positive integers.
* There can be keys that do not have boxes.
* The first box boxes[0] is unlocked.
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened

    Args:
        boxes (list): the boxes that contain keys.

    Returns:
        Boolean:  True if all boxes can be opened, else return False.
    """
    start = True
    n = len(boxes)
    new_l = [False for i in range(n)]
    new_l[0] = True
    old_l = new_l[:]
    while (new_l != old_l or start is True):
        start = False
        old_l = new_l[:]
        for i in range(n):
            if new_l[i]:
                for j in boxes[i]:
                    try:
                        new_l[j] = True
                    except (IndexError):
                        pass
    return all(new_l)
