import unittest
from src.game import Game

class TestGame(unittest.TestCase):
    """Tests for the class Game"""

    def setUp(self):
        # Create Game instance to use in tests
        num_players = 4
        starting_bankroll = 10
        self.game = Game(num_players, starting_bankroll)


    def test_init(self):
        # Test correct number of players on initialization
        self.assertEqual(len(self.game.players), 4)

        # Test correct pot value on initialization
        self.assertEqual(self.game.pot.get_value(), 0)

        # Test correct bankroll values on initialization
        for player in self.game.players:
            self.assertEqual(player.bankroll.get_value(), 10)

        # Test num_players correctly initialized
        self.assertEqual(self.game.num_players, 4)

        # Test starting_bankroll correctly initialized
        self.assertEqual(self.game.starting_bankroll, 10)

        # Test round_count correctly initialized
        self.assertEqual(self.game.round_count, 1)

    
    def test_play_round(self):
        self.game.play_round()

        # Test correct round count after one round
        self.assertEqual(self.game.round_count, 2)

        # Test correct spin count after one round
        self.assertEqual(self.game.dreidel.get_current_spin_count(), 4)


if __name__ == '__main__':
    unittest.main()
