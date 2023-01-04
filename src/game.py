from player import Player
from fund import Fund
from dreidel import Dreidel

class Game():
    """Class to manage running the game."""

    def __init__(self, num_players, starting_bankroll):
        """Initialize class."""
        self.my_pot = Fund()
        self.my_dreidel = Dreidel()
        self.players = []
        self.round_count = 1
        self.inactive_players = []
        self.num_players = num_players
        self.starting_bankroll = starting_bankroll

        # Create players
        for player in range(1, num_players + 1):
            name = 'player' + str(player).zfill(len(str(num_players)))
            self.players.append(Player(name, starting_bankroll))

    def play_round(self):
        """Handle round-actions."""

        for ind, player in enumerate(self.players):
            # Ante if pot has 1 or 0 units
            if self.my_pot.get_value() <= 1:
                for player_to_ante in self.players:
                    player_to_ante.ante(self.my_pot)

            # Spin dreidel and take pot action
            if player.bankroll.get_value() >= 1:
                spin_result = self.my_dreidel.spin(player.name)
                player.take_action(spin_result, self.my_pot)

            # Remove players with depleted bankrolls
            if player.bankroll.get_value() < 1:
                self.inactive_players.append(self.players.pop(ind))

        self.round_count += 1

    def display_bankrolls(self):
        """Display player bankrolls and pot value for debugging purposes."""
        
        for player in self.players:
            print("-{}: {}".format(player.name, player.bankroll.get_value()))
        print("-Pot: {}".format(self.my_pot.get_value()))


    def run_game(self):
        """Run game."""

        while len(self.players) > 1:
            self.play_round()

        #print("{} wins after {} rounds / {} spins".format(self.players[0].name, self.round_count, len(self.my_dreidel.get_history())))
        # Return results
        winner = self.players[0].name
        return "{},{},{},{},{}\n".format(self.num_players, self.starting_bankroll, winner, self.round_count, len(self.my_dreidel.get_history()))
        #self.inactive_players.append(self.players[0])


if __name__ == '__main__':

    num_players_params = range(3, 9)
    starting_bank_params = range(5, 16)
    sims = 1000
    results = ['players,bankroll_start,winner,rounds,spins\n']

    for num_players in num_players_params:
        print('{} players'.format(num_players), end='')
        for starting_bank in starting_bank_params:
            print(' - {}'.format(starting_bank), end='')
            #print("\n{} players, {} starting bank".format(num_players, starting_bank))
            for i in range(sims):
                my_game = Game(num_players, starting_bank)
                results.append(my_game.run_game())
        print()

    # Write results to file
    f = open('dreidel_data.csv', 'w')
    f.writelines(results)
    f.close()
