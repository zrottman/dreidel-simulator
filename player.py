from fund import Fund
from math import ceil

class Player():
    """Class to handle player attributes and methods."""

    def __init__(self, name, starting_bankroll):
        """Initialize player with name and starting bankroll."""

        self.name = name
        self.bankroll = Fund(starting_bankroll)
        self.history = []

    def take_action(self, spin_result, pot):
        """Spin dreidel and take appropriate pot action."""

        # Append spin to history
        self.add_to_history(spin_result)

        # Take pot action
        if spin_result == 'shin': # Player puts 1 in
            self._add_to_pot(1, pot)
        elif spin_result == 'gimmel': # Player wins pot
            self._take_from_pot(pot.get_value(), pot)
        elif spin_result == 'hay': # Player wins half pot
            self._take_from_pot(ceil(pot.get_value() / 2), pot)
        elif spin_result == 'nun': # Player wins nothing
            pass
        
    def ante(self, pot, amt=1):
        """Increment pot value by one and decrement bankroll by 1."""

        # Append ante event to history
        self.add_to_history('ante')

        # Take pot action
        self._add_to_pot(amt, pot)

    def _add_to_pot(self, amt, pot):
        """Incrememnt pot value and decrement bankroll."""
        pot.update(amt)
        self.bankroll.update(-amt)

    def _take_from_pot(self, amt, pot):
        """Decrement pot value and increment bankroll."""
        pot.update(-amt)
        self.bankroll.update(amt)

    def add_to_history(self, event):
        """Add event to player history."""
        self.history.append(event)

    def tally_history(self):
        """Tally events in history."""
        events = {}
        for event in self.history:
            events[event] = events.get(event, 0) + 1
        return events

    def get_history_count(self):
        """Return history length."""
        return len(self.history)

    def compute_history_pct(self):
        """Computer event occurrence percentages."""
        events = self.tally_history()
        events_pct = {}
        for key, value in events.items():
            events_pct[key] = value / self.get_history_count()
        return events_pct

