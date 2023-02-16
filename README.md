# Dreidel Simulator
It was the fifth night of Channukah, and I was shooting dreidel with the boys, which got me thinking: how long is this game gonna take? Do we have time to finish this--before latkes? Before night six? Before the new year?

To state the problem more generally: Given a certain number of players and a certain starting bankroll, how many spins is a typical game going to require before only one player remains with all the winnings? 

I took an empirical approach to the problem. I built a simulator to generate 120,000 dreidel games with various numbers of players and various starting bankgrolls, and I crunched this data to arrive at the answer: Dreidel takes too damn long. If you insist on starting a game and seeing it through til the bitter end, well, make sure that your starting bankrolls are very small. Otherwise it'll take a whole lot longer than 8 days until a victor emerges with all the gelt.

## Game Rules by which Simulator Abides
There are several variations of dreidel rules. Here are the ones by which this simulator abides:

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
