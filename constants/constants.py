from enum import Enum

class RM(Enum):
    docks_esrel = 0
    lake_esrel = 1
    path_esrel = 2

class Direction(Enum):
    North = "north"
    Northeast = "northeast"
    East = "east"
    Southeast = "southeast"
    South = "south"
    Southwest = "southwest"
    West = "west"
    Northwest = "northwest"


class CT(Enum):
    VERB = "verb"
    NOUN = "noun"
    ARTICLE = "article"
    UNKNOWN = "unknown"
