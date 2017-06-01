/*
Random Chance
Let's play the slots!

Make a function that takes a number of quarters (1 quarter = 1 game).

There is a 1 in 100 chance to win the slot machine (which will give you between 50 - 100 quarters -- use Math.random and Math.floor to pick a random number of coins).

While the user still has quarters, use Math.random to determine if they won.

If they ever win, return the number of quarters (ex: they had 50 remaining quarters and won 90, so it should return 140).

Return 0 if all the quarters were wasted.

Bonus (Only If You Have Time):

Let the user pass the number they are willing to leave with
(ex: If they won the lottery and still have 40 coins, they will keep playing until they have collected 200 coins)
*/




// Determine users spin
//determine winning number



function slots(quarters, walkAway) {
    var userSpin;
    var jackpot;
    var winnning = Math.trunc(Math.random()*100);;
    var losses = 0;
    var wins = 0;
    var totalQuartersWon = 0;

    while (quarters > 0 ) {
        userSpin = Math.trunc(Math.random()*100);

        if (userSpin === winnning) {
            jackpot = Math.trunc(Math.random()*50)+51;
            totalQuartersWon += jackpot;
            quarters += jackpot;
            // console.log("Your Spin: " + spin);
            // console.log("Jackpot. You won " + jackpot + " quarters. you now have " + quarters + " left.");
            wins++;
            if (quarters > walkAway) {
                console.log("Walking Away with " + quarters + " Quarters");
                break;
            }

        } else {
            quarters--;
            // console.log("Your Spin: " + spin);
            // console.log("You did not win. You have " + quarters + " quarters left.");
            losses++
        }
    }
    console.log("Winning Spins: " + wins);
    console.log("Losing Spins: " + losses);
    console.log("Total Quarters Won: " + totalQuartersWon);
}

slots(100, 200);
