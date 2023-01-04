import unittest
from src.dreidel import Dreidel
from src.player import Player

class TestDreidel(unittest.TestCase):
    """Tests for class Dreidel."""

    def setUp(self):
        # Create Dreidel and Player instances to use in test methods
        self.dreidel = Dreidel()
        self.player = Player('player1')

    def test_init(self):
        # Test dreidel initialization
        self.assertIn('hay', self.dreidel.faces)
        self.assertIn('shin', self.dreidel.faces)
        self.assertIn('gimmel', self.dreidel.faces)
        self.assertIn('nun', self.dreidel.faces)
        self.assertEqual(len(self.dreidel.faces), 4)
        self.assertEqual(self.dreidel.spin_count, 0)


    def test_dreidel_spin(self):
        """
        Test single dreidel spin.
        """
        # Spin dreidel and store result
        result = self.dreidel.spin(self.player)
        spin_count = self.dreidel.get_current_spin_count()
        history_length = len(self.dreidel.get_history())

        # Test spin result is valid
        self.assertIn(result, ['hay', 'gimmel', 'shin', 'nun'])

        # Test spin count
        self.assertEqual(spin_count, 1)

        # Test history length
        self.assertEqual(history_length, 1)


    def test_five_dreidel_spins(self):
        """
        Test five dreidel spins.
        """
        # Spin dreidel five times
        results = []
        for i in range(5):
            results.append(self.dreidel.spin(self.player))
        spin_count = self.dreidel.get_current_spin_count()
        history = self.dreidel.get_history()
        history_length = len(history)
            
        # Test valid spin results
        for result in results:
            self.assertIn(result, ['hay', 'shin', 'gimmel', 'nun'])

        # Test spin count
        self.assertEqual(spin_count, 5)

        # Test history length
        self.assertEqual(history_length, 5)
        
        # Test history
        for event in history:
            self.assertIsInstance(event[0], (int))
            self.assertEqual(event[1], 'player1')
            self.assertIn(event[2], ['hay', 'shin', 'gimmel', 'nun'])

if __name__ == '__main__':
    unittest.main()
