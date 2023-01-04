import random

class Dreidel():
    """Class to handle dreidel functions."""

    def __init__(self):
        """Initialize dreidel."""
        self.faces = ['shin', 'nun', 'gimmel', 'hay']
        self.history = []
        self.face_counts = {}

    def spin(self, player):
        """Append random selection from dreidel faces to spin history."""
        result = random.choice(self.faces)
        self.history.append((player, result))
        self.face_counts[result] = self.face_counts.get(result, 0) + 1
        return result

    def get_history(self):
        """Return spin history."""
        return self.history

    def get_last_spin(self):
        """Return most recent spin."""
        return self.get_history()[-1]

    def get_spins_count(self):
        """Return number of spins."""
        return len(self.get_history())
