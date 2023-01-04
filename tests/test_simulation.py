import unittest
from src.simulation import Simulation

class TestSimulation(unittest.TestCase):
    """Tests for the class Simulation."""

    def setUp(self):
        # Create Simulation instance to use in tests
        num_players_params = [3, 4, 5] 
        starting_bankroll_params = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        num_sims = 10

        self.sim = Simulation(num_players_params, starting_bankroll_params, num_sims)
        self.iters = len(num_players_params) * len(starting_bankroll_params) * num_sims
        
    
    def test_init(self):
        # Test params stored correctly
        self.assertEqual(self.sim.num_players_params, [3, 4, 5])
        self.assertEqual(self.sim.starting_bank_params, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(self.sim.num_sims, 10)
        self.assertEqual(self.sim.sim_results, ['players,bankroll_start,winner,rounds,spins\n'])


    def test_run(self):
        self.sim.run()
        
        # Test results length is correct
        self.assertEqual(len(self.sim.get_results()) - 1, self.iters)
