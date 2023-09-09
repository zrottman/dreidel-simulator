# Dreidel Simulator

It was the fifth night of Channukah, and I was shooting dreidel with the boys, which got me thinking: how long is this game gonna take? Do we have time to finish this--before latkes? Before night six? Before the new year?

To state the problem more generally: Given a certain number of players and a certain starting bankroll, how many spins is a typical game going to require before only one player remains with all the winnings? 

<figure>
<img src="/resources/dreidel-robot-3-cropped.png" alt="A robot taking notes on a game of dreidel (apparently)">
<figcaption align='center'>DALL-E 2's interpretation of a robot playing dreidel and taking notes</figcaption>
</figure>

## My Approach
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

# Takeaway #1: Death by a Thousand Spins
So how many spins *does* a typical dreidel game take? Too damn many!

![Distribution of spin counts for 4 player games, various starting bankrolls](/resources/dreidel-analysis_01.png)

We can immediately see that these distributions are positively skewed, meaning that there are games with very high spin counts that are going to bias the mean in that direction. Because of that, I'll rely on the median and interquartile range as better indicators of central tendency and variance, respectively.

Just as a larger bankroll results in longer 4-person games, more players will also result in higher spin counts:

![Distribution of spin counts for 5-unit bankroll games, various player counts](/resources/dreidel-analysis_02.png)

Putting it all together, here are the spin counts you can expect (i.e., median spin count with error bars indicating the interquartile range) varying both player count and starting bankroll:

![Median game spins, varying player count and bankroll](/resources/dreidel-analysis_03.png)

That's a lot of spins.

Here'a another way of visualizing the same data with more precise numbers:

![Median game spins, heatmap](/resources/dreidel-analysis_04.png)


# Takeaway #2: This Game Takes Way Too Damn Long

I'm not sure how many spins per minute a typical dreidel gang completes per minute, but 8 strikes me as a reasonably frenzied pace to sustain. Let's calculate game durations using that as an estimate.

![Median game duration, varying player count and bankroll](/resources/dreidel-analysis_05.png)

There is hope yet! As long as you keep your starting bankroll down and your spins/minute rate up, even a 6-person dreidel sesh can (usually) be wrapped in under 30 minutes. But if four dreidel fanatics get together and start the game with ten pieces of gelt each...yikes. That game could easily be an hour long.

Let's take a closer look at that 4-person scenario. It's Channukah and you and three homies are lookin' for some action. But not too much action. How many pieces of gelt do you each start with?

![Game duration for 4-player games](/resources/dreidel-analysis_06.png)

As long as the gang can keep twisting 8 times a minute, you should have things wrapped up in a half hour as long as you start with 5 units or less. You're pushing in with 6.

![Median game duration, heatmap](/resources/dreidel-analysis_07.png)


# Takeaway #3: This Game Ain't Fair

Turns out, you spin first, you got the edge. In fact, the earlier you are in the spin order, the better the chance you have at winning it all. Have a look:

![Player Order vs. Win Prob](/resources/dreidel-analysis_08.png)


<figure>
<img src="/resources/dreidel-robot-2.png" alt="A dreidling robot?">
<figcaption align='center'>Robot playing dreidel (something like that anyway), another DALL-E 2 joint</figcaption>
</figure>
