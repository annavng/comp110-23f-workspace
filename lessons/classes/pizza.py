"""Defining a class"""

from __future__ import annotations

class Pizza:

    # attributes
    #think of tjese as the variables each instance of my class will have 
    #<name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, gf: bool):
        self.size = inp_size
        self_toppings = inp_toppings
        self_gluten_free = gf
        # returns a pizza object for me 

    def price(self) -> float:
        """calculate price."""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00


    def add_toppings(self, num_toppings: int):
        """Add toppings to existing pizza"""
        self.toppings += num_toppings

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        new_pizza: Pizza = Pizza(self.size, num_toppings, self.gluten_free)
        return new_pizza