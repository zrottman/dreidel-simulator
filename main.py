from src.game import Game

def simulate(num_players_params, starting_bank_params, num_sims):
    """
    Runs simulations of multiple games, the parameters of which are 
    specified as arguments. Runs num_sims simulations with each combination of
    num_players_params and starting_bank_params. Total simulations = 
    len(num_players_params) x len(starting_bank_params) x num_sims.

    Args:
        num_players_params (arr): Iterable containing number of player
            combinations with which to run simulations
        starting_bank_params (arr): Iterable containing amounts to use
            for starting bankroll in simulations
        num_sims (int): number of simulations to run for each combination
            of num_players and starting_bank

    Returns:
        sim_results (arr): List where each item contains result of 1
            simulation:
            - number of players in simulation
            - starting bankroll in simulation
            - winner of simulation
            - number of rounds in simulation
            - number of spints in simulation
    """
    
    # Validate arguments
    if not isinstance(num_players_params, (range, list)):
        raise TypeError("num_players_params must be an iterable.")
    if not isinstance(starting_bank_params, (range, list)):
        raise TypeError("starting_bank_params must be an iterable.")
    if not isinstance(num_sims, int):
        raise TypeError("num_sims must be an integer.")
    
    # Initialize output variable with column headers
    sim_results = ['players,bankroll_start,winner,rounds,spins\n']

    # Loop through params and run simulations
    for num_players in num_players_params:
        for starting_bank in starting_bank_params:
            for i in range(num_sims):
                
                # Initialize new Game object
                my_game = Game(num_players, starting_bank)
                
                # Run sim and get results
                sim_result = my_game.run_game()
                
                # Append sim_result to sim_results
                sim_results.append('{},{},{},{},{}\n'.format(*sim_result))

    # Return results
    return sim_results

def write_to_file(sim_results, path):
    """
    Output sim_results to file.

    Args:
        sim_results (arr): List of simulation results
        path (str): file path
    """

    f = open(path, 'w')
    f.writelines(sim_results)
    f.close()
        
if __name__ == '__main__':

    # Define params
    starting_bank_params = range(5, 10)
    num_players_params = range(3, 6)
    num_sims = 3

    # Run simulation
    sim_results = simulate(num_players_params, starting_bank_params, num_sims)

    # Print results
    for result in sim_results:
        print(result, end='')
