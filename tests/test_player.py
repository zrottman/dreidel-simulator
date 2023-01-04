import unittest
from src.player import Player
from src.dreidel import Dreidel
from src.fund import Fund

class TestPlayer(unittest.TestCase):
    """Tests for the class Player."""

    def setUp(self):
        # Create Player instance to use in select tests
        name = 'John'
        starting_bankroll = 10
        self.player = Player(name, starting_bankroll)
        self.dreidel = Dreidel()
        self.pot = Fund(10)


    def test_init(self):
        # Test default initialization
        player = Player('player1')
        self.assertEqual(player.name, 'player1')
        self.assertEqual(player.bankroll.value, 10)

        # Test custom initialization
        player = Player('player1', bankroll=15)
        self.assertEqual(player.name, 'player1')
        self.assertEqual(player.bankroll.value, 15)


    def test_ante_default(self):
        # Test default ante implementation
        self.player.ante(self.pot)
        self.assertEqual(self.player.bankroll.value, 9)
        self.assertEqual(self.pot.value, 11)

    def test_ante_custom(self):
        # Test custom ante implementation
        self.player.ante(self.pot, amt=2)
        self.assertEqual(self.player.bankroll.value, 8)
        self.assertEqual(self.pot.value, 12)


    def test_take_action_shin(self):
        # Test updating pot and player bankroll on `shin`
        self.player.take_action('shin', self.pot)
        self.assertEqual(self.player.bankroll.get_value(), 9)
        self.assertEqual(self.pot.get_value(), 11)


    def test_take_action_hay(self):
        # Test updating pot and player bankroll on `hay`
        self.player.take_action('hay', self.pot)
        self.assertEqual(self.player.bankroll.get_value(), 15)
        self.assertEqual(self.pot.get_value(), 5)


    def test_take_action_hay_odd_pot(self):
        # Test updating pot and player bankroll on `hay` with odd pot value
        self.pot.update(1)
        self.player.take_action('hay', self.pot)
        self.assertEqual(self.player.bankroll.get_value(), 16)
        self.assertEqual(self.pot.get_value(), 5)
        

    def test_take_action_gimmel(self):
        # Test updating pot and player bankroll on `gimmel`
        self.player.take_action('gimmel', self.pot)
        self.assertEqual(self.player.bankroll.get_value(), 20)
        self.assertEqual(self.pot.get_value(), 0)


    def test_take_action_nun(self):
        # Test updating pot and player bankroll on `nun`
        self.player.take_action('nun', self.pot)
        self.assertEqual(self.player.bankroll.get_value(), 10)
        self.assertEqual(self.pot.get_value(), 10)


    def test_spin_sequence_1(self):
        # Test updating pot and player bankroll after specific spin sequence.
        sequence = ['hay', 'shin', 'hay', 'nun', 'gimmel', 'shin']
        for spin in sequence:
            self.player.take_action(spin, self.pot)
        self.assertEqual(self.player.bankroll.get_value(), 19)
        self.assertEqual(self.pot.get_value(), 1)


    def test_spin_sequence_2(self):
        # Test updating pot and player bankroll after specific spin sequence.
        sequence = ['shin', 'nun', 'hay', 'shin', 'hay', 'shin']
        for spin in sequence:
            self.player.take_action(spin, self.pot)
        self.assertEqual(self.player.bankroll.get_value(), 16)
        self.assertEqual(self.pot.get_value(), 4)

    
    def test_get_name(self):
        # Test get_name function
        player = Player('player2')
        self.assertEqual(player.get_name(), 'player2')
