#!/usr/bin/python3
"""
test the lockboxes function
"""

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [], [0, 4, 1], [5, 6], [3], [4, 1], [2]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))


boxes = []
print(canUnlockAll(boxes))

boxes = "[[1], [2], [3]]"
print(canUnlockAll(boxes))

boxes = [[1, 2], "b", [1], [3]]
print(canUnlockAll(boxes))
