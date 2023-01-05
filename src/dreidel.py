import random

class Dreidel():
    """
    A class that represents a dreidel, which holds four dreidel faces
    and a spin history.

    Attributes:
        faces (arr): List of dreidel faces
        history (arr): List of spin history. Each list item is a list
            containing [spin_number, player_name, result]
        spin_count (int): Current number of spins
    """

    def __init__(self):
        """
        Initialize a new Driedel object.
        """
        self.faces = ['shin', 'nun', 'gimmel', 'hay']
        self.history = []
        self.spin_count = 0


    def spin(self, player_name):
        """
        Spin dreidel, append result to history, and return result.

        Args:
            player (obj): Player object who is spinning.

        Returns:
            str: Name of dreidel face that results.
       """
        
        # Vaildate player_name
        if not isinstance(player_name, str):
            raise TypeError('player_name passed must be string.')

        # Increment spin_count
        self.spin_count += 1

        # Get spin result
        result = random.choice(self.faces)

        # Add spin details to history
        spin_number = self.get_current_spin_count()
        self.history.append([spin_number, player_name, result])

        return result


    def get_history(self):
        """
        Return spin history.

        Returns:
            arr: List of spin history.
        """

        return self.history

    def get_current_spin_count(self):
        """
        Returns current spin count.

        Returns:
            int: Spin count
        """
        
        return self.spin_count
