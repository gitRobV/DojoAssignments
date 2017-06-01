var total = .01;
var counter = 0;

// for (var i = 0; i <= 30; i++) {
//     total += total;
//     console.log("Day " + i + " total: " + total);
// }


// while (total <= 10000) {
//     total += total;
//     counter++;
//     console.log("Day " + counter + " total: " + total);
// }



// while (total <= 1000000000) {
//     total += total;
//     counter++;
//     console.log("Day " + counter + " total: " + total);
// }


while (total < Infinity) {
    total += total;
    counter++;
    console.log("Day " + counter + " total: " + total);
}
