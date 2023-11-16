"""Practice for exam."""

def value_exists(value: dict[str, int], arg: int) -> bool:
    """Return true if val is in value."""
    exists: bool = False
    for element in value: 
        if value[element] == arg:
            exists = True 
        return exists 
    