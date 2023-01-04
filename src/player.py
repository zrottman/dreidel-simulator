from fund import Fund
from math import ceil

class Player():
    """
    A class to represent a player, which holds player name and a Fund
    object to represent player bankroll.

    Attributes:
        name (str): Player name
        bankroll (obj): Fund object to represent player bankroll.
    """

    def __init__(self, name, bankroll=10):
        """
        Initialize a new Player object.

        Args:
            name (str): Player name.
            bankroll (int, optional): Starting bankroll value. Default is 10.
        """

        self.name = name
        self.bankroll = Fund(bankroll)


    def take_action(self, spin_result, pot):
        """
        Update pot and player bankroll according to spin result.

        Args:
            spin_result (str): Result of dreidel spin. Valid values: hay,
                shin, nun, gimmel
            pot (obj): Fund object representing pot.
        """

        # Validate spin_result
        if spin_result not in ['hay', 'shin', 'gimmel', 'nun']:
            raise ValueError("Invalid spin result: {}".format(spin_result))

        # Append spin to history
        self.add_to_history(spin_result)

        # Take pot action
        if spin_result == 'shin': # Player puts 1 in
            self._update_pot(1, pot)
        elif spin_result == 'gimmel': # Player wins pot
            self._update_pot(-pot.get_value(), pot)
        elif spin_result == 'hay': # Player wins half pot
            self._update_pot(-ceil(pot.get_value() / 2), pot)
        elif spin_result == 'nun': # Player wins nothing
            pass
        

    def ante(self, pot, amt=1):
        """
        Increment pot value by one and decrement player bankroll by 1.
        
        Args:
            pot (obj): Fund object representing pot.
            amt (int, optional): Ante value. Default 1.
        """

        # Take pot action
        self._update_pot(amt, pot)


    def _udpate_pot(self, amt, pot):
        """
        Increment or decrement pot value and player bankroll by amt.

        Args:
            amt (int): Amount to increase pot/decrease player bankroll by.
            pot (obj): Fund object representing pot.
        """

        # Validate amt
        If not isinstance(amt, int):
            raise ValueError("Invalid amound: {}".format(amt))
        
        pot.update(amt)
        self.bankroll.update(-amt)

