# encoding: utf-8

"""
Data point-related objects.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from collections import Sequence


class _BasePoints(Sequence):
    """
    Sequence providing access to the individual data points in a series.
    """
    def __init__(self, ser):
        super(_BasePoints, self).__init__()
        self._element = ser
        self._ser = ser

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.__len__():
            raise IndexError('point index out of range')
        return Point(self._ser, idx)


class BubblePoints(_BasePoints):
    """
    Sequence providing access to the individual data points in a series.
    """
    def __len__(self):
        return min(
            self._ser.xVal_ptCount_val,
            self._ser.yVal_ptCount_val,
            self._ser.bubbleSize_ptCount_val
        )


class Point(object):
    """
    Provides access to the properties of an individual data point in
    a series, such as the visual properties of its marker and the text and
    font of its data label.
    """
    def __init__(self, ser, idx):
        super(Point, self).__init__()
        self._element = ser
        self._ser = ser
        self._idx = idx


class XyPoints(_BasePoints):
    """
    Sequence providing access to the individual data points in a series.
    """
    def __len__(self):
        return min(self._ser.xVal_ptCount_val, self._ser.yVal_ptCount_val)
