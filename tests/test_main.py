import unittest
import main

class TestMain(unittest.TestCase):
    """Tests for main.py"""

    def setUp(self):
        # Create sample params to use 
        self.num_players_params = [3, 4, 5] 
        self.starting_bank_params = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.num_sims = 10


    def test_simulate(self):
        # Test that simulate function returns list of correct length
        iters = len(self.num_players_params) * len(self.starting_bank_params) * self.num_sims
        sim_results = main.simulate(self.num_players_params, self.starting_bank_params, self.num_sims)
        self.assertEqual(len(sim_results) - 1, iters)
