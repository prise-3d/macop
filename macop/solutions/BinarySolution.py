"""Binary solution class implementation
"""
import numpy as np

# modules imports
from .Solution import Solution


# Solution which stores solution data as binary array
class BinarySolution(Solution):
    """
    Binary integer solution class

    Attributes:
        data: {ndarray} --  array of binary values
        size: {int} -- size of binary array values
        score: {float} -- fitness score value
    """
    def __init__(self, data, size):
        """
        Initialize binary solution using specific data

        Args:
            data: {ndarray} --  array of binary values
            size: {int} -- size of binary array values
        """
        super().__init__(data, size)

    def random(self, validator):
        """
        Intialize binary array with use of validator to generate valid random solution

        Args:
            validator: {function} -- specific function which validates or not a solution

        Returns:
            {BinarySolution} -- new generated binary solution
        """

        self._data = np.random.randint(2, size=self._size)

        while not self.isValid(validator):
            self._data = np.random.randint(2, size=self._size)

        return self

    def __str__(self):
        return "Binary solution %s" % (self._data)
