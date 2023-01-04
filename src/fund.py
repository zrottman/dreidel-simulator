class Fund():
    """
    A class to represent a fund object (e.g., player bankrolls or
    pot), which can hold a current value and have funds added or 
    deducted.

    Attributes:
        value (int): Current value of the fund
        min_value (int): The minimum allowable value for fund.
    """

    def __init__(self, value=0, min_value=0):
        """
        Initialize a new Fund object.

        Args:
            value (int, optional): Initial value of fund. Default is 0
            min_value (int, optional): Minimum allowable value for fund.
                Default is 0.
        """
        self.value = value
        self.min_value = min_value


    def update(self, amt):
        """
        Update the value of a fund by a given amount.

        Args:
            amt (int): The amount to add or subtract from the fund

        Returns:
            int: 1 if the update was successful, -1 if the update would have
                resulted in a fund value less than the minimum allowable
                value
        """
        if not isinstance(amt, (int)):
            raise ValueError("Amount must be an integer.")
            
        if self.value + amt >= self.get_min_value():
            self.value += amt
            return 1
        else:
            return -1


    def get_value(self):
        """
        Return the current value of the fund.

        Returns:
            int: Current value of the fund.
        """
        return self.value
    

    def get_min_value(self):
        """
        Return the minimum allowable value for the fund.

        Returns:
            int: Minimum allowable value for the fund.
        """
        return self.min_value
