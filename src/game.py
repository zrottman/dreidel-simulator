from src.player import Player
from src.fund import Fund
from src.dreidel import Dreidel

class Game():
    """
    A class to represent the game. Holds instances of Dreidel, Fund (pot),
    and a list of Players. Stores an ongoing count of the number of rounds
    that have elapsed.

    Attributes:
        pot (obj): Fund object
        dreidel (obj): Driedel object
        players (arr): List containing Player objects
        round_count (int): Counter for number of rounds
    """

    def __init__(self, num_players, starting_bankroll):
        """
        Initialize a new Game instance.

        Args:
            num_players (int): number of players
            starting_bankroll (int): starting bankroll for players.
        """

        # Validate arguments
        if not isinstance(num_players, (int)):
            raise ValueError("Number of players arg must be an integer.")
        if not isinstance(starting_bankroll, (int)):
            raise ValueError("Starting bankroll arg must be an integer.")

        self.pot = Fund()
        self.dreidel = Dreidel()
        self.players = self._generate_players(num_players, starting_bankroll)
        self.round_count = 1
        self.num_players = num_players
        self.starting_bankroll = starting_bankroll

    
    def _generate_players(self, num_players, starting_bankroll):
        """
        Helper function to generate list of players.

        Args:
            num_players (int): Number of players
            starting_bankroll (int): Starting bankroll for players

        Returns:
            arr: List of Player objects
        """
        players = []
        for player in range(1, num_players + 1):
            name = 'player' + str(player).zfill(len(str(num_players)))
            players.append(Player(name, starting_bankroll))
        return players
        

    def play_round(self):
        """
        Execute a round. Each round consists of each player taking a turn.
        Before each turn, initiate ante if pot.value <=1.
        """
        
        # Loop through players list
        for ind, spinner in enumerate(self.players):

            # Ante if pot has 1 or fewer units
            if self.pot.get_value() <= 1:
                for player_to_ante in self.players:
                    player_to_ante.ante(self.pot)

            # Spin dreidel and take pot action
            if spinner.bankroll.get_value() >= 1:
                spin_result = self.dreidel.spin(spinner.get_name())
                spinner.take_action(spin_result, self.pot)

            # Remove players with depleted bankrolls
            if spinner.bankroll.get_value() < 1:
                self.players.pop(ind)

        self.round_count += 1


    def run_game(self):
        """
        Run entire game, looping play_round() until only one player remains.

        Returns:
            int: Number of players at start
            int: Starting bankroll
            str: Winners' name
            int: Number of rounds
            int: Number of spins
        """

        # Game loop
        while len(self.players) > 1:
            self.play_round()

        # Return results
        num_players = self.num_players
        starting_bankroll = self.starting_bankroll
        winner = self.players[0].name
        rounds = self.round_count
        spins = self.dreidel.get_current_spin_count()
        return num_players, starting_bankroll, winner, rounds, spins
