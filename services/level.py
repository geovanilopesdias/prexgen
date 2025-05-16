from enum import Enum

class Level():
    """
    Abstracts the level of difficulty of a problem.
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description