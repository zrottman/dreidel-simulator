from src.game import Game

class Simulation():
    """
    A class to represent simulations of multiple games, whose parameters
    are specified when a Simulation class is instantiated. This class holds
    the results of the simulations and allows for those results to be
    output to a file.

    Attributes:
        num_players_params (arr): Iterable containing number of player
            combinations with which to run simulations
        starting_bank_params (arr): Iterable containing amounts to use
            for starting bankroll in simulations
        num_sims (int): number of simulations to run for each combination
            of num_players and starting_bank
    """

    def __init__(self, num_players_params, starting_bank_params, num_sims):
        """
        Initialize Simulation object.

        Args:
            num_players_params (arr): Iterable containing number of players
                to use in simulations
            starting_bank_params (arr): Iterable containing amounts to use
                for starting bankroll in simulations
            num_sims (int): Number of simulations to run for each combination
                of num_players and starting_bank
            sim_results (arr): List where each item contains result of 1
                simulation:
                - number of players in simulation
                - starting bankroll in simulation
                - winner of simulation
                - number of rounds in simulation
                - number of spints in simulation
        """
        
        # Validate arguments
        if not isinstance(num_players_params, list):
            raise ValueError("num_players_params must be an iterable.")
        if not isinstance(starting_bank_params, list):
            raise ValueError("starting_bank_params must be an iterable.")
        if not isinstance(num_sims, int):
            raise ValueError("num_sims must be an integer.")
            
        self.num_players_params = num_players_params
        self.starting_bank_params = starting_bank_params
        self.num_sims = num_sims
        self.sim_results = ['players,bankroll_start,winner,rounds,spins\n']

    def run(self):
        """
        Run num_sims simulations with each combination of num_players_params
        and starting_bank_params. Total simulations = len(num_players_params) x
        len(starting_bank_params) x num_sims. Store results of simulations in
        sim_results.
        """

        for num_players in self.num_players_params:
            for starting_bank in self.starting_bank_params:
                for i in range(self.num_sims):
                    my_game = Game(num_players, starting_bank)
                    players, bankroll, winner, rounds, spins = my_game.run_game()
                    self.sim_results.append('{},{},{},{},{}\n'
                        .format(players,bankroll,winner,rounds,spins))

    def get_results(self):
        """
        Return sim_results.

        Returns:
            arr: List of sim results
        """
        return self.sim_results


    def output_data(self, path):
        """
        Output sim_results to file.

        Args:
            path (str): file path
        """
        f = open(path, 'w')
        f.writelines(self.get_results())
        f.close()

        
if __name__ == '__main__':

    # Define params
    starting_bank_params = range(5, 16)
    num_players_params = range(3, 9)
    num_sims = 10

    simulation = Simulation(num_players_params, starting_bank_params, num_sims)
    simulation.run()
    print(simulation.get_results())
