class Fund():
    """
    Class to handle attributes and methods of the fund objects
    (player bankrolls and pot).
    """

    def __init__(self, value=0):
        """Initialize fund object."""
        self.value = value

    def update(self, amt):
        """Update fund value."""
        if self.value + amt >= 0:
            self.value += amt
            return 1
        else:
            return -1

    def get_value(self):
        """Return current fund value."""
        return self.value

