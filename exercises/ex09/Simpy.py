"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730489972"


class Simpy:
    """Functions of Simpy Class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values attribute of the newly constructed Simpy object to the argument passed in."""
        self.values = values
    
    def __str__(self) -> str: 
        """Converts self to a str."""
        return f"Simpy({self.values})"
    
    def fill(self, val: float, fill: int) -> None:
        """Filling a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0 
        while i < fill:
            self.values.append(val)
            i = i + 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values att with range of values."""
        self.values = []
        if step > 0.0:
            next: float = start
            while next < stop:
                self.values.append(next)
                next = next + step
        else:
            last: float = start
            while last > stop:
                self.values.append(last)
                last = last + step
    
    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribite."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Reutrns a new Simpy object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(rhs + value)
        else:
            assert len(rhs.values) == len(self.values)
            i: int = 0 
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i = i + 1
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Reutrns a new Simpy object using power operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(rhs ** value)
        else:
            assert len(rhs.values) == len(self.values)
            i: int = 0 
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i = i + 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """If the floats are the same, it will return a boolean."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(rhs == value)
        else:
            i: int = 0 
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i = i + 1 
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """If the float is greater than, it will reutn a boolean."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(rhs < value)
        else:
            assert len(rhs.values) == len(self.values)
            i: int = 0 
            while i < len(self.values):
                result.values.append(rhs.values[i] < self.values[i])
                i = i + 1 
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns value at index."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            i: int = rhs
            return self.values[i]
        else:
            i: int = 0 
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i = i + 1 
        return result