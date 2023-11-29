"""Node Class."""


from __future__ import annotations


__author__ = "730489972"


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

    def head(self) -> int: 
        """Returns the data attribut for the first element in a linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Returns a linked list of every element."""
        if self.data is None:
            return None
        return self.next
    
    def last(self) -> int | None:
        """Returns the data of the last element in the list."""
        if self.next is None:
            return None
        
        current_node = self.next
        while current_node.next is not None:
            current_node = current_node.next
        return current_node.data
        