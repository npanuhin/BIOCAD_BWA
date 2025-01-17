from typing import List
from collections import deque


class Line:
    """
    Properties:
        start_x  {0}
        start_y  {1}
        end_x    {2}
        end_y    {3}
        dots = [dot1, ..., dotN] {4}
        coords = (start_x, start_y, end_x, end_y)
    """

    def __init__(self, start_x=None, start_y=None, end_x=None, end_y=None, dots=[]):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.dots = dots

    def __repr__(self):
        return "Line(start_x={}, start_y={}, end_x={}, end_y={}, dots=[{}])".format(
            self.start_x, self.start_y, self.end_x, self.end_y, len(self.dots)
        )

    @property
    def coords(self):
        return self.start_x, self.start_y, self.end_x, self.end_y

    # @property
    # def x1(self):
    #     return self.start_x

    # @property
    # def y1(self):
    #     return self.start_y

    # @property
    # def x2(self):
    #     return self.end_x

    # @property
    # def y2(self):
    #     return self.end_y

    @property
    def center_x(self):
        return (self.start_x + self.end_x) // 2

    @property
    def center_y(self):
        return (self.start_y + self.end_y) // 2

    def isTiltedCorrectly(self):
        return self.start_y <= self.end_y

    @property
    def k(self):
        return (self.end_y - self.start_y) / (self.end_x - self.start_x)

    @property
    def b(self):
        return self.end_y - self.end_x * self.k

    def copyCoords(self):
        return Line(self.start_x, self.start_y, self.end_x, self.end_y, dots=[])

    def shift(self, dx=0, dy=0):
        self.start_x += dx
        self.start_y += dy
        self.end_x += dx
        self.end_y += dy
        for i in range(len(self.dots)):
            self.dots[i][0] += dx
            self.dots[i][1] += dy

    def rotateY(self, rotation_center, line=True, dots=False):
        if line:
            self.start_y -= (self.start_y - rotation_center) * 2
            self.end_y -= (self.end_y - rotation_center) * 2

        if dots:
            for i in range(len(self.dots)):
                self.dots[i][1] -= (self.dots[i][1] - rotation_center) * 2


def shiftLines(lines, count) -> List[Line]:
    result = deque(lines)
    for _ in range(count):
        result.append(result.popleft())
    return list(result)
