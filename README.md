# Dreidel Simulator
A simple script to generate data for dreidel games. Specify the number of simulations to run as well as parameter ranges for number of players and starting bankroll.

## Game Rules
There are several variations of dreidel rules. Here are the ones this simulator abides by:

<ol>
    <li>Each player antes one unit to the pot to begin the game, so initially the pot will have as many units as players.</li>
    <li>Each player takes a turn spinning the dreidel and takes the appropriate action depending on which Hebrew letter shows:
        <ul>
            <li>"shin": player adds one unit to the pot</li>
            <li>"hay": player takes half the pot (rounding up on odd-numbered pot)</li>
            <li>"nun": no action</li>
            <li>"gimmel": player takes entire pot</li>
        </ul>
    </li>
    <li>When pot has one unit or less, all players ante one unit.</li>
    <li>When player's bankroll is depleted, that player is out, whether depletion occurs on spinning "shin" or on an ante.</li>
    <li>Game is over when only one player remains.</li>
</ol>
