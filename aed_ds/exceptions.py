class EmptyListException(Exception):
    """Executing non empty list methods on an empty list."""


class InvalidPositionException(Exception):
    """Accessing positions smaller or greater then the number of elements."""


class NoSuchElementException(Exception):
    """Reference to an element not present in the list."""
